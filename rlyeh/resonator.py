# coding: utf-8

"""
Models a deployed resonator.
"""

import re

import attr


@attr.s(slots=True, frozen=True, auto_attribs=True)
class Resonator(object):
    """
    Deployed resonator.

    Attributes:
        level (int): Resonator level (1-8).
        health (int): Resonator health (1-100).
        agent (str): Deploying agent name.
    """
    level: int = attr.ib()
    agent: str = attr.ib()
    health: int = attr.ib(default=100)

    @level.validator
    def check_level(self, attribute, value):
        if not isinstance(value, int):
            raise TypeError('level must be an int')
        if value < 1 or value > 8:
            raise ValueError('level must be between 1 and 8, inclusive')

    @agent.validator
    def check_agent(self, attribute, value):
        if not isinstance(value, str):
            raise TypeError('agent must be a str')
        if not re.match(r'^[a-zA-Z0-9-]+$', value):
            raise ValueError(f"invalid agent name '{value}'")

    @health.validator
    def check_health(self, attribute, value):
        if not isinstance(value, int):
            raise TypeError('health must be an int')
        if value < 1 or value > 100:
            raise ValueError('health must be between 1 and 100, inclusive')

    def damage(self, amount: int) -> 'Resonator':
        """
        Damage a resonator by a specified amount.

        Arguments:
            amount: Damage amount.

        Returns:
            The damaged resonator, or None if the resonator was destroyed.
        """
        remaining = self.health - amount
        if remaining < 1:
            return None
        else:
            return attr.evolve(self, health=remaining)
