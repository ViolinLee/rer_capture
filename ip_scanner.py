import argparse
from urllib import request
from lxml.html import parse
from bs4 import BeautifulSoup
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('prefix', type=str)
args = parser.parse_args()


if __name__ == "__main__":
    print('Scanning...')
    prefix = args.prefix + '.'
    for i in tqdm(reversed(range(0, 256))):
        target_url = 'http://' + prefix + str(i) + ':8000/api/vis'
        try:
            response = request.urlopen(target_url, timeout=0.8)
            html = response.read()
            soup = BeautifulSoup(html, 'lxml')
            title = soup.title

            if "Flask Shou Image" in title:
                print(target_utl)
        except:
            pass


