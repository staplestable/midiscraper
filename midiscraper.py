import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class MIDIScraper:

    def __init__(self, url, directory='dataset', limit=5):
        self.url = url
        self.directory = directory
        self.limit = limit
        self.__check_dir()
        self.__get_midi()

    def __check_dir(self):
        if not (os.path.isdir(self.directory)):
            print("Directory doesn't exist... creating a new one.")
            os.mkdir(self.directory)

    def __get_midi(self):
        # HTTP Request
        response = requests.get(self.url)
        status = response.status_code

        # Get base URL
        base_url = self.url
        ending = '.com'

        if ('kunstderfuge' in self.url) or ('midiworld' in self.url):
            ending = '.com'
        elif 'jsbach' in self.url:
            ending = '.net/midi/'
        else:
            print('WARNING: Chosen website is not currently supported but we\'ll try anyway.')

        while not base_url.endswith(ending):
            base_url = base_url[:-1]

        print('''
Web scraping the following page: '{url}'
Calculated base URL: '{base_url}'
Status code: {status}
        '''.format(url=self.url, base_url=base_url, status=status))

        # Souping
        content = response.content
        parser = BeautifulSoup(content, features='html.parser')
        body = parser.body
        i = 0 

        # Getting MIDI files
        for link in body.find_all('a'):
            href = link.get('href')
            if href is not None and '.mid' in href:
                url = urljoin(base_url, href)
                response = requests.get(url)
                status = response.status_code
                filename = os.path.basename(urlparse(url).path)
                print(os.path.join(self.directory, filename))
                
                if status == 200:
                    if os.path.isfile(os.path.join(self.directory, filename)):
                        continue
                    try:
                        with open(os.path.join(self.directory, filename), 'wb') as file:
                            file.write(response.content)
                    except:
                        print(f'File \'{filename}\' is corrupted or currently in use.')

                else:
                    print(f'Failed to download \'{filename}\' file.')
                i += 1
            if self.limit != 0 and i == self.limit:
                print("Sucessfully downloaded requested files.")
                exit()
                
        print("Sucessfully downloaded requested files.")