# automatata

Automata in Python!

## Usage

Here's a Deterministic Finite Automaton that implements a language where words
either have both even number of "a"s and "b"s or odd number of "a"s and "b"s.

```python
from automatata.models.dfa import DFA

language = DFA(
    alphabet={"a", "b"},
    transition={
        0: {
            "a": 1,
            "b": 1,
        },
        1: {
            "a": 0,
            "b": 0,
        },
    },
    start=0,
    accept={0},
)

assert language.valid("")
assert not language.valid("a")
assert language.valid("ab")
assert language.valid("ba")
assert not language.valid("aba")
assert not language.valid("aab")
assert not language.valid("abb")
for i in range(10):
    for p in permutations("a"*i + "b"+i):
        assert language.valid(p)
assert language.valid("aaaabb")
```
