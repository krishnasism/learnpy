import os


def test_intro(capfd):
    os.system("python exercises/0000_intro.py")
    captured = capfd.readouterr()
    assert captured.out == "Hello World!\n"
