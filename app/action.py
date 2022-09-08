from __future__ import annotations

from enum import Enum


class ActionType(Enum):
    """Represents actions."""
    ADD = 1
    CHANGE = 2
    REMOVE = 3
    CALCULATE = 4

    @classmethod
    def from_string(cls, string: str) -> ActionType:
        """
        Builds ActionType from `string`
        :param string: A string
        :return: ActionType
        """
        match string.lower():
            case "add":
                return cls.ADD
            case "remove":
                return cls.REMOVE
            case "change":
                return cls.CHANGE
            case "calculate":
                return cls.CALCULATE
            case _:
                raise ValueError(f"Invalid action {string}")
