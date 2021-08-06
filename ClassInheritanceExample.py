import pandas as pd
import random

PATH = "/Users/erdemisbilen/Lessons/"
FILE_NAME_01 = "data_by_artists.csv"
FILE_NAME_02 = "data_by_genres.csv"

def gNews():
    return True

def cImage():
    return False

class CSVGetInfo:
    """ This class displays the summary of the tabular data contained in a CSV file """
    instance_count = 0

    # Initializer / Instance Attributes
    def __init__(self, path, file_name):
        CSVGetInfo.increase_instance_count()
        self.path = path
        self.file_name = file_name
        print("CSVGetInfo class object has been instantiated")

def cText():
    return 1

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
        return cls("/Users/erdemisbilen/Lessons/", "data_by_artists.csv")
    
    @classmethod
    def read_file_2(cls):
        return cls("/Users/erdemisbilen/Lessons/", "data_by_genres.csv")

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
        return cls("/Users/erdemisbilen/Lessons/", "data_by_artists.csv", column_name)

if __name__ == '__main__':

    data = CSVGetDetails.read_file_1("danceability")    
    data.display_column_summary()
