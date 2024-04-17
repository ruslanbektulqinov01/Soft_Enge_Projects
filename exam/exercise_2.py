class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__password = ""

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


user = User("John", "Doe")
user.set_password("12345678")
print(user.get_password())









