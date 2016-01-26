import re


class Panda:
    def __init__(self, name, mail, gender):
        self.__name = name
        self.__mail = mail
        self.__gender = gender
        self.__verify_mail()

    def name(self):
        return self.__name

    def email(self):
        return self.__mail

    def gender(self):
        return self.__gender

    def __str__(self):
        return "{}, {}, {}".format(self.__name, self.__mail, self.__gender)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.__str__())

    def __verify_mail(self):
        find = re.compile('([\w_.\-]+[@]+[\w{2,10}]+[.]+[a-zA-Z]{2,5})')
        if len(find.findall(self.email())) == 0:
            raise Exception("You have provided invalid mail adress...")

    def isMale(self):
        return self.__gender == 'male'

    def isFemale(self):
        return self.__gender == 'female'

    def panda_dict(self):
        return str(self.__dict__)
