import requests
import bs4
from PIL import Image
import os

def download_image(url, file_name):
    res = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(res.content)
    print(f'Image saved as {file_name}')

def get_webpage(url):
    res = requests.get(url)
    print(f'{url} response: {res}')
    return bs4.BeautifulSoup(res.text, 'lxml')

sql_urls = [
    ('https://www.mida.gov.my/malaysias-shift-towards-green-mobility/', 
     'https://www.mida.gov.my/wp-content/uploads/2022/10/1-7-scaled-600x400.jpg', 
     'electric_car_image.jpg'),
    ('https://www.thehansindia.com/hans/young-hans/importance-of-global-education-courses-729499?infinitescroll=1', 
     'https://assets.thehansindia.com/h-upload/2022/02/15/1277023-ed.webp', 
     'world_education_image.jpg'),
    ('https://www.cbc.ca/radio/ideas/mystery-of-money-1.6734524', 
     'https://i.cbc.ca/1.6236104.1696526568!/cumulusImage/httpImage/image.jpg_gen/derivatives/16x9_780/money-coins.jpg', 
     'inequality_image.jpg'),
    ('https://travelaway.me/best-ways-explore-new-york-city/', 
     'https://mldvwwasb8tu.i.optimole.com/cb:esbD~6200b/w:896/h:596/q:90/f:best/ig:avif/https://travelaway.me/wp-content/uploads/2017/08/NYC-aerial-view.jpg', 
     'nyc_skyline.jpg')
]

excel_urls = [
    ('https://www.lenmed.co.za/heart-failure-signs-and-symptoms/',
     'https://www.lenmed.co.za/wp-content/uploads/pulse-rate-line-in-heart-shape-on-green-background-vector-31540955-e1671437287410-945x400.jpeg',
     'heart.jpg'),
    ('https://www.newcastle.edu.au/degrees/master-of-construction-management-professional',
     'https://www.newcastle.edu.au/__data/assets/image/0011/963029/Master-Construction-Management-program-header.jpg',
     'construction.jpg')
]

python_urls = [
    ('https://www.facultyfocus.com/articles/effective-classroom-management/using-playing-cards-to-encourage-student-participation-and-engagement/', 
     'https://cdn-jagbh.nitrocdn.com/TYVZHePxisufUuSiVWDElscksnaOxEbE/assets/images/source/rev-88ad360/s39613.pcdn.co/wp-content/uploads/2022/01/playing-cards-poker-cards-in-the-hand-of-a-young-man-picture-id1131822944.jpg', 
     'cards.jpg'),
    ('https://translation-agency-poland.com/polish-website-translations/', 
     'https://translation-agency-poland.com/wp-content/uploads/2017/11/Polish-Translations-ANGOS-Translation-Agency-Krak%C3%B3w.jpg', 
     'polish.jpg'),
    ('https://writingcooperative.com/why-writing-out-a-dictionary-will-instantly-improve-your-work-d9f5878d34e3', 
     'https://miro.medium.com/v2/resize:fit:1400/format:webp/0*-ATQ3-hGyZxfZqmo', 
     'dictionary.jpg'),
    ('https://oxylabs.io/blog/python-web-scraping', 
     'https://oxylabs.io/_next/image?url=https%3A%2F%2Foxylabs.io%2Foxylabs-web%2FZpBxdR5LeNNTxEtH_ZDIwODc5ZDQtNmNlNC00NjVmLTg0ZmQtZDBjN2IzYTExOTVl_oxylabs-images-05.jpeg%3Fauto%3Dformat%2Ccompress&w=2048&q=75', 
     'web_scrape.jpg'),
    ('https://gcore.com/blog/cloud-services-for-fintech/', 
     'https://assets.gcore.pro/blog/cloud-services-for-fintech/1644246923.png', 
     'sql.jpg')
]

for web_url, image_url, file in sql_urls:
    soup = get_webpage(web_url)
    download_image(image_url, file)

for web_url, image_url, file in excel_urls:
    soup = get_webpage(web_url)
    download_image(image_url, file)

for web_url, image_url, file in python_urls:
    soup = get_webpage(web_url)
    download_image(image_url, file)
