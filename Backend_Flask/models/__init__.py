#!/usr/bin/python3
"""
initialize the models package
"""


from models.engine.db_storage import Database
storage = Database()
storage.reload()
