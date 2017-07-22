# coding:utf-8
import unittest
# import  time
import requests
# """
# GET /index-ajaxselectcourierinfo-1202247993797-yunda.html HTTP/1.1
# GET /index-ajaxselectcourierinfo-560697415000-tiantian.html HTTP/1.1
# "User-Agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 59.0.3071.86Safari / 537.36",
# "X - Requested - With": "XMLHttpRequest"
# "Accept-Encoding": "gzip, deflate",
# "Accept": "*/*",
# "Accept-Language": "zh-CN,zh;q = 0.8,en-US;q = 0.6,en;q = 0.4",
# """
class Test_Kuaidi(unittest.TestCase):
    def SetUp(self):
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
            }
        self.s=requests.session()
    def test_yunda(self):
        danhao='1202247993797'
        kd='yunda'
        # self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html"%(danhao,kd)
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao, kd)
        print(self.url)
        #第一步，发请求
        r=self.s.get(self.url,headers=self.headers,verify=False)
        result=r.json()
        #第二步，获取结果
        print(result['company'])  #获取公司名称
        data = result["data"]
        print(data[0])
        get_result=data[0]['content'] #获取已签收状态
        print(get_result)
            #断言：断言结果和期望结果对比
        self.assertEqual(u"韵达快递",result['company'])
        self.assertIn(u"已签收",get_result)
    def test_tiantian(self):
        danhao='560697415000'
        kd='tiantian'
        #这里对url的单号进行参数化了
        # self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao, kd)
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao, kd)
        print(self.url)
        # 第一步，发请求
        r = self.s.get(self.url,headers=self.headers,verify=False)
        result = r.json()
        # 第二步，获取结果
        print(result['company'])  # 获取公司名称
        data = result["data"]
        print(data[0])
        get_result = data[0]['content']  # 获取已签收状态
        print(get_result)
        # 断言：断言结果和期望结果对比
        self.assertEqual(u"天天快递", result['company'])
        self.assertIn(u"已签收", get_result)

if __name__=='__main__':
    unittest.main()
