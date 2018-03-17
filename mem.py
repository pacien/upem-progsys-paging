#!/usr/bin/env python3

# UPEM / Programmation système / Projet : Simulation de gestion de mémoire virtuelle
# Pacien TRAN-GIRARD et Adam NAILI


class Memory:
  def __init__(self, main_size, virt_size):
    self.main = [None] * main_size
    self.virt = [None] * virt_size

  def _mem_to_string(self, mem):
    return ''.join(['%d' % n if n is not None else 'x' for n in mem])

  def dump_main(self):
    return self._mem_to_string(self.main)

  def dump_virt(self):
    return self._mem_to_string(self.virt)

  def has_page(self, page):
    return 0 <= page < len(self.virt)

