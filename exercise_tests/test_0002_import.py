import os


def test_import(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")
    captured = capfd.readouterr()
    assert captured.out == "4.0\n"
