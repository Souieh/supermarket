import bcrypt
from .database import Database


class User:
    @staticmethod
    def create_user(username, password, role="admin"):
        db = Database()
        collection = db.get_collection("users")

        if collection.find_one({"username": username}):
            return False, "اسم المستخدم موجود مسبقاً"

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {
            "username": username,
            "password": hashed_pw,
            "role": role
        }
        collection.insert_one(user_data)
        return True, "تم إنشاء المستخدم بنجاح"

    @staticmethod
    def delete_user(username):
        db = Database()
        collection = db.get_collection("users")
        return collection.delete_one({"username": username})

    @staticmethod
    def get_all_users():
        db = Database()
        collection = db.get_collection("users")
        return list(collection.find({}, {"password": 0}))

    @staticmethod
    def authenticate(username, password):
        db = Database()
        collection = db.get_collection("users")
        if collection is None:
            return False, "قاعدة البيانات غير متصلة"

        user = collection.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            return True, user["role"]

        return False, "اسم المستخدم أو كلمة المرور غير صحيحة"
