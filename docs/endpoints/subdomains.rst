=================
Search Subdomains
=================

------
Schema
------

.. http:post:: /v1/subdomains/(str:domain)

    Search for all seen subdomains of `domain`.

    :param str domain: Domain which subdomains to return.

    :jsonparam list fields: List of fields to return. See
                            :ref:`fields` for a list of acceptable
                            values. Default is to return all existing fields.

    :statuscode 200: Subdomains search was successfull.
    :statuscode 404: Subdomains search returned no results.
    :statuscode 429: API rate limit was exceeded. See
                     :doc:`../concepts/rate-limits` for more information on
                     how to gracefully handle API quota.

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

.. _fields:

------
Fields
------
