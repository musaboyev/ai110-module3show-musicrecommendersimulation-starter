"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import sys

from src.recommender import load_songs, recommend_songs


def print_recommendation_table(label: str, user_prefs: dict, recommendations) -> None:
    """Print a simple ASCII table for one set of recommendations."""
    print(f"\n=== {label} ===")
    print(f"Profile: {user_prefs}\n")

    rows = []
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        rows.append((str(index), song["title"], f"{score:.2f}", explanation))

    headers = ("#", "Title", "Score", "Reason")
    widths = [
        max(len(headers[0]), max(len(row[0]) for row in rows)),
        max(len(headers[1]), max(len(row[1]) for row in rows)),
        max(len(headers[2]), max(len(row[2]) for row in rows)),
        max(len(headers[3]), max(len(row[3]) for row in rows)),
    ]

    def line() -> str:
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def cell(text: str, width: int) -> str:
        return f" {text.ljust(width)} "

    print(line())
    print(
        "|" + "|".join(
            [
                cell(headers[0], widths[0]),
                cell(headers[1], widths[1]),
                cell(headers[2], widths[2]),
                cell(headers[3], widths[3]),
            ]
        ) + "|"
    )
    print(line())
    for row in rows:
        print(
            "|"
            + "|".join(
                [
                    cell(row[0], widths[0]),
                    cell(row[1], widths[1]),
                    cell(row[2], widths[2]),
                    cell(row[3], widths[3]),
                ]
            )
            + "|"
        )
    print(line())


def main() -> None:
    songs = load_songs("data/songs.csv")
    mode = sys.argv[1] if len(sys.argv) > 1 else "genre_first"

    user_prefs0 = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "target_popularity": 0.9,
        "target_decade": 2020,
        "target_mood_tag": "euphoric",
        "preferred_instrumentation": "electronic",
        "target_dancefloor": "high",
    }
    user_prefs1 = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "target_popularity": 0.55,
        "target_decade": 2020,
        "target_mood_tag": "serene",
        "preferred_instrumentation": "acoustic",
        "target_dancefloor": "low",
    }
    user_prefs2 = {
        "genre": "hip hop",
        "mood": "intense",
        "energy": 0.9,
        "target_popularity": 0.85,
        "target_decade": 2010,
        "target_mood_tag": "aggressive",
        "preferred_instrumentation": "electronic",
        "target_dancefloor": "high",
    }
    tricky_user_prefs0 = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.15,
        "target_popularity": 0.8,
        "target_decade": 1980,
        "target_mood_tag": "nostalgic",
        "preferred_instrumentation": "acoustic",
        "target_dancefloor": "low",
    }
    tricky_user_prefs1 = {
        "genre": "lofi",
        "mood": "intense",
        "energy": 0.9,
        "target_popularity": 0.4,
        "target_decade": 2000,
        "target_mood_tag": "aggressive",
        "preferred_instrumentation": "band",
        "target_dancefloor": "high",
    }
    tricky_user_prefs2 = {
        "genre": "hip hop",
        "mood": "chill",
        "energy": 0.5,
        "target_popularity": 0.75,
        "target_decade": 2010,
        "target_mood_tag": "nostalgic",
        "preferred_instrumentation": "hybrid",
        "target_dancefloor": "medium",
    }

    profiles = [
        ("user_prefs0", user_prefs0),
        ("user_prefs1", user_prefs1),
        ("user_prefs2", user_prefs2),
        ("tricky_user_prefs0", tricky_user_prefs0),
        ("tricky_user_prefs1", tricky_user_prefs1),
        ("tricky_user_prefs2", tricky_user_prefs2),
    ]

    for label, user_prefs in profiles:
        prefs = dict(user_prefs)
        prefs["mode"] = mode
        recommendations = recommend_songs(prefs, songs, k=5)
        print_recommendation_table(f"{label} ({mode})", user_prefs, recommendations)


if __name__ == "__main__":
    main()
