import os


def test_import(capfd):
    os.system("python exercises/0002_import.py")
    captured = capfd.readouterr()
    assert captured.out == "4.0\n"
