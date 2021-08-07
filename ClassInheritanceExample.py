import pandas as pd
import random
import requests

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

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")


    job_elements = results.find_all("div", class_="card-content")

    for job_element in job_elements:
        print(job_element, end="\n"*2)
    
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element)
        print(company_element)
        print(location_element)
        print()