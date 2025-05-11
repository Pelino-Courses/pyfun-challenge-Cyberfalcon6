class Person:
    """This is the class that contains attributes of all person objec
    that we will have in our university system. some other classes will inherit it.
    """
    def __init__(self, person_name, person_age, person_sex):
        self.person_name = person_name
        self.person_age = person_age
        self.person_sex = person_sex
