Use persistentlist
==================
How to use the persistentlist library. Start by importing the module::

    >>> from persistentlist import PersistentList

Then initiate a persistentlist object, providing the path to the persistent file and the length of the list::

    >>> cache = PersistentList('cache', 3)

Remember the goal of this object persistentlist is to store persistently N objects (here 3) and the appended n+1 object will remove the first object of the list::

    >>> cache
    []

You can use append()::

    >>> cache.append(1)
    >>> cache
    [1]
    >>> cache.append(2)
    >>> cache
    [1, 2]
    >>> cache.append(3)
    >>> cache
    [1, 2, 3]
    >>> cache.append(4)
    >>> cache
    [2, 3, 4]

And extend()::

    >>> cache.extend([5, 6])
    >>> cache
    [4, 5, 6]

Use your persistent list like a traditional list::

    >>> mylist = cache
    >>> mylist
    [4, 5, 6]

Once you are finished using the persistentlist object, do not forget to close it (requirement of the standard library module shelve underneath)::

    >>> cache.close()

One last important point: the name of your persistent file on the disk will be the path indicated while initializing the object, with the suffixe ".db", e.g if your path is /tmp/cache, the path on your disk will be /tmp/cache.db
