#!/usr/bin/env python3

# UPEM / System programming / Project: Memory paging simulator
# Pacien TRAN-GIRARD, Adam NAILI

from mem import Memory
from pageexception import *


class SecondChancePaginator:
  def __init__(self, mem):
    self.mem = mem
    self._check_table = [0 for _ in range(len(mem.main)+len(mem.virt))]
    self._main_cursor = 0

  def _put_main(self, page):
    overwritten = self.mem.main[self._main_cursor]
    while(overwritten is not None and self._check_table[overwritten] == 1):
      self._main_cursor=(self._main_cursor + 1) % len(self.mem.main)
      self._check_table[overwritten] = 0
      overwritten = self.mem.main[self._main_cursor]
    self.mem.main[self._main_cursor] = page
    self._main_cursor = (self._main_cursor + 1) % len(self.mem.main)
    return overwritten

  def load(self, page):
    if not self.mem.page_in_range(page): raise PageException
    if page in self.mem.main:
      self._check_table[page] = 1
      return
    if page in self.mem.virt: self.mem.remove_virt(page)
    overwritten = self._put_main(page)
    if overwritten is not None: self.mem.put_virt(overwritten)
