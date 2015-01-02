import requests
from bs4 import BeautifulSoup

global city
city = "none"

def parse_results(search_terms):
    if city == "none":
        print("ERROR: No city found!")
        return []
    BASE_URL = "http://"+city+".craigslist.org/search/tia?query="
    results = []
    search_terms = search_terms.strip().replace(' ', '+')
    response = requests.get(BASE_URL+search_terms)
    print(BASE_URL+search_terms)
    soup = BeautifulSoup(response.content)
    for listing in soup.find('div', 'content').find_all('p', 'row'):
        if listing.find('span', 'price') == None:
            price = "Unk"
        else:
            price = listing.find('span', 'price').get_text()
        print(price)
        create_date = listing.find('time').get_text()
        event = listing.find('a', 'hdrlnk').get_text()
        results.append({'price': price, 'create_date': create_date, 'event': event})
    return results

def set_city(city_name):
    global city
    city = city_name;

if __name__ == '__main__':
    #example code
    set_city("denver")
    #uses Phish for example because Phish are always playing in Denver ;)
    results = parse_results("phish")
    for i in results:
        print(i)
