import firebase_admin
from firebase_admin import credentials, db
import hashlib, uuid

class database(object):
    def __init__(self, url: str, key_path: str):
        self.hashed_password = ''  # Default
        self.old = ''
        self.new_pass = ''
        self.url = url

        # get the authorization key
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred, {

            "databaseURL": self.url

        })


    def hash_password(self, password: str):
        salt = self.uuid.uuid4().hex  # hex:bin represent
        # encode it to hashed hex
        return self.hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, hashed_password: str, user_password: str):
        # splits the salt so the decrypt can find the original
        password, salt = hashed_password.split(':')
        return password == self.hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def save(self, ref: str, dict_output, ret = False):
        self.current_db_ref = db.reference(ref)
        _t = self.current_db_ref.push(dict_output)

    def load(self, path = "/"):
        return db.reference(path)

    def update(self, path: str, dict_update):
        ref = db.reference(path)
        ref.update(dict_update)