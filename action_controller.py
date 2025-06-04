import pyautogui
import random
import time
from config import ACTION_DELAY

class ActionController:
    def __init__(self):
        # Set up pyautogui safety features
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

    def perform_action(self, action, coordinates):
        """
        Perform a poker action by clicking at the specified coordinates
        """
        x, y = coordinates
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        time.sleep(ACTION_DELAY)

    def perform_random_action(self, available_actions, screen_reader):
        """
        Choose and perform a random action from the available actions
        """
        if not available_actions:
            return

        action = random.choice(available_actions)
        coordinates = screen_reader.get_action_coordinates(action)
        self.perform_action(action, coordinates)
        return action 