# AI Recommendation System
# Project 3 - DecodeLabs

recommendations = {
    "technology": [
        "Python Programming",
        "Artificial Intelligence",
        "Machine Learning",
        "Data Science"
    ],
    "sports": [
        "Football",
        "Cricket",
        "Basketball",
        "Badminton"
    ],
    "music": [
        "Classical Music",
        "Pop Music",
        "Rock Music",
        "Jazz"
    ],
    "movies": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers: Endgame"
    ],
    "books": [
        "Atomic Habits",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Deep Work"
    ]
}

print("=" * 40)
print("      AI Recommendation System")
print("=" * 40)

print("\nAvailable Categories:")
for category in recommendations:
    print("-", category.title())

user_choice = input("\nEnter your interest: ").strip().lower()

if user_choice in recommendations:
    print("\nRecommended Items:")
    for item in recommendations[user_choice]:
        print("✓", item)
else:
    print("\nSorry! No recommendations found.")
    print("Available categories are:")
    for category in recommendations:
        print("-", category.title())