# adventure_locator/generator.py
import random

# Sample locations by theme
LOCATIONS = {
    "Africa": ["Hazina Ridge", "Orisha Plains", "Crocodile River"],
    "Central America": ["Jaguar Prophecy", "Lost Oasis", "Crimson Canyon"],
    "Europe": ["Emerald Glade", "Frozen Peak", "Fae Corridor"],
    "Antartica": ["Mystic Ice Caves"],
}

def generate_adventure(theme=None):
    """Generate a random adventure location based on a theme."""
    if theme and theme in LOCATIONS:
        return random.choice(LOCATIONS[theme])
    
    # If no theme is specified, pick a random one
    chosen_theme = random.choice(list(LOCATIONS.keys()))
    return random.choice(LOCATIONS[chosen_theme])

if __name__ == "__main__":
    print("Random Adventure Location:", generate_adventure())
