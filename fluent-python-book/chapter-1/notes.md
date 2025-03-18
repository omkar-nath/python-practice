# Python data model

In the french deck class, there are two advantages of using special methods to leverage Python data model

1. User of class don't have to memorize arbitrary method for standard operations
2. Its easier to benefit from the rich Python standard library and avoid reinventing the wheel, like the
   random.choice function
3. In python when we implement the **getitem** method, we are leveraging the fact that lists already support slicing

4. When we use slice on FrechDeck instance (for example deck[2:5]), Python creates a slice object
   and passes it to the **getitem** method as the position parameter.

5. Just by implementing the **getitem** special method, our deck is also iterable

## How does slicing work

`sequence[start:stop:step]` Items start through stop-1
`sequence[start:]` Items start through the rest of the array
`sequence[:stop]` Items from the beginning through stop-1
`sequence[:]` A copy of the whole array

Some examples,

- a[::-1] All items in the array, reversed
- a[1::-1] The first two items, reversed
- a[:-3:-1] The last two items, reversed
- a[-3::-1] Everything except the last two items,reversed

## How special methods are used

1. The special methods are called by interpreter and not by us.
2. We don't write ```my_object.__len__()```. We write len(my_object) and if my_object is an instance of a use defined class, then python
   calls the ```__len__``` instance methd you implemented.

3. More often than not, the special method call is implicit. For example, the statement for i in x:
   actually causes the invocation of iter(x), which in turn may call ```x.__iter__()``` if that is available
