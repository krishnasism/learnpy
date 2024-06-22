import os


def test_intro(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")
    captured = capfd.readouterr()
    assert captured.out == "Hello World!\n"
