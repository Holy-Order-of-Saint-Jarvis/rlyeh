# coding: utf-8

from typing import Dict

import attr

from . import common
from .resonator import Resonator

_DEPLOY_LIMITS = [8, 4, 4, 4, 2, 2, 1, 1]


@attr.s(slots=True, frozen=True, auto_attribs=True)
class Portal(object):
    title: str
    faction: common.Faction = attr.ib(default=None)
    owner: str = attr.ib(default=None)
    resonators: Dict[common.Position, Resonator] = attr.ib()
    level: int = attr.ib(default=None)
    health: int = attr.ib(init=False, default=None)

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

    @level.validator
    def check_level(self, attribute, value):
        expected = Portal._calculate_level(self.resonators)
        if value is None:
            object.__setattr__(self, 'level', expected)
            return

        if value != expected:
            raise ValueError('specified level does not agree with deploys')

    @health.validator
    def check_health(self, attribute, value):
        health = sum(r.level * r.health for r in self.resonators.values())
        object.__setattr__(self, 'health', health)

    @staticmethod
    def _calculate_level(resonators):
        levels = [r.level for r in resonators.values()]
        return max(int(sum(levels) / 8.0), 1)
