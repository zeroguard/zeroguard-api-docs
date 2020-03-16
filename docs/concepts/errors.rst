======
Errors
======
All error responses sent by the API have a unified structure. Contextual data
that is specific for a given request or endpoint is always located under
:code:`error.error_context` key.

See :ref:`error-types` for a list of all defined errors.

---------
Structure
---------

.. json:object:: Error Response

    General structure of an error response.

    :property object error: Error object that was returned.

.. json:object:: Error Object

    Error object structure.

    :property string error_name:    Name of an error that occured. Required.

    :property string error_desc:    Description of an error that occured. It is
                                    static and is defined by the error itself,
                                    not a request that was sent. Required.

    :property object error_context: A nested object with a contextual
                                    information about the error. Optional.
                                    Object structure is defined individually
                                    for each API endpoint.

Example:

.. sourcecode:: json

    {
        "error": {
            "error_name": "invalid_parameter",
            "error_description": "Invalid request parameter was specified",
            "error_context": {
                "received_parameter_name": "foo",
                "excpected_parameter_names": [
                    "bar",
                    "baz"
                ]
            }
        }
    }

.. _error-types:

-----------
Error Types
-----------
Under construction.
