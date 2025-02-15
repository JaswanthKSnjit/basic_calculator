import pytest
import sys
from io import StringIO
from app.calculator import Calculator


def simulate_calculator(monkeypatch, inputs):
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    captured_output = StringIO()
    sys.stdout = captured_output
    Calculator.run()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_start_and_quit(monkeypatch):
    output = simulate_calculator(monkeypatch, ["7"])
    assert "Calculator Menu" in output
    assert "Exiting calculator. Goodbye!" in output


def test_addition(monkeypatch):
    # 1 => addition
    output = simulate_calculator(monkeypatch, ["1", "3", "2", "7"])
    assert "The result is: 5.0" in output


def test_subtraction(monkeypatch):
    # 2 => subtract
    output = simulate_calculator(monkeypatch, ["2", "10", "4", "7"])
    assert "The result is: 6.0" in output


def test_multiplication(monkeypatch):
    # 3 => multiply
    output = simulate_calculator(monkeypatch, ["3", "2", "3", "7"])
    assert "The result is: 6.0" in output


def test_division_by_zero(monkeypatch):
    # 4 => division
    output = simulate_calculator(monkeypatch, ["4", "5", "0", "7"])
    assert "Cannot divide by zero." in output


def test_invalid_number_input(monkeypatch):
    # 1 => addition, then invalid "abc", then valid "2", "3", then 7 => quit
    output = simulate_calculator(monkeypatch, ["1", "abc", "2", "3", "7"])
    assert "Invalid number" in output


def test_history(monkeypatch):
    # 1 => addition with (1,1), then 5 => history, then 7 => quit
    output = simulate_calculator(monkeypatch, ["1", "1", "1", "5", "7"])
    assert "1.0 addition 1.0 = 2.0" in output


def test_clear_history_via_repl(monkeypatch):
    # 6 => clear, then 7 => quit
    output = simulate_calculator(monkeypatch, ["6", "7"])
    assert "History has been cleared." in output


def test_clear_history_direct(capsys):
    Calculator.clear_history()
    captured = capsys.readouterr()
    assert "History has been cleared." in captured.out


def test_quit_during_number_input(monkeypatch):
    # 1 => addition, then first number "5", second number "quit"
    output = simulate_calculator(monkeypatch, ["1", "5", "quit"])
    assert "Exiting calculator. Goodbye!" in output


def test_invalid_command(monkeypatch):
    # Type "999" => invalid, then "7" => quit
    output = simulate_calculator(monkeypatch, ["999", "7"])
    assert "Invalid choice" in output


def test_compute_divide_by_zero_direct():
    # Direct test for compute() coverage
    result = Calculator.compute("division", 5, 0)
    assert result is None


def test_stoptest_command(monkeypatch):
    # 8 => hidden command for coverage
    output = simulate_calculator(monkeypatch, ["8"])
    assert "Testing coverage for final line." in output


def test_quit_as_first_number(monkeypatch):
    # 1 => addition, then "quit" as first number
    output = simulate_calculator(monkeypatch, ["1", "quit"])
    assert "Exiting calculator. Goodbye!" in output


def test_empty_history(monkeypatch):
    # 5 => history, then 7 => quit
    output = simulate_calculator(monkeypatch, ["5", "7"])
    assert "No calculations recorded." in output
