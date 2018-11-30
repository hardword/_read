#!/bin/python
# validation!!
# https://validx.readthedocs.io/en/latest/usage.html?highlight=install

from validx import Dict, List, Str, Int

search_params = Dict(
    {
        "query": Str(minlen=3, maxlen=500),    # Search query
        "tags": List(Str(pattern=r"^[\w]+$")), # Optional list of tags
        "limit": Int(min=0, max=100),          # Pagination parameters
        "offset": Int(min=0),
    },
    defaults={
        "limit": 100,
        "offset": 0,
    },
    optional=["tags"],
)

# testing
assert search_params({"query": u"Craft Beer"}) == {
    "query": "Craft Beer",
    "limit": 100,
    "offset": 0,
}

assert search_params({"query": u"Craft Beer", "offset": 100}) == {
    "query": u"Craft Beer",
    "limit": 100,
    "offset": 100,
}
assert search_params({"query": u"Craft Beer", "tags": [u"APA"]}) == {
    "query": u"Craft Beer",
    "tags": [u"APA"],
    "limit": 100,
    "offset": 0,
}
