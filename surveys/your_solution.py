
"""
Add your solution in here
"""
from typing import TypedDict


class Survey(TypedDict):
    """
    The structure of each survey
    a tx_id (unique identifier)
    a name: (also unique)
    """
    tx_id: int
    name: str


def find_fake_surveys(surveys: list[Survey]) -> list[tuple[int]]:
    """
    Given a list of surveys, return a list of tuples that correspond to the
    fake surveys
    """
    pass
