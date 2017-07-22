# 版本
v1.0

# 目录结构
-apitest #根目录
	-com #接口方法，根据3.0API手册封装
		-EntList.py #企业名录
		-EntQuery.py #企业信息查询
		-EntPerQuery.py #企业人员查询
		-PerVerify.py #人员核验
		-constants.py #常量文件
	-lib #公共方法，根据第三方插件封装
		-rest.py #http request
		-dboracle #cx_Oracle
	-EntList #企业名录测试模块，其它模块文件类似
		-test_*.py #测试case
		-test_all.py #测试suite，组织各自模块测试case
	-global_config.py #配置文件
	-test_all.py #测试suite，组织全部模块测试case
	-readme.txt #说明文档

# 编写规范
1.在com中封装接口，创建文件名称应明确产品分类，在文件内根据API手册封装产品接口方法
2.在lib中封装公共方法
3.根目录apitest下创建各产品模块文件目录，在此目录下编写测试case，并在test_all下进行用例组织
4.根目录apitest下test_all文件负责组织全部模块测试case