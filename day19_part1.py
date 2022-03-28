"""

"""
from __future__ import annotations
from pathlib import Path
import pytest

@pytest.mark.parametrize(
    ('input_s', 'expected'),

)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def compute(s: str) -> int:






def main() -> int:
    input_data: str = Path('day19_input.txt').read_text().rstrip()
    print(compute(input_data))


if __name__ == '__main__':
    raise SystemExit(main())
