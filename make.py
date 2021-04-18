#!/usr/bin/python
import argparse, os

p = argparse.ArgumentParser(description='evalnn build script')
p.add_argument('-c', '--compiler', help='Compiler', choices=['gcc', 'clang', 'musl-gcc',
    'musl-clang'], default='clang')
p.add_argument('-o', '--output', help='Output file', default='./evalnn')
p.add_argument('-d', '--debug', action='store_true', help='Debug compile')
p.add_argument('-s', '--static', action='store_true', help='Static compile')
args = p.parse_args()

# Determine flags for: compilation, warning, and linking
cflags = '-I./src -I./nn -std=c99 {}'.format('-DNDEBUG -Ofast -s' if not args.debug else '-g -O1')

if args.compiler in ['clang', 'musl-clang']:
    wflags = '-Weverything -Wno-vla'
else:  # assume gcc
    wflags = '-Wfatal-errors -Wall -Wextra'

lflags ='-lm'
if args.static: lflags += ' -static'

def run(cmd):
    print('% ' + cmd)
    return os.system(cmd)

sources = 'nn/nn.c src/main.c'
run('{} {} {} {} -o {} {}'.format(args.compiler, cflags, wflags, sources, args.output, lflags))
