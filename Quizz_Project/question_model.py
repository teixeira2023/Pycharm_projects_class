class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username


user_1 = User("001", "Alan")
# user_1.id = "001"
# user_1.username = "Alan"

print(user_1.id)
#
user_2 = User("002","Janete")
# # user_2.id = "002"
# # user_2.username = "Janete"
#
print(user_2.id, user_2.username)
