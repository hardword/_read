#!/bin/python

"""
- everything in Python is an object, even types such as int and str.
- culprit: a struct called a PyObject in CPython.
- a struct, or structure, in C is like a class with attributes and no methods in OOP lang.
- PyObject
  <= ob_refcnt: reference count (for garbage collection), ob_type: pointer to another(actual object) type

typedef struct _object {
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;
"""

import sys

some_hard_to_guess_var_name = [1,2,3,4,5]
a = sys.getrefcount(some_hard_to_guess_var_name)

print "refcount1: ", a #should be 2?

some_harder_to_guess_var_name = some_hard_to_guess_var_name
b = sys.getrefcount(some_hard_to_guess_var_name)

print "refcount2: ", b #should be a+1

list_of_some_hard_to_guess_var_name = [some_hard_to_guess_var_name, some_hard_to_guess_var_name, some_hard_to_guess_var_name]
c = sys.getrefcount(some_hard_to_guess_var_name)

print "refcount3: ", c #should be b+len(list_of_some_hard_to_guess_var_name)

"""
CPython Memory Allocation
- Arena(used, full, or empty) > Pool(used, full, or empty) > Blocks(untouched, free, allocated)
- The freeblock pointer points to a singly linked list of free blocks of memory
"""

# returns the size in bytes
print "object size in byte : ", sys.getsizeof(some_hard_to_guess_var_name)

# unique id of an object ==> Implementation note: this is the address of the object.
print "object id : ", id(some_hard_to_guess_var_name)
obj = object.__repr__(some_hard_to_guess_var_name)
objAddrH = obj.split()[3][:-1]
print "object : ", obj
print "\t\t\t==> ", objAddrH, " == ", int(objAddrH, 16)
