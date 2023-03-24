from itertools import permutations

from automatata.models.dfa import DFA


def test_dfa_model():
    dfa = DFA(
        alphabet={"a", "b"},
        transition={0: {"a": 0, "b": 1}, 1: {}},
        start=0,
        accept={1},
    )
    assert dfa.alphabet == {"a", "b"}
    assert dfa.states == {0, 1}
    assert dfa.start == 0
    assert dfa.accept == {1}


def test_one_or_mode_a_and_one_b():
    as_and_one_b = DFA(
        alphabet={"a", "b"},
        transition={0: {"a": 0, "b": 1}, 1: {}},
        start=0,
        accept={1},
    )

    assert not as_and_one_b.valid("")
    assert not as_and_one_b.valid("a")
    assert not as_and_one_b.valid("aaaaaaaaaaaa")
    assert as_and_one_b.valid("ab")
    assert as_and_one_b.valid("aaaaaaaaaaab")


def test_balanced_evens_or_odds():
    # TODO: hypothesis?
    balanced = DFA(
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

    assert balanced.valid("")
    assert not balanced.valid("a")
    assert balanced.valid("ab")
    assert balanced.valid("ba")
    assert not balanced.valid("aba")
    assert not balanced.valid("aab")
    assert not balanced.valid("abb")
    assert all(
        balanced.valid(p) for i in range(5) for p in permutations("a" * i + "b" * i)
    )
    assert balanced.valid("aaaabb")
    assert balanced.valid("aaabbb")


def test_other_hashable_states():
    dfa = DFA(
        alphabet={1, 2, 3},
        transition={
            (0, 0, 0): {
                1: (0, 0, 1),
                2: (0, 1, 0),
                3: (0, 1, 1),
            },
            (0, 0, 1): {
                1: (0, 1, 0),
                2: (0, 1, 1),
                3: (1, 0, 0),
            },
            (0, 1, 0): {
                1: (0, 1, 1),
                2: (1, 0, 0),
                3: (1, 0, 1),
            },
            (0, 1, 1): {
                1: (1, 0, 0),
                2: (1, 0, 1),
                3: (1, 1, 0),
            },
            (1, 0, 0): {
                1: (1, 0, 1),
                2: (1, 1, 0),
                3: (1, 1, 1),
            },
            (1, 0, 1): {
                1: (1, 1, 0),
                2: (1, 1, 1),
            },
            (1, 1, 0): {
                1: (1, 1, 1),
            },
            (1, 1, 1): {},
        },
        start=(0, 0, 0),
        accept={(1, 1, 1)},
    )
    assert dfa.valid([1, 1, 1, 1, 1, 1, 1])
    assert dfa.valid([1, 1, 1, 1, 1, 2])
    assert dfa.valid([1, 1, 1, 1, 2, 1])
    assert dfa.valid([1, 3, 2, 1])
