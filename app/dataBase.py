# -*- coding: utf-8 -*- 
# __author__='fanweiming'
# __time__ ='2018/4/18 11:44'

import sqlite3

from config import Config


class MyDataBase(object):
    def __init__(self, data_base_name, table_name):
        self.data_base_name = data_base_name
        self.table_name = table_name

    def create_table(self):
        connection = sqlite3.connect(self.data_base_name)
        statement = '''
    CREATE TABLE IF NOT EXISTS {}( 
    Id       INTEGER    PRIMARY KEY AUTOINCREMENT,
    total    int        NOT NULL,
    success   int        NOT NULL,
    fail     int        NOT NULL);
        '''.format(self.table_name)
        try:
            connection.cursor().execute(statement)
        except Exception as e:
            print "you have a Exception during connecting the dataBase!"
        else:
            connection.commit()
        finally:
            connection.close()



def create_table():
    base = MyDataBase(data_base_name=Config.DATA_BASE_NAME, table_name=Config.DATA_BASE_TABLE_NAME)
    base.create_table()


def insert1(total, success, fail):
    cc = sqlite3.connect(Config.DATA_BASE_NAME)
    cs = cc.cursor()
    try:
        cs.execute(r"select * from sqlite_master where type='table' and name=%s" %Config.DATA_BASE_TABLE_NAME)
        record=cs.fetchall()
    except:
        print "error connecting to the database!"
    else:
        if record:
            sentence = "insert into statistics(total,success,fail) values(%d,%d,%d)" % (total, success, fail)
            cs.execute(sentence)
            cc.commit()
    finally:
        cc.close()
