import re
import sys


class Panda(object):
    """docstring for Panda"""
    def __init__(self, name, mail, gender):
        super(Panda, self).__init__()
        self.name = name
        self.mail = mail
        self.gender = gender
        self.__verify_mail()

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.mail, self.gender)

    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.mail, self.gender)

    def __eq__(self, other):
        if self.__hash__() == other:
            return True

    def __hash__(self):
        return hash(self.__str__()) % ((sys.maxsize + 1) * 2)  # return always positive hash int

    def __verify_mail(self):
        find = re.compile('([\w_.\-]+[@]+[\w{2,10}]+[.]+[a-zA-Z]{2,5})')
        if len(find.findall(self.mail)) == 0:
            raise Exception("You have provided invalid email adress...")

    def isMale(self):
        return True if self.gender == 'Male' else False

    def isFemale(self):
        return True if self.gender == 'Female' else False
