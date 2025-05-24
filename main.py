import time
from screen_reader import ScreenReader
from action_controller import ActionController
from config import SCREEN_CAPTURE_INTERVAL

def main():
    print("Starting ClubGG Poker Automator...")
    print("Press Ctrl+C to stop the program")
    
    screen_reader = ScreenReader()
    action_controller = ActionController()
    
    try:
        # while True:
            # Get available actions
        available_actions = screen_reader.get_available_actions()
        
        if available_actions:
            # Perform a random action
            action = action_controller.perform_random_action(available_actions, screen_reader)
            print(f"Performed action: {action}")
        
        # Wait before next iteration
        time.sleep(SCREEN_CAPTURE_INTERVAL)
            
    except KeyboardInterrupt:
        print("\nStopping ClubGG Poker Automator...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
