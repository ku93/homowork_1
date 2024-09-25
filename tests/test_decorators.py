from src.decorators import log


# Testing functions for test log
@log(filename="logs.txt")
def func_and_file(x, y):
    return x / y


@log()
def func_no_file(x, y):
    return x / y


# Tests for log
def test_log_file(filename="logs.txt"):
    func_and_file(2, 2)
    with open(filename, "r", encoding="utf-8") as file:
        last_lines = file.readlines()[-4:]
        assert last_lines == [
            "Function func_and_file started\n",
            "Function func_and_file finished\n",
            "Result: 1.0\n",
            "\n",
        ]


def test_log_print(capsys):
    func_no_file(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "Function func_no_file started\nFunction func_no_file finished\nResult: 1.0\n\n"


def test_log_file_error(filename="logs.txt"):
    func_and_file(2, 0)
    with open(filename, "r", encoding="utf-8") as file:
        last_lines = file.readlines()[-5:]
        assert last_lines == [
            "Function func_and_file started\n",
            "Function func_and_file finished by error:\n",
            "<class 'ZeroDivisionError'>: division by zero\n",
            "Parameters - args: (2, 0), kwargs: {}\n",
            "\n",
        ]


def test_log_error_2(capsys):
    func_no_file(2, 0)
    captured = capsys.readouterr()
    assert captured.out == (
        "Function func_no_file started\nFunction func_no_file finished by error:\n"
        "<class 'ZeroDivisionError'>: division by zero\nParameters - args: (2, 0), kwargs: {}\n\n"
    )
