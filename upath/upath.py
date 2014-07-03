#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os


def split_path(path):
    # please note that this function expects a path with the drive letter
    # stripped
    chunks = []
    while True:
        head, tail = os.path.split(path)
        if len(tail):
            chunks.append(tail)
        else:
            chunks.append('')
        path = head
        if head == '\\':
            head = ''
            chunks.append(head)
        if not len(head):
            break
    chunks.reverse()
    return chunks


def translate_path(path):
    drive, tail = os.path.splitdrive(path)
    chunks = split_path(tail)
    if len(drive):
        if len(chunks) and chunks[0] == '':
            chunks.pop(0)
        chunks.insert(0, drive)
    path = '/'.join(chunks)
    return '"{0}"'.format(path) if ' ' in path else path


@click.command()
@click.option('-c', '--command', 'command',
              help='Executes provided command appending provided path(s).')
@click.argument('paths', default=[], nargs=-1)
def cli(command, paths):
    paths = ' '.join([translate_path(path) for path in paths])
    if command is not None:
        os.system(' '.join([command, paths]))
    elif len(paths):
        click.echo(paths, nl=False)

if __name__ == '__main__':
    cli()
