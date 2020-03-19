==========
Data Types
==========
Data types represent all different entities that can be referenced (see
:doc:`references` for details) in the API response object. Each data
type may contain different data fields but they all have the same
:ref:`general-structure`.

.. _general-structure:

-----------------
General Structure
-----------------

.. json:object:: Data Object

    General structure of a data object for all data types.

    :property string type: Type of a data object. Always present.
    :property object data: Object that contains the actual data fields of this
                           object type instance. Always present.

Minimal example:

.. sourcecode:: json

    {
        "type": "subdomain",
        "data": {
            "name": "foo.example.com"
        }
    }

-----
Types
-----

.. _ipv4-data-type:

^^^^^^^^^^^^
IPv4 Address
^^^^^^^^^^^^

IPv4 address. Type field value: :code:`ipv4`.

.. json:object:: IPv4 Data

    Data object of IPv4 data type.

    :property string address:  IPv4 address. Always present.
    :property list reputation: List of reputation feed names in which this IP
                               address was observed throughout its lifespan.

Example:

.. sourcecode:: json

    {
        "type": "ipv4",
        "data": {
            "address": "8.8.8.8",
            "reputation": [
                "firehol-coinbl-hosts",
                "firehol-dshield-top-1000",
                "firehol-firehol-abusers",
                "firehol-firehol-level3",
                "firehol-hphosts-ats",
                "firehol-hphosts-emd",
                "firehol-hphosts-fsa",
                "firehol-hphosts-psh",
                "firehol-packetmail-emerging-ips",
                "firehol-stopforumspam"
            ]
        }
    }

.. _ipv6-data-type:

^^^^^^^^^^^^
IPv6 Address
^^^^^^^^^^^^

IPv6 address. Type field value: :code:`ipv6`.

.. json:object:: IPv6 Data

    Data object of IPv6 data type.

    :property string address: IPv6 address. Always present.

Example:

.. sourcecode:: json

    {
        "type": "ipv6",
        "data": {
            "address": "2001:4860:4860::8888",
            "reputation": [
                "firehol-coinbl-hosts",
                "firehol-dshield-top-1000",
                "firehol-firehol-abusers",
                "firehol-firehol-level3",
                "firehol-hphosts-ats",
                "firehol-hphosts-emd",
                "firehol-hphosts-psh",
                "firehol-packetmail-emerging-ips"
            ]
        }
    }

.. _subdomain-data-type:

^^^^^^^^^
Subdomain
^^^^^^^^^

Internet subdomain. Type field value: :code:`subdomain`.

.. json:object:: Subdomain Data

    Data object of subdomain data type.

    :property string name: Name of a subdomain. Always present.

Example:

.. sourcecode:: json

    {
        "type": "subdomain",
        "data": {
            "name": "foo.example.com"
        }
    }
