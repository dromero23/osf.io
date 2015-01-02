from modularodm import fields
from framework.mongo import StoredObject


class Subscription(StoredObject):
    _id = fields.StringField(primary=True)
    event_name = fields.StringField()
    # types = {
    #   'email':  [User1, User2],
    #       ...
    # }
    types = fields.DictionaryField()

