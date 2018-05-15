# -*- coding: utf-8 -*- 
#__author__='fanweiming'
#__time__ ='2018/4/19 9:29'

import unittest

from app.dataBase import MyDataBase


class myTestCase(unittest.TestCase):
    def setUp(self):
        self.data_base=MyDataBase("test_data_base1","test_data_table1")

    def test_case(self):
        a=self.data_base.create_table()
        test_sentence='''
    CREATE TABLE IF NOT EXISTS test_data_table1( 
    Id       INTEGER    PRIMARY KEY AUTOINCREMENT,
    total    int        NOT NULL,
    sucess   int        NOT NULL,
    fail     int        NOT NULL);
        '''
        self.assertEqual(a,test_sentence)

    def tearDown(self):
        pass


if  __name__=="__main__":
    unittest.main()


