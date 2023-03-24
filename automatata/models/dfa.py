"""Deterministic Finite Automata"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Hashable, Mapping, Sequence, TypeVar

L = TypeVar("L", bound=Hashable)
S = TypeVar("S", bound=Hashable)


@dataclass
class DFA(Generic[L, S]):
    alphabet: set[L]
    transition: Mapping[S, Mapping[L, S]]
    start: S
    accept: set[S]

    @property
    def states(self):
        return set(self.transition)

    def valid(self, word: Sequence[L]) -> bool:
        state = self.start
        for letter in word:
            state = self.transition[state][letter]
        return state in self.accept
