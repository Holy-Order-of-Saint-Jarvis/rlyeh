# coding: utf-8

"""
Common (simple) types.
"""

from enum import Enum, auto


class Position(Enum):
    """
    Represents a compass position as used in resonator deployment.
    """
    NORTH = auto()
    NORTHEAST = auto()
    EAST = auto()
    SOUTHEAST = auto()
    SOUTH = auto()
    SOUTHWEST = auto()
    WEST = auto()
    NORTHWEST = auto()


class Faction(str, Enum):
    """
    Agent faction.
    """
    ENL = 'Enlightened'
    RES = 'Resistance'
