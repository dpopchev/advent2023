from typing import Iterable

import pytest

from advent2023.day1 import (
    find_calibration_value,
    find_calibration_value_sum, find_digit,
)

SCENARIOS: Iterable[tuple[str, str]] = (
    ('two1nine', '29'),
    ('eightwothree', '83'),
    ('abcone2threexyz', '13'),
    ('xtwone3four', '24'),
    ('4nineeightseven2', '42'),
    ('zoneight234', '14'),
    ('7pqrstsixteen', '76'),
)

SCENARIO_TOTALS_SUM = 281


@pytest.mark.parametrize(
    'tcase, expected', SCENARIOS,
    ids=(s[0] for s in SCENARIOS),
)
def test_finding_frist_calibration_digit(tcase, expected):
    assert find_digit(tcase) == expected[0]

@pytest.mark.parametrize(
    'tcase, expected', SCENARIOS,
    ids=(s[0] for s in SCENARIOS),
)
def test_finding_last_calibration_digit(tcase, expected):
    assert find_digit(tcase, is_last=True) == expected[1]

@pytest.mark.parametrize(
    'tcase, expected', SCENARIOS,
    ids=(s[0] for s in SCENARIOS),
)
def test_finding_calibration_values(tcase, expected):
    assert find_calibration_value(tcase) == expected


@pytest.mark.parametrize('scenarios', [SCENARIOS])
def test_calibration_value_sum(scenarios):
    actual = find_calibration_value_sum((s for s, _ in scenarios))
    assert actual == SCENARIO_TOTALS_SUM
