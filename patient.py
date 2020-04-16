class Patient:
    def __init__(self, social, dob, hia, first_name, last_name, address):
        self.__social = social
        self.__dob = dob
        self.__hia = hia
        self.address = address
        self.full_name = f'{first_name} {last_name}'

    @property
    def social(self):
        try:
            return self.__social
        except AttributeError:
            return 0

    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return 0

    
    @property
    def hia(self):
        try:
            return self.__hia
        except AttributeError:
            return 0

    def first_name(self):
        return "None"
    
    def last_name(self):
        return "None"


patient1 = Patient("111-11-1111", "09/24/1989", "1234567890", "Dave", "Thomas", "111 1st Street")
print(patient1)
print(patient1.social)
print(patient1.full_name)
print(patient1.dob)

patient1.first_name = "Tiffany"
patient1.social = "222-22-2222"
patient1.dob = "01/01/1901"

print(patient1.first_name)
print(patient1.last_name)