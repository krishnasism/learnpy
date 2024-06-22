import os


def test_common_games(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")

    expected_commons = ["Among Us", "Stardew Valley"]

    captured = capfd.readouterr().out.strip("\n")
    captured_list = captured.split(",")
    assert len(captured_list) == 2

    for expected_common in expected_commons:
        assert expected_common in captured
