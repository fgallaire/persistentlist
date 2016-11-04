# -*- coding: utf-8 -*-
# Copyright © 2016 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# standard libraries imports
import os.path
import shelve

class PersistentList(object):

    def __init__(self, dbpath, maxitems):
        self.dblist = []
        self.maxitems = maxitems
        if not os.path.exists('.'.join([dbpath, 'db'])):
            self.db = shelve.open(dbpath, writeback=True)
            self.db['itemlist'] = []
        else:
            self.db = shelve.open(dbpath, writeback=True) 

    def __str__(self):
        return self.db['itemlist'].__repr__()

    def __repr__(self):
        return str(self.db['itemlist'])

    def __iter__(self):
        for elem in self.db['itemlist']:
            yield elem

    def append(self, item):
        if len(self.db['itemlist']) == self.maxitems:
            del self.db['itemlist'][0]
        self.db['itemlist'].append(item)

    def close(self):
        self.db.close()
        
