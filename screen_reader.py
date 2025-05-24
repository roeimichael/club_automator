import pyautogui
import pytesseract
from PIL import Image
from config import ACTION_REGIONS, CONFIDENCE_THRESHOLD
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\roeym\Desktop\tesseract\tesseract.exe'

# Map possible OCR results to action names
ACTION_TEXTS = {
    'fold': ['fold', 'check / fold', 'check/fold'],
    'check': ['check', 'check / fold', 'check/fold'],
    'call': ['call'],
    'raise': ['raise', 'raise to'],
}

class ScreenReader:
    def __init__(self):
        self.available_actions = []

    def capture_screen(self):
        """Capture the current screen"""
        return pyautogui.screenshot()

    def get_available_actions(self):
        """
        Analyze the screen and return available actions
        Returns a list of available actions (fold, check, call, raise)
        """
        screen = self.capture_screen()
        available_actions = []

        for action, region in ACTION_REGIONS.items():
            # Crop the button region
            left = region['x']
            top = region['y']
            right = left + region['width']
            bottom = top + region['height']
            button_img = screen.crop((left, top, right, bottom))

            # Save the crop for debugging
            debug_path = f"debug_crop_{action}.png"
            button_img.save(debug_path)
            print(f"Saved crop for '{action}' to {os.path.abspath(debug_path)}")

            # OCR the button text
            text = pytesseract.image_to_string(button_img).lower().strip()
            print(f"OCR for '{action}': {text}")
            # Check if any of the expected texts are in the OCR result
            for key, possible_texts in ACTION_TEXTS.items():
                if action == key and any(t in text for t in possible_texts):
                    available_actions.append(action)
                    break

        return available_actions

    def get_action_coordinates(self, action):
        """
        Get the coordinates for a specific action
        Returns (x, y) coordinates for the center of the action button
        """
        if action not in ACTION_REGIONS:
            raise ValueError(f"Unknown action: {action}")

        region = ACTION_REGIONS[action]
        x = region['x'] + region['width'] // 2
        y = region['y'] + region['height'] // 2
        return (x, y) 