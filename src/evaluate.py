try:
    from src.recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs

def evaluate():
    songs = load_songs("data/songs.csv")

    test_profiles = [
        {"genre": "pop", "target_energy": 0.8},
        {"genre": "hip hop", "target_energy": 0.9},
        {"genre": "lofi", "target_energy": 0.3},
    ]

    total = 0

    for prefs in test_profiles:
        recs = recommend_songs(prefs, songs, k=5)
        avg_score = sum(score for _, score, _ in recs) / len(recs)
        print(f"{prefs} → avg score: {avg_score:.2f}")
        total += avg_score

    print("\nFINAL SCORE:", total / len(test_profiles))

if __name__ == "__main__":
    evaluate()
