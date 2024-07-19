# Image Scraper for my Portfolio Website

This Python script fetches web pages and downloads specified images from those pages, saving them locally.

## Required Python packages:
- requests
- beautifulsoup4
- lxml
- Pillow

### You can install the required packages using the following command:

```bash
pip install requests beautifulsoup4 lxml Pillow
```

## How to Use

1) Clone the Repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

2) Run the Script:

```bash
python script.py
```

## Functions

- `download_image(url, file_name)`: Downloads an image from a given URL and saves it locally with the specified file name.
- `get_webpage(url)`: Fetches and parses a webpage using BeautifulSoup.

## URL Lists:

- `sql_urls`, `excel_urls`, `python_urls`: Lists of tuples containing web page URLs, image URLs, and local file names. The categories correspond to the different sections of my portfolio website.

The script will download images and save them with the following filenames:

- electric_car_image.jpg
- world_education_image.jpg
- inequality_image.jpg
- nyc_skyline.jpg
- heart.jpg
- construction.jpg
- cards.jpg
- polish.jpg
- dictionary.jpg
- web_scrape.jpg
- sql.jpg

Each downloaded image will be printed with a confirmation message indicating that it has been saved.

