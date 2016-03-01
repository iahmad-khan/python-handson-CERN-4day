class original_class:

    def hello(self):
        print "This is original_class going about its business"

class new_class:

    def hello(self):
        print "This is new_class going about its business"


instance = original_class()
instance.hello()

instance.__class__ = new_class
instance.hello()

