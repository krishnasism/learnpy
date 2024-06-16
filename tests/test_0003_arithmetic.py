import os


def test_area_cylinder(capfd):
    os.system("python exercises/0003_arithmetic.py")
    captured = capfd.readouterr()
    assert 470 < float(captured.out.strip("\n")) < 472
