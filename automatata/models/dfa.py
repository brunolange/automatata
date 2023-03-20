"""Deterministic Finite Automata"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Hashable, Mapping, Sequence, TypeVar

H = TypeVar("H", bound=Hashable)

State = int


@dataclass
class DFA(Generic[H]):
    alphabet: set[H]
    transition: Mapping[State, Mapping[H, State]]
    start: State
    accept: set[State]

    @property
    def states(self):
        return set(self.transition)

    def valid(self, word: Sequence[H]) -> bool:
        state = self.start
        for letter in word:
            state = self.transition[state][letter]
        return state in self.accept
