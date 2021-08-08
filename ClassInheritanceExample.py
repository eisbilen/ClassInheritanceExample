import pandas as pd
import random
import json
import requests
import os
from datetime import datetime

from bs4 import BeautifulSoup

import re


PATH = ""
FILE_NAME_01 = "data_by_artists.csv"
FILE_NAME_02 = "data_by_genres.csv"


class CSVGetInfo:
    """ This class displays the summary of the tabular data contained in a CSV file """
    instance_count = 0

    # Initializer / Instance Attributes
    def __init__(self, path, file_name):
        CSVGetInfo.increase_instance_count()
        self.path = path
        self.file_name = file_name
        print("CSVGetInfo class object has been instantiated")

    # Instance Method
    def display_summary(self):
        data = pd.read_csv(self.path + self.file_name)
        print(self.file_name)
        print(data.head(self.generate_random_number(10)))
        print(data.info())
        return data

    # Class Method
    @classmethod
    def increase_instance_count(cls):
        cls.instance_count += 1
        print(cls.instance_count)

    @classmethod
    def read_file_1(cls):
        return cls("", "data_by_artists.csv")
    
    @classmethod
    def read_file_2(cls):
        return cls("", "data_by_genres.csv")

    # Static Methods
    @staticmethod
    def generate_random_number(limit):
        return random.randint(1, limit)


class CSVGetDetails(CSVGetInfo):
    """ This class displays the summary of a column in a tabular data contained in a CSV file """

    def __init__(self, path, file_name, column_name):
        CSVGetInfo.__init__(self, path, file_name)
        self.column_name = column_name
        print("CSVGetDetail class object has been instantiated")

    # Instance Method
    def display_column_summary(self):
        data = self.display_summary()
        print(data[self.column_name].describe())

    @classmethod
    def read_file_1(cls, column_name):
        return cls("", "data_by_artists.csv", column_name)

if __name__ == '__main__':

    data = CSVGetDetails.read_file_1("danceability")    
    data.display_column_summary()


    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    print(page)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    job_elements = results.find_all("div", class_="card-content")

    #open file
    file = open("/data/Python.txt", "w")
    
    #convert variable to string
    str = repr(job_elements)
    file.write(str)
    
    #close file
    file.close()

    print(os.getcwd())
    print('file saved')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

    articleLinks = set()
    dataAll = []

    def getArticleLinks(tag, page):
        url = f'https://www.trtworld.com/{tag}?page={page}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        articleLinks = {'https://www.trtworld.com' + a['href'] for a in soup.find_all('a', {'class': 'gtm-topic-latest-article'})}

        for articleLink in articleLinks:
            r = requests.get(articleLink, headers=headers)
            item = BeautifulSoup(r.text, 'html.parser')
            content = item.find("div", {"class":"contentBox bg-w noMedia"})

            if content:
                content = content.findAll('p')
                data = {'tag': tag,
                        'datetime': datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),  
                        'title': item.find('h1', {'class': 'article-title'}).text,
                        'website': 'trtworld',
                        'link': url,
                        'article': [p.text for p in content]}
                print(data)
                dataAll.append(data)

        with open('/data/articles_'+datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.json', 'w') as outfile:
            json.dump(dataAll, outfile)

        return

    getArticleLinks('Sport', 1)