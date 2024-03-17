"""
This module scrapes concert information from the Bowery Presents website, 
including band names, dates, and locations. It then processes this information 
to create a structured list of concert events.
"""
import requests
from bs4 import BeautifulSoup

def scrape_concerts(url):
    """
    Scape concert information from the given URL.

    Parameters:
    - url (str): The URL of the website to scrape for concert information.

    Returns:
    - list of dict: A list of dictionaries, each containing the name,
      date, and location of a concert.
    """
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Assuming concerts are listed in <div class="concert-info">
    # <div class="event-information-wrapper">
    # (This will vary based on actual website structure)
    # concert_dates = soup.find_all('h3', class_='calendar-day-title')
    # for concert_date in concert_dates:
    e = 0
    
    concert_dates = soup.find_all('li',class_='calendar-day')
    print("concert dates length=" + str(len(concert_dates)))
    for concert_date in concert_dates:
        calendar_day = concert_date.find('h3', class_='calendar-day-title').string
        print(calendar_day)
        concerts = concert_date.find_all('div', class_='event-information-wrapper')
        for concert in concerts:
            headliner = concert.find('h4', class_="event-headliner event-text").text
            support = concert.find('h5', class_="event-support event-text").text
            venue = concert.find('p', class_="event-venue event-text").text
            print(headliner)
            print(support)
            print(venue)
            e += 1
            print(e)
        print("NEXT")
    return concert_dates

# Example URL, replace with the actual Bowery Presents schedule page
CONCERTS_URL = 'https://www.bowerypresents.com/calendar/'
concert_list = scrape_concerts(CONCERTS_URL)
# updated to commit changes
