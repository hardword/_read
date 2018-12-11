#!/bin/python
# Dan at RealPython - PyTricks

def contains(haystack, needle):
    for item in haystack:
        if item == needle:
            break
    else:
        raise ValueError('Needle not found')

def better_contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return
    raise ValueError('Needle not found')

"""
if needle not in haystack:
    raise ValueError('Needle not found')
"""

print "# haystack with needle at contains"
print contains([23, 'needle', 0xbadc0ffee], 'needle')

print "# haystack with needle at better_contains"
print better_contains([23, 'needle', 0xbadc0ffee], 'needle')

print "# haystack without needle at contains"
print contains([23, 42, 0xbadc0ffee], 'needle')

print "# haystack without needle at better_contains"
print better_contains([23, 42, 0xbadc0ffee], 'needle')