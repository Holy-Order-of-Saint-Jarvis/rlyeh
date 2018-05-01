# coding: utf-8

import pytest
from rlyeh.resonator import Resonator


def test_posargs():
    r = Resonator(8, 'agentname')
    assert r.level == 8
    assert r.agent == 'agentname'
    assert r.health == 100

    r = Resonator(8, 'agentname', 14)
    assert r.level == 8
    assert r.agent == 'agentname'
    assert r.health == 14

    with pytest.raises(TypeError):
        # missing agent
        Resonator(8)


def test_kwargs():
    r = Resonator(agent='agentname', level=8)
    assert r.level == 8
    assert r.agent == 'agentname'
    assert r.health == 100

    r = Resonator(health=14, agent='agentname', level=8)
    assert r.level == 8
    assert r.agent == 'agentname'
    assert r.health == 14

    with pytest.raises(TypeError):
        # missing agent
        Resonator(level=8)

    with pytest.raises(TypeError):
        # missing level
        Resonator(agent='agentname')

    with pytest.raises(TypeError):
        # missing agent and level
        Resonator(health=14)


def test_validate_level():
    with pytest.raises(TypeError):
        # level must be an int
        Resonator(level='4', agent='agentname')

    with pytest.raises(ValueError):
        # level must be >= 1
        Resonator(level=0, agent='agentname')

    with pytest.raises(ValueError):
        # level must be <= 8
        Resonator(level=9, agent='agentname')


def test_validate_agent():
    with pytest.raises(TypeError):
        # agent must be a str
        Resonator(level=8, agent=42)

    with pytest.raises(ValueError):
        # agent name must be alphanumeric with hyphens
        Resonator(level=8, agent='bad_agent_name')


def test_validate_health():
    with pytest.raises(TypeError):
        # health must be an int
        Resonator(level=8, agent='agentname', health='33')

    with pytest.raises(ValueError):
        # health must be >= 1
        Resonator(level=8, agent='agentname', health=0)

    with pytest.raises(ValueError):
        # health must be <= 100
        Resonator(level=8, agent='agentname', health=9001)


def test_damage():
    r = Resonator(level=8, agent='agentname')

    damaged = r.damage(10)

    assert damaged.agent == r.agent
    assert damaged.level == r.level
    assert damaged.health == 90

    destroyed = damaged.damage(999)
    assert destroyed is None
