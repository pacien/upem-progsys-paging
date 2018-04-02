#!/usr/bin/env python3

from mem import Memory
from pageexception import *

class LruPaginator:
  def __init__(self, mem):
    self.mem = mem
    self._global_counter = 1
    self._check_table = [0 for _ in range(len(mem.main)+len(mem.virt))]
    self._main_cursor = 0
  
  def _update_check_table(self, page):
    """
    >>> lru = LruPaginator(Memory(3,5))
    >>> page = 3
    >>> lru._update_check_table(page)
    >>> print(lru._check_table[page])
    1
    >>> print(lru._global_counter)
    2
    """
    self._check_table[page] = self._global_counter
    self._global_counter += 1

  def _check_where_to_replace(self):
    """
    >>> lru = LruPaginator(Memory(3,5))
    >>> lru._check_where_to_replace()
    >>> print(lru._main_cursor)
    0
    >>> lru.mem.main = [3,4,2]
    >>> lru._check_table = [1, 3, 6, 4, 5, 0, 0, 0]
    >>> lru._check_where_to_replace()
    >>> print(lru._main_cursor)
    0
    """
    for page in self.mem.main:
      if page is None:
        self._main_cursor = self.mem.main.index(page)
        return
    min = self._check_table[self.mem.main[0]]
    self._main_cursor = 0
    for page in self.mem.main:
      if min > self._check_table[page]:
        min = self._check_table[page]
        self._main_cursor = self.mem.main.index(page)

  def _put_main(self, page):
    self._check_where_to_replace()
    print("Cursor:")
    print(self._main_cursor)
    print("")
    overwritten = self.mem.main[self._main_cursor]
    self.mem.main[self._main_cursor] = page
    self._update_check_table(page)
    return overwritten  
        
  def load(self, page):
    if not self.mem.page_in_range(page): raise PageException
    if page in self.mem.main: 
      self._update_check_table(page)
      return
    if page in self.mem.virt: self.mem.remove_virt(page)
    overwritten = self._put_main(page)
    if overwritten is not None: self.mem.put_virt(overwritten)


if __name__ == "__main__":
  import doctest
  doctest.testmod()
