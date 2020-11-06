# main.py

from .packages import *
from .classes import *
from .helpers import *

def get_page(url: str):
    try:
        request = requests.get(url)

        # Any response other than 200 - unsatisfactory
        if not request.status_code == 200:
            raise ResponseNot200(request.status_code)
        
        return request.text
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL #return "Error: {}".format(e)
        raise e
 

def search_spider(query:str, max_titles:int=6, max_pages:int=1):
    page = 1
    search_results = []
    while page <= max_pages:
        # Compose url for search and request that page
        url = 'https://rezka.ag/index.php?do=search&subaction=search&q=' + query + '&page=' + str(page)
        plain_page = get_page(url)

        # Convert to soup object
        soup = BeautifulSoup(plain_page, 'lxml')

        # Loop through matching titles
        for title in islice(soup.findAll('div', {'class':'b-content__inline_item-link'}), max_titles):
            # Gather the title's short info
            title_info = {
                "name": title.a.text,
                "sub_info": title.div.text,
                "link": title.a.get('href')
            }
            # Populate the search results array with titles
            search_results.append(title_info)

        page += 1 # Continue cycling through pages
    
    return search_results

def schedule_spider(url:str):

    # Request series' page
    plain_page = get_page(url)
    # Convert to soup object
    soup = BeautifulSoup(plain_page, 'lxml')

    # Try to find schedule table, if not - rise error
    table = soup.find('div', {'class':'b-post__schedule_block'})
    if not table:
        raise NoScheduleFound
    
    # Find schedule title and raw schedule table's rows
    schedule_title = table.find('div', {'class':'b-post__schedule_block_title'}).find('div', {'class':'title'}).text
    raw_schedule = reversed((table.findAll(is_informational_tr)))

    # Initialize the title's schedule object
    schedule = {
        "schedule_title": schedule_title,
        "episodes": [],
    }
    schedule = Schedule(schedule_title, [])
    for episode in raw_schedule:
        sections = episode.findAll('td')
        episode_object = Episode(sections[0].text, sections[1].text, sections[3].text)
        schedule.addEpisode(episode_object)

    return schedule

# schedule_spider('https://rezka.ag/series/drama/36116-follovery-2020.html')