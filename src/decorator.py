# The decorator pattern supposedly allows you to "Add additional
# responsibilities to an object dynamically". The Python code below
# shows what I understand this buzz-phrase to mean. It turns out that
# in C++ this design pattern doesn't allow you to do anything nearly
# as dynamic as that ... as discussed in the source of the C++
# implementation of the pattern.

class the_class:
    pass

instance = the_class()
instance.new_datum = "This is new_datum"

def instance_method(self):
    print "The new_datum attribute of this object is:", self.new_datum

import new
instance.new_method = new.instancemethod(instance_method, instance, the_class)

print instance.new_datum
instance.new_method()
