=========================
Response Object Structure
=========================
All responses returned by ZeroGuard Recon API have a unified structure. This
page describes how a non-error responses are structured. For a structure of
error responses refer to :doc:`errors` section.

---------
Structure
---------

.. json:object:: Non-Error Response

    General structure of a non-error API response.

    :property object _meta: Contextual meta information about the response.
                            Optional.

    :property object query: Contextual information about the query that was
                            performed. Essentially, this object just mirrors
                            request parameters that were specified (after
                            a disambiguation and resolution process). Object
                            structure is defined individually for each API
                            endpoint. Required.

    :property object data:  Results of a performed query (request). Required.

.. json:object:: Data Object

    General structure of a non-error API response data.

    :property list records:   List of records returned by the back-end. Object
                              structure is defined individually for each API
                              response. Required.

    :property map references: Mapping of `_ref` (reference number) to a
                              referenced object. See :doc:`references` for
                              details. Optional and included only if records
                              reference any related objects.

.. todo::

    Describe a structure of `_meta` object

--------
Examples
--------

.. sourcecode:: json

    {
        "_meta": {},
        "query": {
            "domain": "example.com"
        },
        "data": {
            "records": [
            ],
            "references": {
            }
        }
    }

.. todo::

    More decent examples (or at least one example that is full)
