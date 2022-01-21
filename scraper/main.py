from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    html = urlopen('https://abcnews.go.com/Health/Coronavirus')
    bs = BeautifulSoup(html, "html.parser")
    links = bs.findAll('a', attrs={'class': 'AnchorLink News__Item external flex flex-row'})

    for x in links:
        print(x.get('href'))
        html = urlopen(x.get('href'))
        bs = BeautifulSoup(html, "html.parser")

        for data in bs(['style', 'script']):
            data.decompose()

        text = ''.join(bs.stripped_strings)

        regex2 = 'https://'
        pattern2 = re.compile(regex2)

        fileName = x.get('href')
        fileArray = re.sub(pattern2, "", fileName).split('/')
        fileName = fileArray.__getitem__(len(fileArray) - 1)
        fileName += '.txt'

        try:
            with open(fileName, 'w', encoding='utf-8') as fp:
                fp.write(text)
        except:
            print(fileArray, " LOPKA")
            fileName = fileArray.__getitem__(len(fileArray) - 2)
            fileName += '.txt'
            print(fileName)
            with open(fileName, 'w', encoding='utf-8') as fp:
                fp.write(text)
