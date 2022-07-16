# Configure database
import sys
import os
class Config():
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(sys._MEIPASS,"database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "LSADKJ038)#*%)@mlasgjdagso3298"