# Screen regions for different poker actions
# These coordinates will need to be adjusted based on your screen resolution
ACTION_REGIONS = {
    'fold':  {'x': 1115, 'y': 930, 'width': 150, 'height': 65},
    'call':  {'x': 1285, 'y': 930, 'width': 150, 'height': 65},
    'raise': {'x': 1485, 'y': 930, 'width': 150, 'height': 65}
}

# Delay between actions (in seconds)
ACTION_DELAY = 1.0

# Confidence threshold for image recognition
CONFIDENCE_THRESHOLD = 0.8

# Screen capture settings
SCREEN_CAPTURE_INTERVAL = 0.5  # seconds 