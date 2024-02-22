import requests
from bs4 import BeautifulSoup

def scrape_concerts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Assuming concerts are listed in <div class="concert-info"> (This will vary based on actual website structure)
    concerts = soup.find_all('div', class_='concert-info')
    concert_list = []
    for concert in concerts:
        # Extract necessary information, e.g., band name, date, location. This depends on the website's HTML structure.
        name = concert.find('h2').text
        date = concert.find('span', class_='date').text
        location = concert.find('span', class_='location').text
        concert_list.append({'name': name, 'date': date, 'location': location})
    return concert_list

# Example URL, replace with the actual Bowery Presents schedule page
concerts_url = 'https://example.com/concerts'
concert_list = scrape_concerts(concerts_url)
print(concert_list)
# updated to commit changes