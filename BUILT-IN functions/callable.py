#callable()

# The callable() function in Python is used to check if an object appears to be callable,
# such as a function, method, class, or an instance of a class with a __call__ method.
# It returns True if the object is callable and False otherwise

x = 5
print(callable(x))

def test_function():
    print("Test")

y = test_function
print(callable(y))

class MyClass:
  def __call__(self):
    print("Instance is being called")

obj = MyClass()
print(callable(obj))