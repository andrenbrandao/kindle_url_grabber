import requests

from bs4 import BeautifulSoup

with open('book_list', 'r') as f:
    read_data = f.readlines()

with open('formatted_book_list', 'w') as f:
    for line in read_data:
        try:
            f.write(line.split(' ', maxsplit=1)[1]).lstrip()
        except:
            pass

with open('formatted_book_list', 'r') as f:
    read_data = f.readlines()

with open('parseddata', 'w+') as f:
    for title in read_data:
        keywords = '+'.join(title.split(' '))
        url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Ddigital-text&field-keywords={}".format(keywords)
        print("Getting URLs for BOOK: {}".format(title))

        # add header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "lxml")

        links = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})

        f.write('BOOK: {}\n'.format(title))
        for link in links:
            f.write(link.get('href')+ '\n')
        f.write('\n\n')
