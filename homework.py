from datetime import datetime
from time import sleep
import requests
import selectorlib

URL = 'https://programmer100.pythonanywhere.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the tour data from the given URL."""
    response = requests.get(url, HEADERS)
    source = response.text
    return source

def extract( source ):
    extractor = selectorlib.Extractor.from_yaml_file( 'extractor_hwrk.yaml' )
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    pass

def store( extracted ):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('data_temperature.txt', 'a') as file:
        text_input = f"{current_time},{extracted}\n"
        file.write( text_input )

def read( extracted ):
    with open('data_temperature.txt', 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    while True:
        scrape_response = scrape(URL)
        extracted_data = extract(scrape_response)
        print( extracted_data )
        store( extracted_data )

        sleep(10)  # Sleep for 1 hour