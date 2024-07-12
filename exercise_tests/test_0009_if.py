import os


def test_pass_fail(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")

    captured = capfd.readouterr().out.strip("\n")
    assert captured == "ok"