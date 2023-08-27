# AnimePlanet-Web-Scraping


This script allows you to scrape anime information for a specific season from Anime-Planet Website and create a Word document with the details.

## Prerequisites

- Python 3.x installed
- Required packages:
    - `requests`
    - `beautifulsoup4`
    - `Pillow`
    - `python-docx`

You can install these packages using the following command:
```bash
pip install requests beautifulsoup4 Pillow python-docx
```

## Usage

1. Run the script `anime_season_scraping.py`.
2. The script will prompt you to input a season in the format `season-YYYY` (e.g., `summer-2023`). If no season is entered, the default season `summer-2023` will be used.
3. The script will scrape anime data for the specified season from Anime-Planet and generate a Word document named `anime_season.docx` with the information.

## Features

- Scrapes anime data for the specified season.
- Generates a Word document with season name, anime names, number of episodes, and anime images.
- Resizes and inserts anime images into the document.

## Customization

You can customize the script by modifying the following parts:
- `season` variable: Set your desired season in the format `season-YYYY`.
- `image.thumbnail((156, 222))`: Customize the size of the inserted images by changing the dimensions `(156, 222)`.

## Note

- The script uses web scraping to gather anime data from Anime-Planet. Ensure you have a stable internet connection.
- The script may encounter issues if the website structure changes. Regularly update the script if necessary.

## Author

Noureldin Mohamed
