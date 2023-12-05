def outer1(func):
    def outer1inner(name):
        print("****___________________________****")
        func(name)
        print("****___________________________****")
    return outer1inner
def outer(func):
    def inner(name):
        print("****___________________________****")
        func(name)
        print("****___________________________****")
    return inner
@outer1
@outer
def greetings(name):
    print("how are u",name)
greetings("lakshmi")
