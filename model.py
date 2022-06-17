import re as regex


class Model:
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        """
        Validate weight
        :param value:
        :return: 
        """
        pattern = r'^\d*[.,]?\d*$'
        if regex.fullmatch(pattern, value):
            self.__weight = value
        else:
            raise ValueError(f'Invalid entry!')

    def save(self):
        """
        Save the weight to database
        :return:
        """
        with open("data.txt", "a") as file:
            file.write(self.weight + '\n')
