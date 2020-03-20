==========
Data Types
==========
Data types represent all different entities that can be referenced (see
:doc:`references` for details) in the API response object. Each data
type defines a unique value for a :code:`type` field as well as any other
type-specific fields.

.. _ipv4-data-type:

------------
IPv4 Address
------------

.. json:object:: IPv4 Address

    IPv4 address.

    :property string type:        Type definition. Always present and has a
                                  value of :code:`ipv4`.

    :property string address:     IPv4 address. Always present.

    :property int closest_prefix: A `reference <references.html>`_ to the
                                  smallest :ref:`network-prefix-data-type`
                                  which contains this IP address. Always
                                  present.

    :property list prefixes:      A list of `references <references.html>`_
                                  to multiple :ref:`network-prefix-data-type`
                                  instances which together represent a full
                                  prefix chain for this IP.

    :property list reputation:    List of :json:object:`IP Reputation Entry`
                                  instances containing information from
                                  reputation feeds in which this IP address
                                  was observed throughout its lifespan.

.. json:object:: IP Reputation Entry

    IP reputation feed entry. Instances of this type are always located in
    :code:`reputation` list of :json:object:`IPv4 Address` or
    :json:object:`IPv6 Address` objects as they are generated dynamically for a
    specific IP returned in the API response.

    :property string name:  Name of IP reputation feed to which this entry
                            belongs to. Always pressent.
    :property bool current: Flag which determines whether this reputation feed
                            entry is current (exists in a source reputation
                            feed when the response is returned). Always
                            present.

    :property int first_seen: Unix timestamp of when this entry was first
                              observed. Always present.

    :property int last_seen: Unix timestamp of when this entry was last
                             observed. Always present.

Example of :json:object:`IPv4 Address` data type instance (truncated for
clarity):

.. sourcecode:: json

    {
        "type": "ipv4",
        "address": "8.8.8.8",
        "reputation": [
            {
                "name": "firehol-coinbl-hosts",
                "current": false,
                "first_seen": 1584712048,
                "last_seen": 1584720037

            },
            {
                "name": "firehol-dshield-top-1000",
                "current": true,
                "first_seen": 1584714021,
                "last_seen": 1584720037
            }
        ]
    }

.. _ipv6-data-type:

------------
IPv6 Address
------------

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

.. _network-prefix-data-type:

--------------
Network Prefix
--------------

.. json:object:: Network Prefix

.. _subdomain-data-type:

---------
Subdomain
---------

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
