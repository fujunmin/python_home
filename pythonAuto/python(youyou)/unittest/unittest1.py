import unittest
import  time
# python接口自动化book third chapter  unittest  practise
"""今天踩了一个坑，为什么有时候执行一个函数，有时候执行多个函数呢，原来光标放在哪里，右键执行的时候，就只执行哪个函数；只有放在
main函数那里才会执行所有的函数"""


# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):  ## test method names begin 'test'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#         print('testAdd')
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#         print('testMultiply')

#测试加法和乘法

class Test(unittest.TestCase):
#前置和后置都是非必要的条件，如果没有也可以写pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testMinus(self):
        u'''这里是测试减法'''
        result=6-5
        hope =1
        self.assertEqual(result,hope)
        print('测试减法')

    def testDrive(self):
        u'''这里是测试除法'''
        result =7/2
        hope = 3.5
        self.assertEqual(result,hope)
        print('测试除法')
if __name__=='__main__':
    unittest.main()