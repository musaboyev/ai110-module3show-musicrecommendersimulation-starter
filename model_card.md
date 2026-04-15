# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**MoodRank 1.0**

---

## 2. Goal / Task

This recommender suggests songs from a small classroom dataset. It tries to match a user’s taste using mood, genre, energy, and a few audio features. It is for classroom exploration only, not for real users.

---

## 3. Data Used

The catalog has 115 songs. I added popular songs from pop, hip hop, rock, rnb, rap, indie pop, ballad, folk, country, and electronic styles. The file includes genre, mood, energy, tempo, valence, danceability, and acousticness. It does not include lyrics, artist popularity, or cultural context.

---

## 4. Algorithm Summary

The recommender gives points for songs that match the user’s genre and mood. It also gives points when a song’s energy, valence, danceability, and acousticness are close to the user’s target values. After every song gets a score, the system sorts the list from highest to lowest. The top songs are the final recommendations.

---

## 5. Observed Behavior / Biases

The recommender can overvalue mood and energy because those features are easy to compare. It can also repeat songs that feel very similar, which makes the results less diverse. Since the dataset is mostly popular music, the system may favor mainstream taste and miss smaller niches. It also cannot understand lyrics or deeper context, so some good songs may be ranked too low.

---

## 6. Evaluation Process

I tested the system with high-energy pop, chill lo-fi, intense hip hop, and a few tricky profiles with conflicting preferences. I checked whether the top 5 results matched the mood and energy I expected. I also compared outputs before and after removing genre from the score. That showed me how much the weights change the ranking. I saved the terminal output so I could compare the different runs.

---

---

## 7. Intended Use and Non-Intended Use

This system is designed for classroom use and small experiments. It is not meant for real listeners, and it should not be used to make important decisions about people. It works best when the user can give simple taste preferences.

---

## 8. Ideas for Improvement

If I kept working on this, I would add more user preferences like tempo range and artist preference. I would also try to improve diversity so the top songs do not feel too similar. A larger and more balanced dataset would help a lot too.

---

## 9. Personal Reflection

My biggest learning moment was seeing how small changes in weights could change the whole ranking. Using AI tools helped me move faster, but I still had to double-check the code and terminal output because the first version did not always match the design I wanted. I was surprised that a very simple algorithm could still feel like a real recommender when the songs and scores were explained clearly. If I extended the project, I would make the profile smarter and add more ways to balance diversity with accuracy.
