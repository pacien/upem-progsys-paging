#!/usr/bin/env python3


from random import randint
from mem import Memory
from pageexception import PageException

# UPEM / System programming / Project: Memory paging simulator
# Pacien TRAN-GIRARD, Adam NAILI


class RandomPaginator:
  def __init__(self, mem):
    self.mem = mem
    self._main_occupancy = 0

  def _random_page(self):
    if self._main_occupancy < len(self.mem.main):
      return self._main_occupancy
    else:
      return randint(0, len(self.mem.main) - 1)

  def _put_main(self, page):
    index = self._random_page()
    overwritten = self.mem.main[index]
    self.mem.main[index] = page
    self._main_occupancy += 1
    return overwritten

  def load(self, page):
    if not self.mem.page_in_range(page): raise PageException
    if page in self.mem.main: return
    if page in self.mem.virt: self.mem.remove_virt(page)
    overwritten = self._put_main(page)
    if overwritten is not None: self.mem.put_virt(overwritten)
