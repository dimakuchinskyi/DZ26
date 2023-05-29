class UserNotFoundError(Exception):
    pass
class User:
    def __init__(self, username):
        self.username = username
class UserDatabase:
    def __init__(self):
        self.users = {}
    def add_user(self, user):
        self.users[user.username] = user
    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise UserNotFoundError(f"User '{username}' not found")
db = UserDatabase()
user1 = User("максік")
user2 = User("діма")
db.add_user(user1)
db.add_user(user2)
try:
    user = db.get_user("максік")
    print(f"Username: {user.username}")
except UserNotFoundError as e:
    print(str(e))

try:
    user = db.get_user("глеп")
    print(f"Username: {user.username}")
except UserNotFoundError as e:
    print(str(e))
