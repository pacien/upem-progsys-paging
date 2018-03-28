#!/usr/bin/env python3

# UPEM / Programmation système / Projet : Simulation de gestion de mémoire virtuelle
# Pacien TRAN-GIRARD et Adam NAILI

from mem import Memory


class FifoPaginator:
  def __init__(self, mem):
    self.mem = mem
    self._main_cursor = 0

  def _put_main(self, page):
    overwritten = self.mem.main[self._main_cursor]
    self.mem.main[self._main_cursor] = page
    self._main_cursor = (self._main_cursor + 1) % len(self.mem.main)
    return overwritten

  def load(self, page):
    if not self.mem.page_in_range(page): raise IndexError
    if page in self.mem.main: return
    if page in self.mem.virt: self.mem.remove_virt(page)
    overwritten = self._put_main(page)
    if overwritten is not None: self.mem.put_virt(overwritten)

