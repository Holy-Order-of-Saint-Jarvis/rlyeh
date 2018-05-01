# coding: utf-8

import pytest
from rlyeh.common import Faction, Position
from rlyeh.portal import Portal
from rlyeh.resonator import Resonator


def test_posargs():
    p = Portal('testing')
    assert p.title == 'testing'
    assert p.faction is None
    assert p.owner is None
    assert p.resonators == {}
    assert p.level == 1
    assert p.health == 0

    p = Portal('testing', Faction.ENL, 'bob')
    assert p.title == 'testing'
    assert p.faction is Faction.ENL
    assert p.owner == 'bob'
    assert p.resonators == {}
    assert p.level == 1
    assert p.health == 0

    p = Portal('testing',
               Faction.ENL,
               'bob',
               {Position.NORTH: Resonator(8, 'bob')})
    assert p.title == 'testing'
    assert p.faction is Faction.ENL
    assert p.owner == 'bob'
    assert p.resonators[Position.NORTH].level == 8
    assert p.level == 1
    assert p.health == 800


def test_kwargs():
    p = Portal(title='testing')
    assert p.title == 'testing'
    assert p.faction is None
    assert p.owner is None
    assert p.resonators == {}
    assert p.level == 1
    assert p.health == 0

    p = Portal(title='testing', faction=Faction.ENL, owner='bob')
    assert p.title == 'testing'
    assert p.faction is Faction.ENL
    assert p.owner == 'bob'
    assert p.resonators == {}
    assert p.level == 1
    assert p.health == 0

    p = Portal(title='testing',
               faction=Faction.ENL,
               owner='bob',
               resonators={Position.NORTH: Resonator(level=8, agent='bob')})
    assert p.title == 'testing'
    assert p.faction is Faction.ENL
    assert p.owner == 'bob'
    assert p.resonators[Position.NORTH].level == 8
    assert p.level == 1
    assert p.health == 800


def test_validate_faction():
    with pytest.raises(TypeError):
        # faction must be a Faction if set
        Portal(title='testing', faction=8, owner='bob')


def test_validate_owner():
    with pytest.raises(TypeError):
        # owner must be a str if set
        Portal(title='testing', faction=Faction.ENL, owner=42)

    with pytest.raises(TypeError):
        # faction must be set if owner is set
        Portal(title='testing', owner='bob')

    with pytest.raises(TypeError):
        # owner must be set if faction is set
        Portal(title='testing', faction=Faction.ENL)


def test_validate_resonators():
    with pytest.raises(TypeError):
        # positions must be a Position
        Portal(title='testing',
               faction=Faction.ENL,
               owner='bob',
               resonators={42: Resonator(level=8, agent='bob')})

    with pytest.raises(TypeError):
        # resonators must be a Resonator
        Portal(title='testing',
               faction=Faction.ENL,
               owner='bob',
               resonators={Position.NORTH: 42})


def test_deploy_limits():
    expected = [8, 4, 4, 4, 2, 2, 1, 1]
    for level, limit in enumerate(expected):
        level = level + 1
        resos = dict(zip(Position, [Resonator(level, 'bob')] * limit))
        okay = Portal('title', Faction.ENL, 'bob', resos)
        assert len(okay.resonators) == limit

        if level != 1:
            resos = dict(
                zip(Position, [Resonator(level, 'bob')] * (limit + 1)))
            with pytest.raises(ValueError):
                Portal('title', Faction.ENL, 'bob', resos)


def test_validate_level():
    with pytest.raises(ValueError):
        Portal(title='testing',
               faction=Faction.ENL,
               owner='bob',
               resonators={Position.NORTH: Resonator(8, 'bob')},
               level=8)
