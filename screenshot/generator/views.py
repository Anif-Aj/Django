from django.shortcuts import render

# Create your views here.
import pyautogui
from .models import Screenshot

def take_screenshot_and_save():
    # Take the screenshot
    screenshot = pyautogui.screenshot()

    # Define file path
    file_path = 'media/screenshots/screenshot.png'
    screenshot.save(file_path)  # Save the screenshot locally

    # Save to the database
    screenshot_instance = Screenshot(title='My Screenshot', image=file_path)
    screenshot_instance.save()
    return screenshot_instance

from django.http import JsonResponse
from .utils import take_screenshot_and_save

def capture_screenshot(request):
    screenshot = take_screenshot_and_save()
    return JsonResponse({'message': 'Screenshot saved', 'id': screenshot.id})
