# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I played the game I decided to go in blind, analyzing only what was on the screen. When I began to input my guesses, I followed the hints as instructed and noticed something was wrong when I guessed '0' and the hint was still telling me to go lower. I tried guessing a higher number but I ran out of turns.

- List at least two concrete bugs you noticed at the start.
I noticed that incorrect hints were given for each guess. When the guess is too high the hint is to guess a higher number, and if my guess is too low the hint is to guess a lower number. I also noticed that the when you click the 'New Game' button, instead of starting a new game it displays the message 'Start a new game to play again.'

<!-- markdownlint-disable-next-line MD036 -->
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location
-------- | -------- | -------- | -------- | --------
 Guess of 50 when secret is 11 | "Go LOWER" hint shown | "Go Higher" hint shown | "📈 Go HIGHER!" | `app.py`, `def check_guess()`
 Correct guess in 5 attempts | Final score of 20 shown | Final score of 30 shown | "Final score: 30" | `app.py`, `def update_score()`
 'New Game' button toggled | New game started | Current game still displayed | "You already won. Start a new game to play again." | `app.py`, `if new_game:`

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
