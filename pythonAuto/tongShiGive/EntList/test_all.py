#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
import os, time, smtplib, unittest
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 导入自定义库
from global_config import *
from EntList.test_ent_listPro import TestEntListPro

def run():
    # 定义test_suite
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestEntListPro)
    suite = unittest.TestSuite([suite1])
    # 执行test_suite
    # result = unittest.TextTestRunner(verbosity=2).run(suite)

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # 定义测试结果文件存放路径
    filename = REPORT_PATH + now + 'result.html'
    # 打开测试结果文件
    fp = open(filename, 'wb')
    # 执行test_suite并将结果保存到测试结果文件中
    runner = HTMLTestRunner(stream=fp,
                            title=u"3.0接口测试",
                            description=u"用例执行情况:")
    runner.run(suite)
    # 关闭测试结果文件
    fp.close()
    # 找最新生成的测试文件
    report_file_new = find_new_report(REPORT_PATH)
    # 发送邮件
    send_mail(report_file_new)

def send_mail(new_report_file):
    # 读取测试结果文件
    file = open(new_report_file, 'rb')
    mail_body = file.read()
    file.close()

    # msg = MIMEText(mail_body, 'html', 'utf-8')
    # msg['Subject'] = Header("3.0接口自动化测试", 'utf-8')

    msg = MIMEMultipart('related')
    # 邮件标题
    msg['Subject'] = Header("3.0接口自动化测试", 'utf-8')
    # 邮件正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(text)
    # 邮件附件
    att = MIMEText(open(new_report_file, 'rb').read(), 'base64', 'gbk')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', new_report_file))
    msg.attach(att)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(MAIL_SERVER)
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
    smtp.sendmail(MAIL_SENTER, MAIL_RECEIVER, msg.as_string())
    smtp.quit()
    print "email has sent out!"

def find_new_report(report_path):
    filename_list = os.listdir(report_path)
    filename_list.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn))
    report_file_new = os.path.join(report_path, filename_list[-1])
    return report_file_new

if __name__ == '__main__':
    run()