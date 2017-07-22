#coding:utf-8
import unittest
#coding:utf-8
import unittest

def all_case():
    #待执行用例的目录
    case_dir="D:\\wenjian\\pythonStudy\\pythonAuto\\python(youyou)"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcse
            testcase.addTests(test_case)
    print(testcase)
    print("bbb")
#     return testcase
# if __name__=="__main__":
#     runner = unittest.TextTestResult()
#     runner.run(all_case())

