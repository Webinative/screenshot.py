# Webpage Screenshot Capture Script

This script captures full-page screenshots of a webpage in different form factors using Playwright.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (>=3.7)
- Playwright: Install using `pip install playwright`

## Usage

### Command-line Arguments

- `--url`: The URL of the webpage to capture screenshots.
- `--browser`: The browser to use for capturing screenshots (default: chrome). Options: ['chrome', 'chromium', 'firefox', 'safari', 'edge'].

### Example

```bash
python capture_screenshot.py --url https://example.com --browser chrome


Form Factors
The script captures screenshots for different form factors defined in the config.py file.

Output
Screenshots are saved in the screenshots/ directory with filenames corresponding to each form factor.

Customization
Modify the config.py file to add or modify form factors.
Change the output filename in the script as needed.