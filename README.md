# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game is a Streamlit number guessing game. The player chooses a difficulty, enters guesses, receives hints, and can inspect the current game state in the developer panel.
- [x] I reproduced three bugs: a fresh game started with Attempts at 1, a guess above the secret incorrectly said to go higher, and New Game left the score and history unchanged.
- [x] I selected and fixed the first two bugs. I also moved the game logic into `logic_utils.py` and updated the tests to match the `(outcome, message)` API. Bug 3 remains documented as an unfixed issue from Phase 1.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start the Streamlit app and choose a difficulty such as Normal.
2. Open **Developer Debug Info** before guessing; a fresh game shows Attempts: 0, Score: 0, and an empty History.
3. Enter a guess and submit it. The game compares the guess with the stable secret and records the attempt.
4. If the guess is higher than the secret, the hint says `Go LOWER!`; if it is lower, the hint says `Go HIGHER!`.
5. Use the score and game status messages to continue until winning or reaching the attempt limit.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
> python -m pytest
4 passed in 2.79s
```

The full pytest suite was verified successfully with `python -m pytest`: 4 passed in 2.79s. A second verification run also completed successfully: 4 passed in 2.07s. Streamlit verification is not recorded here because no successful Streamlit result was provided.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
