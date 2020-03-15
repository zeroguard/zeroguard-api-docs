======
Errors
======
All error responses sent by the API have a unified structure. Contextual data
that is specific for a given request or endpoint is always located under
:code:`error_context` key.

See :ref:`error-types` for a list of all defined errors.

---------
Structure
---------

.. json:object:: Error Response

    General structure of an error response.

    :property string error_name:  Name of an error that occured. Required.
    :property string error_desc:  Description of an error that occured. It is
                                  static and is defined by the error itself,
                                  not a request that was sent. Required.
    :property obj error_context:  A nested object with a contextual information
                                  about the error. Optional. Object structure
                                  is defined individually for each API endpoint.

.. _error-types:

-----------
Error Types
-----------
Under construction.
