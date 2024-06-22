import os


def test_multiply_list(capfd):
    file = f"exercises/{os.path.basename(__file__).replace("test_", "")}"
    os.system(f"python {file}")
    captured = capfd.readouterr()
    output = captured.out.strip().strip("\n").split()
    modified_numbers = [int(num) for num in output]
    expected_numbers = [2, 4, 6, 8, 10]  # Expected output after multiplying each element by 2
    assert modified_numbers == expected_numbers
