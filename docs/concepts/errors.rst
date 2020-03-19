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
                            structure. Always present.

    :property object error: Error object that was returned. Always present.

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
An example of a simple error response:

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
:ref:`no-such-endpoint-error` are returned with :http:statuscode:`404`). Hence
it is advised to always check the response body to determine which error has
occured.

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

.. _no-such-endpoint-error:

^^^^^^^^^^^^^^^^
No Such Endpoint
^^^^^^^^^^^^^^^^
