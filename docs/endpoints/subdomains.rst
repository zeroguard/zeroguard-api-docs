=================
Search Subdomains
=================
This endpoint allows to search for subdomains of a given domain. Search results
will not only include subdomains but also all related to them objects (i.e.
`IP addresses <https://en.wikipedia.org/wiki/IP_address>`_,
`ASNs <https://en.wikipedia.org/wiki/Autonomous_system_(Internet)>`_,
`RIRs <https://en.wikipedia.org/wiki/Regional_Internet_registry>`_).

.. include:: _shared/concepts-note.rst

------
Schema
------

.. http:post:: /v1/subdomains/(str:domain)

    Search for all seen subdomains and related objects for `domain`.

    All JSON parameters are prefixed with **<ip_version>** which determines
    a version of IP addresses on which a given JSON parameter acts on. This
    can be one of the following: **ipv4**, **ipv6**, **ip** (both versions).
    More specific version always prevails meaning that below parameters

    .. sourcecode:: json

        {
            "ipv4.history": true,
            "ip.history": false
        }

    are resolved as

    .. sourcecode:: json

        {
            "ipv4.history": true,
            "ipv6.history": false
        }


    :param str domain: Domain which subdomains to return.

    :jsonparam bool <ip_version>.history: Return a list of IP addresses to
                                          which a found subdomain pointed in
                                          the past. Default is *false*.

    :jsonparam bool <ip_version>.latest:  Return the latest found IP address
                                          for each found subdomain. Default is
                                          *true*.

    :jsonparam bool <ip_version>.oldest:  Return the oldest found IP address
                                          for each found subdomain. Default is
                                          *false*.

    :jsonparam bool <ip_version>.live:    Perform a live DNS query and return
                                          its results
    :jsonparam bool <ip_version>.meta: 

    :statuscode 200: Subdomains search was successfull.
    :statuscode 204: Subdomains search was performed successfully but yielded
                     no results.
    :statuscode 400: Bad request. See :doc:`../concepts/errors` for a general
                     structure of an error response and :ref:`error-context`
                     for details on how error context is structured for this
                     endpoint.
    :statuscode 429: API rate limit was exceeded. See
                     :doc:`../concepts/rate-limits` for more information on
                     how to gracefully handle API quota.
    :statuscode 500: Internal server error. This is most probably a bug. See
                     :doc:`../about/bugs` for more information about how to
                     report bugs and security vulnerabilities.

**Minimal Example**:

.. http:example:: curl wget python-requests

    POST /v1/subdomains/google.com HTTP/1.1
    Host: api.zeroguard.com
    Accept: application/json


    HTTP/1.1 200 OK
    Content-Type: application/json

    {"stab": "StuB"}

**Complex Example**:

.. http:example:: curl wget python-requests

    POST /v1/subdomains/complex?fields=foo,bar,baz HTTP/1.1
    Host: api.zeroguard.com
    Accept: application/json

.. _error-context:

-------------
Error Context
-------------
