# coding: utf-8

from enum import Enum, auto


class Position(Enum):
    NORTH = auto()
    NORTHEAST = auto()
    EAST = auto()
    SOUTHEAST = auto()
    SOUTH = auto()
    SOUTHWEST = auto()
    WEST = auto()
    NORTHWEST = auto()


class Faction(str, Enum):
    ENL = 'Enlightened'
    RES = 'Resistance'
