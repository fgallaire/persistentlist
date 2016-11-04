# PersistentList

Persistentlist is a simple persistent list carrying n objects, the last objects being appended
at the end of the list.

When n objects are in the list, before appending the n+1 object at then end of the list, the
first object is removed from the list.

### Quick Install

* Install persistentlist from PyPI

        # pip3 install persistentlist

* Install persistentlist from sources

        # tar zxvf persistentlist-0.3.tar.gz
        # cd persistentlist
        # python3.4 setup.py install

### How to use persistentlist

        >>> from persistentlist import PersistentList
        >>> cache = PersistentList('cache', 3)
        >>> cache
        []
        >>> cache.append(1)
        [1]
        >>> cache.append(2)
        [1, 2]
        >>> cache.append(3)
        [1, 2, 3]
        >>> cache.append(4)
        [2, 3, 4]
        >>> mylist = cache
        >>> mylist
        [2, 3, 4]
        >>> cache.close()

### Authors

Carl Chenet <chaica@ohmytux.com>

### License

This software comes under the terms of the GPLv3+. See the LICENSE file for the complete text of the license.
