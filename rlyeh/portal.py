# coding: utf-8

"""
Models a portal.
"""

from typing import Dict

import attr

from . import common
from .resonator import Resonator

_DEPLOY_LIMITS = [8, 4, 4, 4, 2, 2, 1, 1]


@attr.s(slots=True, frozen=True, auto_attribs=True)
class Portal(object):
    """
    An Ingress portal.

    Attributes:
        title (str): Displayed name of the portal.
        faction (Faction): Controlling faction (or None if uncaptured).
        owner (str): Capturing agent name (None if uncaptured).
        resonators: Mapping from position to resonator.
        level (int): Calculated portal level (1-8).
        health (int): Calculated portal health (1-6400).
    """
    title: str
    faction: common.Faction = attr.ib(default=None)
    owner: str = attr.ib(default=None)
    resonators: Dict[common.Position, Resonator] = attr.ib()
    level: int = attr.ib(init=False)
    health: int = attr.ib(init=False)

    @faction.validator
    def check_faction(self, attribute, value):
        if value is None:
            return

        if not isinstance(value, common.Faction):
            raise TypeError('faction must be a Faction value')

    @owner.validator
    def check_owner(self, attribute, value):
        # owner is set after faction, check mutual dependencies here
        if self.faction is None and value is not None:
            raise TypeError('owner must be set if faction is set')
        if self.faction is not None and value is None:
            raise TypeError('faction must be set if owner is set')

        if value is None:
            # don't check if unset
            return
        else:
            # defer to Resonator.owner's validator
            Resonator(level=1, agent=value)

    @resonators.default
    def _resonators(self):
        return {}

    @resonators.validator
    def check_resonators(self, attribute, value):
        by_agent = {}
        for pos, reso in value.items():
            if not isinstance(pos, common.Position):
                raise TypeError(f'invalid position {pos!r}')
            if not isinstance(reso, Resonator):
                raise TypeError(f'invalid resonator {reso!r}')

            agent_deploys = by_agent.setdefault(reso.agent, [])
            agent_deploys.append(reso.level)

        for agent, agent_deploys in by_agent.items():
            for i, limit in enumerate(reversed(_DEPLOY_LIMITS)):
                level = 8 - i
                count = agent_deploys.count(level)
                if count > limit:
                    raise ValueError(
                        f"agent '{agent}' has too many level {level} "
                        f'resonators ({count}, limit {limit})')

    @level.default
    def _level(self):
        # run the validator before accessing self.resonators
        self.check_resonators(type(self).resonators, self.resonators)
        calc = int(sum(r.level for r in self.resonators.values()) / 8.0)
        # a portal is never level 0, even when uncaptured
        return max(calc, 1)

    @health.default
    def _health(self):
        # run the validator before accessing self.resonators
        self.check_resonators(type(self).resonators, self.resonators)
        return int(sum(r.level * r.health for r in self.resonators.values()))
