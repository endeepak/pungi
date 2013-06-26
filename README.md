Pungi [![Build Status](https://travis-ci.org/endeepak/pungi.png)](https://travis-ci.org/endeepak/pungi)
=====

Simple and powerful python mocking framework with extensible assertion matchers (Inspired by [jasmine](https://github.com/pivotal/jasmine/wiki/Spies) BDD framework)

[define:pungi](http://www.google.com/search?q=define:pungi)

This documentation is for the latest code on this branch. For earlier versions, please refer to corresponding [tags](https://github.com/endeepak/pungi/tags).

Install
=======

        pip install pungi


Intention of this library
=========================

* The library should have simple interface and easily extensible.
* Mocking a method or creating mock/stub object should simply be one line code.
* The tests should not contain any mock replay and verify steps.
* The expectations should be asserted after the action is performed.

Mocking with spies
==================

This mocking library is based on AAA(Arrange Act Assert) pattern. It is built to be simple and easy to use without having to know about how the internals work.

        from pungi import spyOn, createSpy, expect, any

Mocking a class/instance method
-------------------------------

        spyOn(x, 'method') #Arrange

        x.method() #Act

        expect(x.method).toHaveBeenCalled() #Assert

The toHaveBeenCalled matcher can take optional argument *times* to indicate number times method should have been called

        expect(x.method).toHaveBeenCalled(times = 2)

Asserting arguments passed to method call

        expect(x.method).toHaveBeenCalledWith(foo, bar=1)
        expect(x.method).toHaveBeenCalledWith(foo, bar=any(int))

If you do not want to use the above syntax, you can do the same as:

        assertTrue(x.method.wasCalled(times=2)) # The failure message will not be as pretty as the *expect* syntax.
        assertTrue(x.method.wasCalledWith(foo, bar=1))

All the expect matchers will have a corresponding negative assertion matcher.

        expect(x.method).notToHaveBeenCalled()
        expect(x.method).notToHaveBeenCalledWith(foo, bar=1)
        expect(x.method).notToHaveBeenCalledWith(foo, bar=any(int))

The spy can be configured in several ways

        spyOn(x, 'method').andReturn(foo) # x.method() returns foo

        spyOn(x, 'method').andRaise(SomeException, "Message Args") # raise this exception on calling x.method()

        spyOn(x, 'method').andCallThrough() # Call the original method, but record the call which can be used for assertion

        spyOn(x, 'method').andCallFake(some_function) # Call the fake method and record the call

Same can be done with alternate syntax

        spyOn(x, 'method', returnValue=foo)
        spyOn(x, 'method', raiseException=SomeException)
        spyOn(x, 'method', callThrough=True)
        spyOn(x, 'method', callFake=some_func)

The spied method contains useful methods

        x.method.callCount # Number of times x.method() was called

        x.method.mostRecentCall
        x.method.mostRecentCall.received(*args, **kwargs) # True or False
        x.method.mostRecentCall.args # Positional arguments(*args) passed to the method
        x.method.mostRecentCall.kwargs # Named arguments(**kwargs) passed to the method

        x.method.argsForCall(index) # args for nth call
        x.method.kwargsForCall(index) # kwargs for nth call

Mocking a class method is same as above:

      spyOn(FooClass, 'some_class_method')

Cleaning up spies
-----------------

The spies can be cleared in few ways:

* Decorating the test case

        @pungi.dec.testcase
        class ClassDecoratorTest(unittest.TestCase): #Spies are cleared after every test(methods with 'test' in name)

* Decorating individual tests

        @pungi.dec.test
        def test_method(self):

* Add a teardown method which calls *pungi.stopSpying()*

* Use spy inside a *with* block

        with spyOn(x, 'method', returnValue=foo):
              x.method() # returns foo

        x.method() # returns actual value

Creating mock/stub objects
--------------------------

The createSpy method creates a mock/stub object with an optional name, this object records all the method calls.

        x = createSpy("greeter")

        x.say_hello(to='world')

        expect(x.say_hello).wasCalledWith(to='world')

The assertion syntax remains the same. Cleaning up spy objects is same as above. The individual methods on spy object can be setup using *spyOn* method shown above. The alternate syntax for setting up multiple methods with return values is:

        x = createSpy("person", age=20, balance=20000)

or you can configure individual methods

       x.age.returnValue = 20
       x.foo.callFake = fake_method
       x.bar.raiseException = SomeException

Chaining methods and spies
--------------------------

The spied methods return *spy objects* by default. Hence you need to define a spy only once in the complete method chain.

      spyOn(x, 'method')

      x.method().another_method().foo()

      x.method.callCount # 1
      x.method().another_method.callCount # 1
      x.method().another_method().foo.callCount # 1

The behavior is same for spies created using *createSpy* method.

      greeter = createSpy('greeter')

      greeter.say().hello().to().world()


Asserting the order in which methods are called
-----------------------------------------------

The method call order is tracked for every test. This order can be accessed as

      x.method.callNumber # Number indicating global order in which x.method was called

It can asserted be as

      expect(obj.hi).toHaveBeenCalledBefore(obj.hello)

      or

      assertTrue(obj.hi.wasCalledBefore(obj.hello))


Using expect matchers
=====================

There are several inbuilt assertion matchers apart from the spy expectation matchers shown above.

        expect(1 + 1).toBe(2)
        expect(1 + 1).toEqual(2)

        expect(x).toBeNone()
        expect(x).toBeTruthy()
        expect(x).toBeFalsy()

        expect("abcd").toMatch(".*b.*")

        expect("abcd").toContain("b")
        expect([1, 2, 3]).toContain(2)

        expect(2).toBeGreaterThan(1)
        expect(1).toBeLessThan(2)

        expect(raise_ex).toRaise(SomeException)
        expect(raise_ex).toRaise(SomeException, "Message")
        expect(raise_ex).toRaise(SomeException("Message"))        

All the above matchers have corresponding negative('notTo') matchers.

        expect(foo).notToBe(bar)

Adding custom matchers
----------------------

The matchers are easily extensible to allow domain specific custom matchers to improve the readability of test. The custom matcher has to be a class which inherits from *pungi.matchers.Base* and implement *matches* method and optionally message method.

        class ToHaveAttr(pungi.matchers.Base):
            def matches(self, expectedAttrName):
                return hasattr(self.actual, expectedAttrName)

Add the matchers as

        pungi.matchers.add(ToHaveAttr, SomeMoreMatchers, ..)

The matcher is used as

        expect(foo).toHaveAttr('bar')
        expect(foo).notToHaveAttr('qux')

More examples on defining a matcher can be found [here](https://github.com/endeepak/pungi/blob/master/pungi/matchers.py)


Contributing
============

* Issues and feature requests can be added [here](https://github.com/endeepak/pungi/issues/new)

* If an issue can reproduced in the form of a test, fork the project and raise a [pull request](https://github.com/endeepak/pungi/pull/new/master)

Support
=======
The tests pass with python 2.6 and 2.7. Please check the [build matrix](https://travis-ci.org/endeepak/pungi) for more details.

Miscellaneous
=============
This library has been tested unittest framework. It may or may not work with other testing frameworks. If you notice any failures, please report the issue [here](https://github.com/endeepak/pungi/issues/new).
