# -*- coding: utf-8 -*- 
#__author__='fanweiming'
#__time__ ='2018/4/19 10:21'

import unittest

from app.hello import get_task_sta


class myTestCase1(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_sta(self):
        get_task_sta()

    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()
