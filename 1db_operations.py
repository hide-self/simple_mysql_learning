import pymysql

# 连接MySQL(底层用的是socket)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')

cursor = conn.cursor()

# cursor.execute('命令')可以利用python代向命令行发出命令，其中的命令之后可以加分号也可以不加分号

# 1、查看数据库
cursor.execute('show databases')
# 获取指令结果
result = cursor.fetchall()
print(result)  # 打印结果：(('day26db',), ('information_schema',), ('mysql',), ('performance_schema',), ('sys',))

# 2、创建数据库
# 发送指令
cursor.execute('create database db03 default charset utf8 collate utf8_general_ci')  # 若创建数据库名字已存在，则报错
conn.commit()
# 在执行查询后通常要接上cursor.fetchall()来获取查询数据
# 在执行创建数据库或者增删改查数据库数据后，通常要接上conn.commit()来确保执行

# 3、创建数据库之后，查看数据库
cursor.execute('show databases')
# 获取指令结果
result = cursor.fetchall()
print(result)

# 4、删除数据库
# 发送指令
cursor.execute('drop database db03')
conn.commit()

# 5、进入数据库，查看表
cursor.execute('use mysql')
cursor.execute('show tables')
result = cursor.fetchall()
print(result)

# 关闭连接
cursor.close()
conn.close()
