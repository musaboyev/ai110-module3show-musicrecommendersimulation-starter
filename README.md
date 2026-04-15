# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

My recommender uses a small taste profile and compares it against the features in `data/songs.csv`. Each song has `genre`, `mood`, `energy`, `valence`, `danceability`, `acousticness`, and `tempo_bpm`. The user profile stores the listener’s preferred genres, preferred mood, and target values for the numeric features.

The scoring rule gives the most weight to genre, then mood, then the numeric features. A song gets more points when its genre or mood matches the user profile, and when its numeric values are close to the target values in the user profile. This means the system rewards songs that feel similar to what the user asked for instead of only preferring bigger or smaller numbers.

The ranking rule is simple: score every song, sort the songs from highest score to lowest score, and return the top `K` songs. That makes the final recommendation list easy to understand and easy to explain.

Final algorithm recipe:

```text
score =
0.40 * genre_match
0.20 * mood_match
0.15 * energy_closeness
0.10 * valence_closeness
0.10 * danceability_closeness
0.05 * acousticness_closeness
```

One limitation of this design is that it can over-prioritize genre and mood, which may hide songs that fit the user’s vibe well but come from a different genre. It also depends on the quality of the taste profile, so if the user gives vague answers, the recommendations may be less accurate.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---
## CLI Verification

I ran `python -m src.main` and confirmed the recommender prints a ranked list of songs.

![CLI output](screenshot.png)

I also saved the terminal output here: [output.txt](output.txt)

### Saved Outputs

I used text files here instead of screenshots because they were faster to save and easier to compare.

- [Original output](output.txt)
- [Mood-based output](mood_based_output.txt)
- [Genre-first output](genre_first_output.txt)
- [Mood-first output](mood_first_output.txt)

### Challenge Summary

I completed Challenge 1, Challenge 2, and Challenge 4. Challenge 3 is still not fully implemented because I did not add a real diversity penalty for repeated artists or genres.


## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
