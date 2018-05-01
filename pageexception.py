#!/usr/bin/env python3

# UPEM / System programming / Project: Memory paging simulator
# Pacien TRAN-GIRARD, Adam NAILI


class PageException(Exception):
  def __init__(self):
    super().__init__()
