# Screenshot.py

Capture full-page screenshots of webpages in the follwing form factors,

Device / Orientation | Width (px) | Height (px)
--- | --- | ---
iPhone 8 | 375 | 667
iPad Portrait | 768 | 1024
iPad Landscape | 1024 | 768
Laptop | 1280 | 720
Desktop | 1440 | 800
Full HD | 1920 | 1080

## Prerequisites

- Python (>=3.7)

## Installation

```bash
# clone the repository
git clone git@github.com:Webinative/screenshot.py.git

cd screenshot.py

# create new virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install the required packages
python3 -m pip install -r requirements.txt

# download playwright browsers
playwright install
```

## Usage

```bash
python screenshot.py --url https://example.com --browser chrome --color_scheme dark
```

The above command captures screenshots of the given URL and saves them to the "screenshots" folder.

### Command-line Arguments

Argument | Description
--- | ---
`--url` | The URL of the webpage to capture screenshots.
`--browser` | The browser (engine) to use for capturing screenshots (default: chrome).
`--color_scheme` | The browser Color scheme enabled as dark mode (default: light)
Support for `chromium`, `firefox`, `safari` and `edge` coming soon.

## Customisation

Modify the `utils.py` file to customise further.

- `form_factors` - Add, edit or remove devices / screen sizes.
- `save_folder` – Change the target folder where screenshots are saved.
