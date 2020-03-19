======
Errors
======
All error responses sent by the API have a unified structure. Each error
response contains two contextual keys: :code:`query` and
:code:`error.error_context`. The former just mirrors specified request
parameters while the latter contains contextual error data that is specific
for an endpoint to which the request was sent.

See :ref:`error-types` for a list of all defined errors.

---------
Structure
---------

.. json:object:: Error Response

    General structure of an error response.

    :property object query: Contextual information about the query that was
                            performed. Essentially, this object just mirrors
                            request parameters that were specified (after
                            a disambiguation and resolution process). Object
                            structure is defined individually for each API
                            endpoint. See `Query Object
                            <response-structure.html#query-object>`_ for a
                            half-decent generalization of this object's
                            structure. May be absent.

    :property object error: Error object that was returned. Always present.

    :proptype error: :json:object:`Error Object`

.. json:object:: Error Object

    Error object structure.

    :property string error_name:    Name of an error that occured. Always
                                    present.

    :property string error_desc:    Description of an error that occured. It is
                                    static and is defined by the error itself,
                                    not a request that was sent. Always
                                    present.

    :property object error_context: A nested object with a contextual
                                    information about the error. Object
                                    structure is defined individually for each
                                    API endpoint. May be absent.

--------
Examples
--------
An example of a full-fledged error response:

.. sourcecode:: json

    {
        "query": {
            "action": "search_subdomains",
            "parameters": {
                "domain": "example.com",
                "iv.history": true
            }
        },
        "error": {
            "error_name": "bad_request",
            "error_description": "Request is malformed",
            "error_context": {
                "invalid_parameter_name": "iv.history",
                "valid_parameter_names": [
                    "ipv4.history",
                    "ipv4.latest",
                    "ipv4.live",
                    "ipv4.meta",
                    "ipv4.oldest",
                    "ipv6.history",
                    "ipv6.latest",
                    "ipv6.live",
                    "ipv6.meta",
                    "ipv6.oldest"
                ]
            }
        }
    }

.. _error-types:

-----------
Error Types
-----------

The majority of error types are tied to a specific HTTP status code though
this is not always the case (i.e. both :ref:`empty-result-error` and
:ref:`no-such-endpoint-error` are returned with :http:statuscode:`404`). It is
advised to always check the response body to determine which type of error has
occured.

While the majority of API errors are documented here, there is a chance that
client will receive an undocumented error. These can be treated according to
HTTP response status they are returned with completely ignoring the response
body.

.. _bad-request-error:

^^^^^^^^^^^
Bad Request
^^^^^^^^^^^

Request object structure is malformed. This error usually contains more
information about what is exactly malformed in `error.error_context` object.
Context object structure usually differs depending on an endpoint.

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`400`
      - :code:`bad_request`
      - :code:`Request object structure is malformed`

Example:

.. sourcecode:: json

    {
        "query": {
            "action": "search_subdomains",
            "parameters": {
                "domain": "69"
            }
        },
        "error": {
            "error_name": "bad_request",
            "error_description": "Request is malformed",
            "error_context": {
                "invalid_parameter_value": "69"
            }
        }
    }

.. _empty-result-error:

^^^^^^^^^^^^
Empty Result
^^^^^^^^^^^^

Request was successfully processed but yielded no results. This error is often
sent in conjunction with :http:statuscode:`404` HTTP status code thus making it
similar to :ref:`no-such-endpoint-error`. Do check the response body to
correctly handle these errors.

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`404`
      - :code:`empty_result`
      - :code:`Request produced no results`

Example:

.. sourcecode:: json

    {
        "query": {
            "action": "search_subdomains",
            "parameters": {
                "domain": "abcabcabcabcabcabcabcabcabcabcabcabcabc.io",
                "ipv4.history": false,
                "ipv4.latest": true,
                "ipv4.live": false,
                "ipv4.meta": false,
                "ipv4.oldest": true,
                "ipv6.history": false,
                "ipv6.latest": true,
                "ipv6.live": false,
                "ipv6.meta": false,
                "ipv6.oldest": true
            }
        },
        "error": {
            "error_name": "empty_result",
            "error_description": "Request produced no results"
        }
    }

.. _internal-server-error:

^^^^^^^^^^^^^^^^^^^^^
Internal Server Error
^^^^^^^^^^^^^^^^^^^^^

Internal server error. This is most probably a bug. See :doc:`../about/bugs`
for more information about how to report bugs and security vulnerabilities.

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`500`
      - :code:`internal_server_error`
      - :code:`API server failed to process the request`

Example:

.. sourcecode:: json

    {
        "error": {
            "error_name": "internal_server_error",
            "error_description": "API server failed to process the request"
        }
    }


.. _method-not-allowed:

^^^^^^^^^^^^^^^^^^
Method Not Allowed
^^^^^^^^^^^^^^^^^^

Requested endpoint does not support HTTP method that was used. `Query Object
<response-structure.html#query-object>`_ is not returned when this error
occurs.

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`405`
      - :code:`method_not_allowed`
      - :code:`Request method is not supported by this endpoint`

Example:

.. sourcecode:: json

    {
        "error": {
            "error_name": "method_not_allowed",
            "error_description": "Request method is not supported by this endpoint"
        }
    }

.. _no-such-endpoint-error:

^^^^^^^^^^^^^^^^
No Such Endpoint
^^^^^^^^^^^^^^^^

Requested API endpoint does not exist. `Query Object
<response-structure.html#query-object>`_ is not returned when this error
occurs.

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`404`
      - :code:`no_such_endpoint`
      - :code:`Requested API endpoint does not exist`

Example:

.. sourcecode:: json

    {
        "error": {
            "error_name": "no_such_endpoint",
            "error_description": "Requested API endpoint does not exist"
        }
    }

.. _rate-limit-exceeded-error:

^^^^^^^^^^^^^^^^^^^
Rate Limit Exceeded
^^^^^^^^^^^^^^^^^^^

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`429`
      - :code:`rate_limit_exceeded`
      - :code:`API rate limit was exceeded`

.. todo::

    Propertly document Rate Limit Exceeded error type

^^^^^^^^^^^^^^^^^^
Processing Timeout
^^^^^^^^^^^^^^^^^^

.. note::

    This error indicates that a hard limit for resources utilization was reached
    and no further processing will be made for this request. This is a current
    limitation of the API. Processing timeout will be increasing in the near
    future.

Request took too long to process and was abandoned by the API server. No
results will be returned.

.. list-table::

    * - **HTTP Status Code**
      - **Error Name**
      - **Error Description**

    * - :http:statuscode:`501`
      - :code:`processing_timeout`
      - :code:`Request processing took too long`

.. sourcecode:: json

    {
        "query": {
            "action": "search_subdomains",
            "parameters": {
                "domain": "example.com",
                "ipv4.history": true,
                "ipv4.latest": true,
                "ipv4.live": true,
                "ipv4.meta": true,
                "ipv6.history": true,
                "ipv4.oldest": true,
                "ipv6.latest": true,
                "ipv6.live": true,
                "ipv6.meta": true,
                "ipv6.oldest": true
            }
        },
        "error": {
            "error_name": "processing_timeout",
            "error_description": "Request processing took too long"
        }
    }
