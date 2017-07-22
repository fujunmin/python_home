import unittest
import  time
"""
1.执行顺序是start-执行测试用例test01-end；test02也是如此
2.执行顺序是先执行setUp，然执行test*开头的用例，最后是后置tearDown
3.addtest没执行，说明只执行test开头的用例

"""


class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        time.sleep(1)
        print('end')
    def test02(self):
        print('执行测试用例test01')
    def test01(self):
        print('执行测试用例test02')
    def addtest(self):
        print('执行测试用例add方法')

if __name__=='__main__':
    unittest.main()