import os

from upath.upath import translate_path, split_path


def test_path_with_drive_letter():
    path_in = r'C:\Python27'
    path_out = 'C:/Python27'
    assert translate_path(path_in) == path_out


def test_path_with_trailing_backslash():
    path_in = r'C:\Python27\\'
    path_out = 'C:/Python27/'
    assert translate_path(path_in) == path_out


def test_path_with_spaces():
    path_in = r'C:\Program Files\Microsoft Visual Studio 10.0\Common7\IDE'
    path_out = r'"C:/Program Files/Microsoft Visual Studio 10.0/Common7/IDE"'
    assert translate_path(path_in) == path_out


def test_path_without_drive_letter():
    path_in = r'\Program Files\Microsoft Visual Studio 10.0\Common7\IDE'
    path_out = r'"/Program Files/Microsoft Visual Studio 10.0/Common7/IDE"'
    assert translate_path(path_in) == path_out


def test_path_with_relative_dirs1():
    path_in = r'C:\Program Files\..\..\Common7\IDE'
    path_out = r'"C:/Program Files/../../Common7/IDE"'
    assert translate_path(path_in) == path_out


def test_path_with_relative_dirs2():
    path_in = r'..\Program Files\..\..\Common7\IDE'
    path_out = r'"../Program Files/../../Common7/IDE"'
    assert translate_path(path_in) == path_out


def test_path_with_relative_dirs3():
    path_in = r'C:\..\Program Files\..\..\Common7\IDE'
    path_out = r'"C:/../Program Files/../../Common7/IDE"'
    assert translate_path(path_in) == path_out


def test_path_split_1():
    path = os.path.splitdrive(
        r'C:\Program Files\Microsoft Visual Studio 10.0\Common7\IDE')[1]
    result = [
        '', 'Program Files', 'Microsoft Visual Studio 10.0', 'Common7', 'IDE']
    assert split_path(path) == result


def test_path_split_2():
    path = os.path.splitdrive(
        r'Program Files\Microsoft Visual Studio 10.0\Common7\IDE')[1]
    result = [
        'Program Files', 'Microsoft Visual Studio 10.0', 'Common7', 'IDE']
    assert split_path(path) == result
