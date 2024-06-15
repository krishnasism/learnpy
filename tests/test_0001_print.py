import os


def test_print(capfd):
    os.system("python exercises/0000_intro.py")
    captured = capfd.readouterr()
    assert captured.out == "30\n"
