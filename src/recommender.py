from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        def score(song: Song) -> float:
            points = 0.0
            if song.genre == user.favorite_genre:
                points += 0.40
            if song.mood == user.favorite_mood:
                points += 0.20

            energy_closeness = max(0.0, 1.0 - abs(song.energy - user.target_energy))
            points += 0.15 * energy_closeness

            if user.likes_acoustic and song.acousticness >= 0.6:
                points += 0.05
            if not user.likes_acoustic and song.acousticness < 0.4:
                points += 0.05
            return points

        ranked = sorted(self.songs, key=score, reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons: List[str] = []
        if song.genre == user.favorite_genre:
            reasons.append("genre match")
        if song.mood == user.favorite_mood:
            reasons.append("mood match")

        energy_closeness = max(0.0, 1.0 - abs(song.energy - user.target_energy))
        reasons.append(f"energy closeness {energy_closeness:.2f}")

        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("acoustic preference")
        elif not user.likes_acoustic and song.acousticness < 0.4:
            reasons.append("less acoustic preference")

        return ", ".join(reasons) if reasons else "This song is a reasonable match."

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    import csv

    print(f"Loading songs from {csv_path}...")
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
                "popularity": int(row["popularity"]),
                "release_decade": int(row["release_decade"]),
                "mood_tag": row["mood_tag"],
                "instrumentation": row["instrumentation"],
                "dancefloor": row["dancefloor"],
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict, mode: str = "genre_first") -> Tuple[float, List[str]]:
    """Score one song against the user's preferences and return reasons."""
    score = 0.0
    reasons: List[str] = []

    if mode == "mood_first":
        weights = {
            "genre": 0.06,
            "mood": 0.24,
            "energy": 0.14,
            "valence": 0.09,
            "danceability": 0.09,
            "acousticness": 0.05,
            "popularity": 0.12,
            "release_decade": 0.10,
            "mood_tag": 0.08,
            "instrumentation": 0.02,
            "dancefloor": 0.01,
        }
    else:
        weights = {
            "genre": 0.24,
            "mood": 0.06,
            "energy": 0.14,
            "valence": 0.09,
            "danceability": 0.09,
            "acousticness": 0.05,
            "popularity": 0.12,
            "release_decade": 0.10,
            "mood_tag": 0.02,
            "instrumentation": 0.03,
            "dancefloor": 0.02,
        }

    favorite_genres = user_prefs.get("favorite_genres")
    if isinstance(favorite_genres, str):
        favorite_genres = [favorite_genres]
    if favorite_genres and song.get("genre") in favorite_genres:
        score += weights["genre"]
        reasons.append(f"genre match (+{weights['genre']:.2f})")

    favorite_mood = user_prefs.get("favorite_mood") or user_prefs.get("mood")
    if favorite_mood and song.get("mood") == favorite_mood:
        score += weights["mood"]
        reasons.append(f"mood match (+{weights['mood']:.2f})")

    numeric_targets = {
        "energy": user_prefs.get("target_energy", user_prefs.get("energy")),
        "valence": user_prefs.get("target_valence"),
        "danceability": user_prefs.get("target_danceability"),
        "acousticness": user_prefs.get("target_acousticness"),
    }

    for feature, target in numeric_targets.items():
        if target is None:
            continue
        song_value = float(song.get(feature, 0.0))
        closeness = max(0.0, 1.0 - abs(song_value - float(target)))
        feature_points = weights[feature] * closeness
        score += feature_points
        reasons.append(f"{feature} closeness (+{feature_points:.2f})")

    target_popularity = user_prefs.get("target_popularity")
    if target_popularity is not None:
        popularity_value = int(song.get("popularity", 0)) / 100.0
        closeness = max(0.0, 1.0 - abs(popularity_value - float(target_popularity)))
        feature_points = weights["popularity"] * closeness
        score += feature_points
        reasons.append(f"popularity closeness (+{feature_points:.2f})")

    target_decade = user_prefs.get("target_decade")
    if target_decade is not None:
        gap = abs(int(song.get("release_decade", 0)) - int(target_decade))
        closeness = max(0.0, 1.0 - (gap / 40.0))
        feature_points = weights["release_decade"] * closeness
        score += feature_points
        reasons.append(f"release decade closeness (+{feature_points:.2f})")

    target_mood_tag = user_prefs.get("target_mood_tag")
    if target_mood_tag and song.get("mood_tag") == target_mood_tag:
        score += weights["mood_tag"]
        reasons.append(f"detailed mood tag match (+{weights['mood_tag']:.2f})")

    target_instrumentation = user_prefs.get("preferred_instrumentation")
    if target_instrumentation and song.get("instrumentation") == target_instrumentation:
        score += weights["instrumentation"]
        reasons.append(f"instrumentation match (+{weights['instrumentation']:.2f})")

    target_dancefloor = user_prefs.get("target_dancefloor")
    if target_dancefloor and song.get("dancefloor") == target_dancefloor:
        score += weights["dancefloor"]
        reasons.append(f"dancefloor match (+{weights['dancefloor']:.2f})")

    if not reasons:
        reasons.append("no strong preference match")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k recommendations."""
    mode = user_prefs.get("mode", "genre_first")
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song, mode=mode)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
