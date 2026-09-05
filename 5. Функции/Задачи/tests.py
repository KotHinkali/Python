import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.stdout.reconfigure(encoding="utf-8")

from tester import TaskConfig, TestCase, exact_match, run_module

_BASE_DIR = os.path.dirname(__file__)

TASKS = [
    TaskConfig(
        task_id="51",
        name="Простые числа",
        filename="Задание 51.py",
        time_limit=10.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1",  "2"),
            TestCase("2",  "2 3"),
            TestCase("3",  "2 3 5"),
            TestCase("5",  "2 3 5 7 11"),
            TestCase("7",  "2 3 5 7 11 13 17"),
            TestCase("10", "2 3 5 7 11 13 17 19 23 29"),
            TestCase("15", "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47"),
            TestCase("20", "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71"),
        ],
    ),
    TaskConfig(
        task_id="52",
        name="Совершенные числа",
        filename="Задание 52.py",
        time_limit=10.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1", "6"),
            TestCase("2", "6 28"),
            TestCase("3", "6 28 496"),
            TestCase("4", "6 28 496 8128"),
        ],
    ),
    TaskConfig(
        task_id="53",
        name="Числа-Палиндромы",
        filename="Задание 53.py",
        time_limit=10.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n20",    "1 2 3 4 5 6 7 8 9 11"),
            TestCase("100\n130", "101 111 121"),
            TestCase("12\n20",   "Нет палиндромов"),
            TestCase("13\n21",   "Нет палиндромов"),
            TestCase("1\n1",     "1"),
            TestCase("11\n11",   "11"),
            TestCase("1\n9",     "1 2 3 4 5 6 7 8 9"),
            TestCase("11\n55",   "11 22 33 44 55"),
            TestCase("22\n30",   "22"),
            TestCase("50\n55",   "55"),
            TestCase("90\n100",  "99"),
            TestCase("99\n101",  "99 101"),
            TestCase("200\n220", "202 212"),
            TestCase("1000\n1010", "1001"),
        ],
    ),
    TaskConfig(
        task_id="54",
        name="Дружественные числа",
        filename="Задание 54.py",
        time_limit=10.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("100",  "Нет дружественных чисел"),
            TestCase("219",  "Нет дружественных чисел"),
            TestCase("283",  "Нет дружественных чисел"),
            TestCase("284",  "(220, 284)"),
            TestCase("300",  "(220, 284)"),
            TestCase("1300", "(220, 284), (1184, 1210)"),
            TestCase("3000", "(220, 284), (1184, 1210), (2620, 2924)"),
        ],
    ),
    TaskConfig(
        task_id="55",
        name="Числа Армстронга",
        filename="Задание 55.py",
        time_limit=10.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n9",      "1 2 3 4 5 6 7 8 9"),
            TestCase("1\n200",    "1 2 3 4 5 6 7 8 9 153"),
            TestCase("100\n999",  "153 370 371 407"),
            TestCase("10\n99",    "Нет чисел Армстронга"),
            TestCase("200\n300",  "Нет чисел Армстронга"),
            TestCase("154\n369",  "Нет чисел Армстронга"),
            TestCase("153\n153",  "153"),
            TestCase("371\n500",  "371 407"),
            TestCase("1\n999",    "1 2 3 4 5 6 7 8 9 153 370 371 407"),
            TestCase("1000\n9999", "1634 8208 9474"),
        ],
    ),
]

if __name__ == "__main__":
    result = run_module("Функции", TASKS, _BASE_DIR)
    sys.exit(0 if result.solved_tasks == result.total_tasks else 1)
