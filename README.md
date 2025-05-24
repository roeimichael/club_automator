# ClubGG Poker Automator

An automated poker bot for ClubGG platform that can perform random actions based on screen analysis.

## Setup

1. Install Python 3.8 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `src/` - Main source code directory
  - `screen_reader.py` - Handles screen capture and analysis
  - `action_controller.py` - Controls mouse movements and clicks
  - `game_logic.py` - Contains game-specific logic and decision making
  - `config.py` - Configuration settings and constants
- `main.py` - Entry point of the application

## Usage

Run the main script:
```bash
python main.py
```

## Note

This is a basic implementation that performs random actions. Use responsibly and in accordance with ClubGG's terms of service. 