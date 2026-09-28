import pytest

from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_string_secret_compares_numerically():
    # Regression: a str secret used to hit a lexicographic compare,
    # where "9" > "50" reported a low guess as "Too High".
    assert check_guess(9, "50")[0] == "Too Low"
    assert check_guess(60, "50")[0] == "Too High"
    assert check_guess(50, "50")[0] == "Win"

# The word each outcome must steer the player toward, and the word it must
# never contain. Swapping these is the original bug: a "Too High" guess was
# answered with "Go HIGHER!", pushing the player further from the secret.
STEER = {"Too High": ("LOWER", "HIGHER"), "Too Low": ("HIGHER", "LOWER")}


@pytest.mark.parametrize(
    "guess, secret, expected",
    [
        (51, 50, "Too High"),   # one above
        (60, 50, "Too High"),   # just above
        (100, 50, "Too High"),  # far above
        (49, 50, "Too Low"),    # one below
        (40, 50, "Too Low"),    # just below
        (1, 50, "Too Low"),     # far below
        (9, 50, "Too Low"),     # single digit: also guards the "9" > "50" case
    ],
)
def test_hint_steers_toward_secret(guess, secret, expected):
    outcome, message = check_guess(guess, secret)

    assert outcome == expected, (
        "guess %d vs secret %d should be %s, got %s" % (guess, secret, expected, outcome)
    )

    want, must_not = STEER[expected]
    assert want in message, (
        "a %s guess must say %s, got: %s" % (expected, want, message.encode("ascii", "replace"))
    )
    assert must_not not in message, (
        "a %s guess must never say %s, got: %s"
        % (expected, must_not, message.encode("ascii", "replace"))
    )

WRONG_OUTCOMES = ["Too High", "Too Low"]
ATTEMPTS = [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.parametrize("attempt_number", ATTEMPTS)
@pytest.mark.parametrize("outcome", WRONG_OUTCOMES)
def test_wrong_guess_never_increases_score(outcome, attempt_number):
    # A guess that missed must cost the player points, on every attempt.
    # The bug: "Too High" on an even attempt awarded +5 instead.
    before = 100
    after = update_score(before, outcome, attempt_number)

    assert after < before, (
        "a %s guess on attempt %d changed score %d -> %d; "
        "a wrong guess must never be rewarded"
        % (outcome, attempt_number, before, after)
    )


@pytest.mark.parametrize("attempt_number", ATTEMPTS)
def test_penalty_identical_for_both_directions(attempt_number):
    # Guessing too high and too low are equally wrong, so they must cost
    # the same -- regardless of whether the attempt number is odd or even.
    high = update_score(100, "Too High", attempt_number)
    low = update_score(100, "Too Low", attempt_number)

    assert high == low, (
        "attempt %d: Too High -> %d but Too Low -> %d; "
        "penalty must not depend on direction or attempt parity"
        % (attempt_number, high, low)
    )
