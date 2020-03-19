==========
Data Types
==========

.. todo::

    Add an introduction to a data types documentation page

-----------------
General Structure
-----------------

.. json:object:: Data Object

    General structure of a data object.

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

.. _domain-data-type:

^^^^^^
Domain
^^^^^^

.. todo::

    Document Domain data type

.. _ipv4-data-type:

^^^^^^^^^^^^
IPv4 Address
^^^^^^^^^^^^

IPv4 address. Type field value: :code:`ipv4`.

.. json:object:: IPv4 Data

    Data object of IPv4 data type.

    :property string address: IPv4 address. Always present.

Example:

.. sourcecode:: json

    {
        "type": "ipv4",
        "data": {
            "address": "8.8.8.8"
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
            "address": "2001:db8:85a3::8a2e:370:7334"
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
