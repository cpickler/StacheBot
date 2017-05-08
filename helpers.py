import os
from pymongo import MongoClient

mongo = MongoClient(os.environ['MONGODB_URI'])
db = getattr(mongo, os.environ['MONGODB_NAME'])


def config(server, option):
    """
    Read from the config document for a specific option
    :param option: string
    :param server: server id string
    :return: value set to option
    """
    cursor = getattr(db, server).find_one({'field': 'config'})
    value = cursor['config'][option]
    return value

