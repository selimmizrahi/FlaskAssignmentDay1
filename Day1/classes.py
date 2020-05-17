import requests
import json
import datetime


class BasePost:
    def __init__(self, post):
        self.userId = post["userId"]
        self.id = post["id"]
        self.title = post["title"]
        self.body = post["body"]


class ExtendedPost(BasePost):

    def __init__(self, post):
        super().__init__(post)
        self.createdAt = str(datetime.datetime.now())


class JsonablePost(ExtendedPost):
    def __init__(self, post):
        super().__init__(post)

    def json_parse(self):
        dict = json.dumps(self.__dict__)
        return dict



posts = {}

def GetData():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    for i in res.json():
        post = JsonablePost(i)
        newpost = json.loads(post.json_parse())
        posts[i["id"]] = newpost



