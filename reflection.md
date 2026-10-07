# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The game was a Streamlit number guessing game with a debug panel showing the secret, attempts, score, difficulty, and history. I reproduced three bugs before making changes. Bugs 1 and 2 were selected as the primary Phase 2 fixes; Bug 3 was documented but left outside the selected fixes.

**Bug Reproduction Log**

| Input / Trigger | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|---|---|---|---|---|
| Start a fresh game before making any guess. Debug panel showed Secret: 16, Difficulty: Normal. | Attempts should start at 0. | Attempts started at 1. | none | `app.py` session-state initialization for `attempts`. |
| With Secret: 16, enter guess `17` and submit. | Because 17 is greater than 16, the game should say to go LOWER. | The hint said `Go HIGHER!` | none | `check_guess` comparison and hint message in `app.py`. |
| After making a guess, click **New Game**. The new debug panel showed Secret: 21, Attempts: 0, Score: 5, History: [17]. | A new game should reset score to 0 and clear history. | The score stayed 5 and history stayed `[17]`. | none | `app.py` New Game reset block. |

## 2. How did you use AI as a teammate?

I used AI to help organize the repair into a small logic module, update the app imports, and design focused tests. I accepted the suggestion to move `check_guess`, `parse_guess`, the difficulty range, and score logic into `logic_utils.py` because this matched the assignment and made the logic testable. I verified that the app imported those functions and that the tests used their tuple return value.

I modified the broader reset suggestion by not fixing Bug 3 in this pass, because the assignment asked me to select Bugs 1 and 2 as the two primary fixes. I kept Bug 3 in the reproduction log and checked the final code so the documentation did not claim that it was fixed.

## 3. Debugging and testing your fixes

I used the three supplied reproductions to decide what needed to change. Bug 1 was fixed by initializing `st.session_state.attempts` to 0, and Bug 2 was fixed by returning `Go LOWER!` when the guess is greater than the secret. I added a Streamlit AppTest for the fresh-game attempt count and direct tests for the corrected hint tuple. Running `python -m pytest` completed successfully with all 4 tests passing in 2.79 seconds; a second verification run also passed all 4 tests in 2.07 seconds.

The tests also helped identify that `check_guess` returns `(outcome, message)`, so the assertions were updated to check the complete tuple. I did not claim Bug 3 was fixed because score and history reset were not part of the two selected fixes.

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from the top when a widget is used. Values that should survive those reruns must be stored in `st.session_state`; otherwise they are recreated each time. Initializing a state value only when its key is missing lets the value persist during the game.

## 5. Looking ahead: your developer habits

I want to reuse the habit of reproducing a bug before changing code and then adding a focused test for the fix. Next time, I would install and run the project dependencies earlier so verification is available throughout the repair. This project reinforced that AI-generated code still needs to be read, tested, and compared with the observed behavior.
