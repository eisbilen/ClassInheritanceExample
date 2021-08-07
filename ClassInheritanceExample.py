import pandas as pd
import random
import requests
import os

from bs4 import BeautifulSoup

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

    questionlist = []

    def getQuestions(tag, page):
        url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=Active&page={page}&pagesize=50'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        questions = soup.find_all('div', {'class': 'question-summary'})
        for item in questions:
            question = {
            'tag': tag,    
            'title': item.find('a', {'class': 'question-hyperlink'}).text,
            'link': 'https://stackoverflow.com' + item.find('a', {'class': 'question-hyperlink'})['href'],
            'votes': int(item.find('span', {'class': 'vote-count-post'}).text),
            'date': item.find('span', {'class': 'relativetime'})['title'],
            }
            questionlist.append(question)
        return

    for x in range(1,3):
        getQuestions('python', x)
        getQuestions('flask', x)

    df = pd.DataFrame(questionlist)
    df.to_excel('/data/stackquestions.xlsx', index=False)
    print('Fin.')