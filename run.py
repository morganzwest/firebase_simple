import database_fire

a = database_fire.db("https://test1-2117c.firebaseio.com/", "key.json")
a.update("/", {"dog1": 5, "cat1": 9})