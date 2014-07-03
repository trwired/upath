A simple tool to translate DOS like paths into paths understood by UNIX tools.
Now you can use path completion functionality that comes with your cmd window
and still make msys/gnutools commands work.

Assuming you have a Python interpreter installed in your system and the path to
the Scripts directory is in your PATH (Python 2.7 installer does that for you if
you check appropriate option):

```
python setup.py install
```

And use it like this:

```
upath C:\Python27
C:/Python27
```

To use the translated path with a command do:

```
upath -c "ls -l" C:\Python27
```

The above is equivalent to:

```
ls -l C:/Python27
```
