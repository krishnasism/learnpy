import os


def test_area_cylinder(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")
    captured = capfd.readouterr()
    assert 470 < float(captured.out.strip("\n")) < 472
