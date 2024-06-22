import os


def test_print(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")
    captured = capfd.readouterr()
    assert captured.out == "30\n"
