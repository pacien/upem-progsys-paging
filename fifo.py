#!/usr/bin/env python3

# UPEM / Programmation système / Projet : Simulation de gestion de mémoire virtuelle
# Pacien TRAN-GIRARD et Adam NAILI

from mem import Memory


class FifoPaginator:
  def __init__(self, mem):
    self.mem = mem
    self._main_cursor = 0
    self._virt_cursor = 0

  def _put_main(self, page):
    overwritten = self.mem.main[self._main_cursor]
    self.mem.main[self._main_cursor] = page
    self._main_cursor = (self._main_cursor + 1) % len(self.mem.main)
    return overwritten

  def _put_virt(self, page):
    self.mem.virt[self._virt_cursor] = page
    self._virt_cursor += 1

  def load(self, page):
    if not self.mem.has_page(page): raise IndexError
    if page in self.mem.main: return
    overwritten = self._put_main(page)
    if overwritten not in self.mem.virt: self._put_virt(overwritten)

