from streamlit.testing.v1 import AppTest

from logic_utils import check_guess


def test_fresh_game_starts_with_zero_attempts():
    app = AppTest.from_file("app.py").run(timeout=10)
    assert app.session_state["attempts"] == 0

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # Bug 2: a guess above the secret should tell the player to go lower.
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # A guess below the secret should tell the player to go higher.
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")
