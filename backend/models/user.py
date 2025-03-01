from bson.objectid import ObjectId
from enum import Enum


class AccountState(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class User:

    COLLECTION = 'Users'

    def __init__(self, user_id, name, email, password, age=0, is_student=True,account_state=AccountState.ACTIVE):
        self.user_id = user_id if user_id else str(ObjectId())
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.is_student = is_student
        self.account_state = account_state

    def to_dict(self):
    #Convert the User object to a dictionary for MongoDB storage
        return {
            "_id": ObjectId(self.user_id) if isinstance(self.user_id, str) else self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "is_student": self.is_student,
            "account_state": self.account_state.value if isinstance(self.account_state, AccountState) else self.account_state
        }

    def save(self, db):
        #Save the user to MongoDB
        user_dict = self.to_dict()

        result = db.db[self.COLLECTION].insert_one(user_dict)
        self.user_id = str(result.inserted_id)
        
        return self.user_id


