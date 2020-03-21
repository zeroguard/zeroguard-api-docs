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

    :property obj closest_prefix: A reference to the smallest network prefix
                                  which contains this IP address. Always
                                  present.

    :property list prefixes:      A list of references to multiple
                                  network prefixes which together represent a
                                  full prefix chain for this IP (from the
                                  smallest to 0.0.0.0/0). Always present.

    :property list reputation:    List of IP reputation entries containing
                                  information from reputation feeds in which
                                  this IP address was observed throughout its
                                  lifespan. Always present.

    :proptype closest_prefix: :json:object:`Prefix Reference`
    :proptype prefixes:       *list of* :json:object:`Prefix Reference`
    :proptype reputation:     *list of* :json:object:`IP Reputation Entry`

.. json:object:: Prefix Reference

    A `reference <references.html>`_ to :ref:`network-prefix-data-type`
    which contains an IP address.

    :property int _ref: Reference number. Always present.

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

.. todo::

    Replace IPv4 address data type example with an actual output from the API.
    Currently it is a stub.

Example of :json:object:`IPv4 Address` data type instance (truncated for
clarity):

.. sourcecode:: json

    {
        "type": "ipv4",
        "address": "8.8.8.8",
        "closest_prefix": {"_ref": 1},
        "prefixes": [
            {"_ref": 1},
            {"_ref": 3},
            {"_ref": 4}
        ],
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

IPv6 address. Structure is near identical to :json:object:`IPv4 Address` thus a
lot of nested object definitions are re-used.

.. json:object:: IPv6 Address

    IPv6 address.

    :property string type:        Type definition. Always present and has a
                                  value of :code:`ipv6`.

    :property string address:     IPv6 address. Always present.

    :property obj closest_prefix: A reference to the smallest network prefix
                                  which contains this IP address. Always
                                  present.

    :property list prefixes:      A list of references to multiple
                                  network prefixes which together represent a
                                  full prefix chain for this IP (from the
                                  smallest to 0.0.0.0/0). Always present.

    :property list reputation:    List of IP reputation entries containing
                                  information from reputation feeds in which
                                  this IP address was observed throughout its
                                  lifespan. Always present.

    :proptype closest_prefix: :json:object:`Prefix Reference`
    :proptype prefixes:       *list of* :json:object:`Prefix Reference`
    :proptype reputation:     *list of* :json:object:`IP Reputation Entry`

.. todo::

    Replace IPv6 address data type example with an actual output from the API.
    Currently it is a stub.

Example (truncated for clarity):

.. sourcecode:: json

    {
        "type": "ipv6",
        "address": "2001:4860:4860::8888",
        "closest_prefix": {"_ref": 3},
        "prefixes": [
            {"_ref": 3},
            {"_ref": 4},
            {"_ref": 12}
        ],
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

.. _network-prefix-data-type:

--------------
Network Prefix
--------------

.. todo::

    Replace Network Prefix data type stub with an actual definition

.. json:object:: Network Prefix

    Network prefix.

    :property string type:   Type definition. Always present and has a value of
                             :code:`netpref`.

    :property string prefix: Actual value of a network prefix.

Example:

.. sourcecode:: json

    {
        "type": "netpref",
        "prefix": "0.0.0.0/0"
    }

.. _subdomain-data-type:

---------
Subdomain
---------

.. json:object:: Subdomain

    Internet subdomain.

    :property string type: Type definition. Always present and has a value of
                           :code:`subdomain`.
    :property string name: Name of a subdomain. Always present.

Example:

.. sourcecode:: json

    {
        "type": "subdomain",
        "name": "foo.example.com"
    }
