def to_hashmap (l):
    return dict((item['id'], item) for item in l)

class UserDB:
    def __init__(self, entries):
        self.entries = to_hashmap(entries)

    def add(self, user):
        self.entries[user['id']] = user

    def remove(self, userId):
        del self.entries[userId]

    def all(self):
        users = []
        for key, user in self.entries.items():
            users.append(user)

        return users

def create_user_db():
    users = [
        { 'id': '1', 'name': 'Harris' },
        { 'id': '2', 'name': 'Dan Abramov' },
    ]

    return UserDB(users)
