#!/usr/bin/env python3

# UPEM / Programmation système / Projet : Simulation de gestion de mémoire virtuelle
# Pacien TRAN-GIRARD et Adam NAILI


class Memory:
  def __init__(self, main_size, virt_size):
    self.main = [None] * main_size
    self.virt = [None] * virt_size
    self._virt_cursor = 0

  def _mem_to_string(self, mem):
    return ''.join(['%d' % n if n is not None else 'x' for n in mem])

  def dump_main(self):
    return self._mem_to_string(self.main)

  def dump_virt(self):
    return self._mem_to_string(self.virt)

  def page_in_range(self, page):
    return 0 <= page < len(self.main + self.virt)

  def put_virt(self, page):
    self.virt[self._virt_cursor] = page
    self._virt_cursor += 1

  def remove_virt(self, page):
    for i in range(len(self.virt)):
      if self.virt[i] == page:
        self._virt_cursor -= 1
        self.virt[i] = self.virt[self._virt_cursor]
        self.virt[self._virt_cursor] = None
        break

