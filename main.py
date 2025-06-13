from time import sleep
import requests
import selectorlib

URL = 'https://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the tour data from the given URL."""
    response = requests.get(url, HEADERS)
    source = response.text
    return source

def extract( source ):
    extractor = selectorlib.Extractor.from_yaml_file( 'extractor.yaml' )
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    pass

def store( extracted ):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n')

def read( extracted ):
    with open('data.txt', 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    while True:
        scrape_response = scrape(URL)
        extracted_data = extract(scrape_response)
        print( extracted_data )
        
        content = read(extracted_data)
        if extracted_data.lower() != 'No upcoming tours'.lower():
            if extracted_data not in content:
                store(extracted_data)
                print("Sending email...")
                send_email()

        sleep(10)  # Sleep for 1 hour