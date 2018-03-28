#!/usr/bin/env python3

# UPEM / Programmation système / Projet : Simulation de gestion de mémoire virtuelle
# Pacien TRAN-GIRARD et Adam NAILI

from mem import Memory
from fifo import FifoPaginator

paginators = {
  'fifo': FifoPaginator
}


def output(cmd, msg):
  print('> \033[1A' + cmd + '\t' + msg)


def main(main_size, virt_size, paginator):
  mem = Memory(main_size, virt_size)
  pag = paginator(mem)

  while True:
    cmd = input('> ')
    if cmd.isnumeric():
      try:
        pag.load(int(cmd))
        output(cmd, mem.dump_main())
      except IndexError:
        output(cmd, "Error: invalid page.")
    elif cmd == 'p':
      output(cmd, mem.dump_main() + '\t' + mem.dump_virt())
    elif cmd == 'x':
      break
    else:
      output(cmd, 'Error: invalid command.')


if __name__ == '__main__':
  from argparse import ArgumentParser
  argparser = ArgumentParser()
  argparser.add_argument('-s', '--mem_size', type = int, required = True)
  argparser.add_argument('-v', '--virtual_size', type = int, required = True)
  argparser.add_argument('-a', '--algorithm', required = True, choices = paginators.keys())

  args = argparser.parse_args()
  assert args.mem_size < args.virtual_size
  main(args.mem_size, args.virtual_size, paginators[args.algorithm])

