=================
Object References
=================

.. todo::

    Object references explanation sucks. Make it better.

Due to a highly nested and interconnected nature of the data provided by the
API, there is a need to avoid data duplication and deep nesting in a response
object structure. API utilizes object references to achieve that.

It is said that JSON object references another object if and only if it
contains :code:`_ref` field.

The easiest way to understand how references work is to explain how they are
generated:

#. Retrieve all matching data for a given request from a storage cluster
#. Assign a unique `natural number
   <https://en.wikipedia.org/wiki/Natural_number>`_ as an ID for each data
   object in the results
#. Replace all references inside data objects with a newly generated reference
   numbers that are specific only to this response object.

The result is a flat response object structure which allows each data object to
reference multiple other data objects without any data duplication.

.. note::

    Reference objects never contain values that are specific to the request and
    its parameters. Each referenced data object contains data that is
    independent from the request thus the same data object may be encountered
    across several responses with a different reference ID but with the same
    data.

Example:

.. sourcecode:: json

    {
        "query": {
            "domain": "zeroguard.com"
        },
        "data": {
            "records": [
                {
                    "_ref": 1,
                    "ipv4": [
                        {
                            "_ref": 2,
                            "latest": true,
                            "oldest": false,
                            "live": false,
                            "seen_at": [
                                1584660099,
                                1584650121
                            ]
                        }
                    ]
                }
            ],
            "references": {
                "1": {
                    "type": "subdomain",
                    "data": {
                        "name": "www.zeroguard.com"
                    }
                },
                "2": {
                    "type": "ipv4",
                    "data": {
                        "address": "157.7.107.64",
                        "reputation": []
                    }
                }
            }
        }
    }
