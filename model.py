import sqlite3

# 操作数据库
class Database:
    def CreateDatabase(self):
        self.conn = sqlite3.connect('data.db')
        # 创建一个Cursor
        self.cursor = self.conn.cursor()
        # 执行一条SQL语句，创建user表
        # self.cursor.execute('create  table  patientinfo (id int(10)  primary key,\
        #     name varchar(20), sex varchar(20), age varchar(20), weight varchar(20), illness varchar(80))')
        self.cursor.execute('create  table  userinfo (id int(10)  primary key,\
                    name varchar(20), username varchar(20), password varchar(20))')
        # 关闭游标
        self.cursor.close()
        # 关闭Connection
        self.conn.close()
    def AddUserInfo(self,name):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(name)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
    def SearchInfo(self,name):
        self.conn = sqlite3.connect('data.db')
        # 创建一个Cursor
        self.cursor = self.conn.cursor()
        # 执行一条SQL语句，插入一条记录
        self.cursor.execute(name)
        # self.cursor.execute('select * from userinfo')
        result = self.cursor.fetchall()
        # 关闭游标
        self.cursor.close()
        # 提交事务
        self.conn.commit()
        # 关闭Connection
        self.conn.close()

        return result