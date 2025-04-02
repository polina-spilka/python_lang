# classmethod()

class C:
    @classmethod
    def f(cls, arg1, arg2): ...

# A class method can be called either on the class (such as C.f())
# or on an instance (such as C().f()).
# The instance is ignored except for its class.