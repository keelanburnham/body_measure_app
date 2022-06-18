from contextlib import closing
import re as regex
from database import connect_to_db


class Model:
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        pattern = r'^\d*[.]?\d*$'
        if regex.fullmatch(pattern, value):
            self.__weight = value
        else:
            raise ValueError(f'Invalid entry!')

    def save(self):
        with closing(connect_to_db('measurements')) as connection:
            with closing(connection.cursor()) as cursor:
                try:
                    cursor.execute(
                        f'INSERT INTO body_measurements (weight) VALUES ({self.weight});')
                    print('Save successful!')
                except Exception as error:
                    print('Unable to save weight!')
