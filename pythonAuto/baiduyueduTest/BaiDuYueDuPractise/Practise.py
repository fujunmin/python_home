import random
from datetime import *
now_date = date.today() #获取当前日期
now_time = datetime.now() #获取当前时间
yesterday = date.today() - timedelta(1)  #减去一天，是昨天
day = date.today() + timedelta(2)  #加上一天，是后天
print(now_date, now_time)
print(yesterday, day)






#写文件
f=open('/E:/text.txt','w')  #以写入的方式打开文件
f.write('Hello, world!')  #写入内容到文件中
f.close()  #关闭文件
#读文件
f=open('/E:/text.txt','r') #以只读的方式打开we年
f.read()  #读取文件的内容
f.close()




#随机数
# a=random.random()  #生成一个0到1的随机浮点数
# b=random.randint(1,100)  #桑鞥脑恒一个指定范围内的随机数
# #c=random.randrange() #按指定基数递增的集合中获取一个随机数
# #可以用来生成一个随机的电话号码
# m= random.randint(13500000000, 13599999999)
# #根据某个数据或者字符串随机选一个名字
# n = random.randint('张三', '李四', '王五', '赵六')
# print(a, b, m, n)




# #字典的用法
# kathy = {'hobby': 'game', 'color': 'blue'}
# for k, v in kathy.items():
#     print(k, v)
# #序列的用法
# for i,v in enumerate(['Kathy', 'love', 'Smark']):
#     print(i,v)

#多个序列循环
questions = ['name', 'hobby', 'color']
answers = ['Kathy', 'love', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? It is {1}')
