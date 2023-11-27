import os
import argparse
from playwright.sync_api import sync_playwright

from utils import form_factors, save_folder

# Create the save folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

def capture_full_page_screenshot(url, browser_name, output_file, width, height):
    """
    Capture a full-page screenshot of a webpage.

    Parameters:
        url (str): The URL of the webpage to capture.
        browser_name (str): The browser to use for capturing screenshots.
                            Options: ['chrome', 'chromium', 'firefox', 'safari', 'edge'].
        output_file (str): The output file path to save the screenshot.
        width (int): The width of the viewport.
        height (int): The height of the viewport.
    """
    with sync_playwright() as p:
        if browser_name == 'chrome':
            browser = p.chromium.launch()
        elif browser_name == 'firefox':
            browser = p.firefox.launch()
        else:
            browser = p.chromium.launch()
        context = browser.new_context(viewport={'width': width, 'height': height})
        page = context.new_page()

        # Navigate to the URL
        page.goto(url)

        # Capture a full page screenshot
        page.screenshot(path=output_file, full_page=True)

        # Close the browser
        browser.close()

if __name__ == "__main__":
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description='Capture screenshots of a webpage in different form factors.')
    parser.add_argument('--url', type=str, help='The URL of the webpage to capture screenshots.')
    parser.add_argument('--browser', choices=['chrome', 'chromium', 'firefox', 'safari', 'edge'], default='chrome',
                        help='The browser to use for capturing screenshots (default: chrome).')

    # Parse the command-line arguments
    args = parser.parse_args()
    url_to_capture = args.url
    browser_name = args.browser

    for form_factor in form_factors:
        # Replace 'screenshot.png' with the desired output file name
        output_file_name = f'screenshots/screenshot_{form_factor["name"]}.png'

        # Capture screenshot for the current form factor
        capture_full_page_screenshot(url_to_capture, browser_name, output_file_name, form_factor["width"],
                                     form_factor["height"])
