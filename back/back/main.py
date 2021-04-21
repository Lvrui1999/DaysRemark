import asyncio
import websockets
import pymysql as sql
import time
# 检测客户端权限，用户名密码通过才能退出循环
async def check_permit(websocket):
    while True:
        recv_str = await websocket.recv()
        cred_dict = recv_str.split(":")
        if cred_dict[0] == "regi": #注册验证
            print("regi" + cred_dict[1])
            db = sql.connect("119.3.164.126","DB_USER47","DB_USER47@123","user47db" )
            cursor = db.cursor()
            cursor.execute('select * from user_password where uname = "' + cred_dict[1] + '"')
            data = cursor.fetchone()
            print(data)
            if data == None:
                cursor.execute('insert into user_password (uname,pword) values ("' + cred_dict[1] + '","' + cred_dict[2] + '")')
                cursor.execute('insert into user_data (uname) values ("' + cred_dict[1] + '")')
                db.commit()
                data = cursor.fetchone()
                print(data)
                db.close()
                response_str = "congratulation, you have regi"
                await websocket.send(response_str)
                return True
            else:
                db.close()
                response_str = "fail, you have regi"
                await websocket.send(response_str)

        if cred_dict[0] == 'log': #登录验证
            db = sql.connect("119.3.164.126","DB_USER47","DB_USER47@123","user47db" )
            cursor = db.cursor()
            cursor.execute('select * from user_password where uname = "' + cred_dict[1] + '"and pword = "'+ cred_dict[2] + '"')
            data = cursor.fetchone()
            db.close()
            print(data)
            if data != None:
                print("right " + cred_dict[1])
                response_str = "congratulation, you have connect with server\r\nnow, you can do something else"
                await websocket.send(response_str)
                return True
            else:
                print("fail " + cred_dict[1])
                response_str = "sorry, the username or password is wrong, please submit again"
                await websocket.send(response_str)

class item(object):  #事件条目
    def __init__(self,_id,title,content,ddl,length):
        self.id = _id #数据库内编号
        self.title = title #事件标题
        self.content = content #事件内容
        self.ddl = ddl.split('-') #事件截止日期
        for i in range(0,6):
            self.ddl[i] = int(self.ddl[i])
        self.dr_time = "" #事件执行日期
        self.length = length #事件期望长度
    def to_str(self):
        return self.title + ',' + self.content + ',' + self.dr_time + ',' + str(self.id)
    def __lt__(self, value):
        if self.ddl[0] != value.ddl[0]:
            return self.ddl[0] < value.ddl[0]
        if self.ddl[1] != value.ddl[1]:
            return self.ddl[1] < value.ddl[1]
        if self.ddl[2] != value.ddl[2]:
            return self.ddl[2] < value.ddl[2]
        if self.ddl[3] != value.ddl[3]:
            return self.ddl[3] < value.ddl[3]
        if self.ddl[4] != value.ddl[4]:
            return self.ddl[4] < value.ddl[4]
        return self.ddl[5] < value.ddl[5]
# delete from user_data;
# delete from user_password;
# delete from event_list;
        
def deal_event(s:item): #事件排列
    ans = []
    lt = time.localtime(time.time())
    tm_year = lt.tm_year
    tm_mon = lt.tm_mon
    tm_mday = lt.tm_mday
    tm_hour = lt.tm_hour
    tm_min = lt.tm_min
    tm_sec = lt.tm_sec
    s = sorted(s)
    ddd = 0
    for x in s:
        print(x.ddl)
        if tm_year > x.ddl[0]:
            continue
        elif tm_year == x.ddl[0]:
            if tm_mon > x.ddl[1]:
                continue
            elif tm_mon == x.ddl[1]:
                if tm_mday > x.ddl[2]:
                    continue
                elif tm_mday == x.ddl[2]:
                    if tm_hour > x.ddl[3]:
                        continue
                    elif tm_hour == x.ddl[3]:
                        if tm_min > x.ddl[4]:
                            continue
                        elif tm_min == x.ddl[4]:
                            if tm_sec > x.ddl[5]:
                                continue
        x.dr_time = str(tm_year) + '-' + str(tm_mon) + '-' + str(tm_mday) + '-' + str(tm_hour) + '-' + str(tm_min) + '-' + str(tm_sec)
        tm_hour += x.length
        if tm_hour >= 24:
            tm_mday += tm_hour // 24
            tm_hour //= 24
        while True:
            if tm_mon in [1,3,5,7,8,10,12]:
                if tm_mday > 31:
                    tm_mon += 1
                    tm_mday -= 31
                    if tm_mon == 13:
                        tm_mon = 1
                        tm_year += 1
                else:
                    break
            elif tm_mon in [4,6,9,11]:
                if tm_mday > 30:
                    tm_mon += 1
                    tm_mday -= 30
                    if tm_mon == 13:
                        tm_mon = 1
                        tm_year += 1
                else:
                    break
            else:
                if tm_year % 4:
                    if tm_mday > 28:
                        tm_mon += 1
                        tm_mday -= 28
                        if tm_mon == 13:
                            tm_mon = 1
                            tm_year += 1
                else:
                    if tm_mday > 29:
                        tm_mon += 1
                        tm_mday -= 29
                        if tm_mon == 13:
                            tm_mon = 1
                            tm_year += 1  
        if tm_year > x.ddl[0]:
            tm_year = x.ddl[0]
            tm_mon = x.ddl[1]
            tm_mday = x.ddl[2]
            tm_hour = x.ddl[3]
            tm_min = x.ddl[4]
            tm_sec = x.ddl[5]
        elif tm_year == x.ddl[0]:
            if tm_mon > x.ddl[1]:
                tm_year = x.ddl[0]
                tm_mon = x.ddl[1]
                tm_mday = x.ddl[2]
                tm_hour = x.ddl[3]
                tm_min = x.ddl[4]
                tm_sec = x.ddl[5]
            elif tm_mon == x.ddl[1]:
                if tm_mday > x.ddl[2]:
                    tm_year = x.ddl[0]
                    tm_mon = x.ddl[1]
                    tm_mday = x.ddl[2]
                    tm_hour = x.ddl[3]
                    tm_min = x.ddl[4]
                    tm_sec = x.ddl[5]
                elif tm_mday == x.ddl[2]:
                    if tm_hour > x.ddl[3]:
                        tm_year = x.ddl[0]
                        tm_mon = x.ddl[1]
                        tm_mday = x.ddl[2]
                        tm_hour = x.ddl[3]
                        tm_min = x.ddl[4]
                        tm_sec = x.ddl[5]
                    elif tm_hour == x.ddl[3]:
                        if tm_min > x.ddl[4]:
                            tm_year = x.ddl[0]
                            tm_mon = x.ddl[1]
                            tm_mday = x.ddl[2]
                            tm_hour = x.ddl[3]
                            tm_min = x.ddl[4]
                            tm_sec = x.ddl[5]
                        elif tm_min == x.ddl[4]:
                            if tm_sec > x.ddl[5]:
                                tm_year = x.ddl[0]
                                tm_mon = x.ddl[1]
                                tm_mday = x.ddl[2]
                                tm_hour = x.ddl[3]
                                tm_min = x.ddl[4]
                                tm_sec = x.ddl[5]
        x.dr_time += '->' + str(tm_year) + '-' + str(tm_mon) + '-' + str(tm_mday) + '-' + str(tm_hour) + '-' + str(tm_min) + '-' + str(tm_sec)
        ans.append(x)
    return ans


# 接收客户端消息并处理
async def recv_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        cred_dict = recv_text.split(":")
        if cred_dict[0] == 'fetch': # 查询用户数据并返回
            db = sql.connect("119.3.164.126","DB_USER47","DB_USER47@123","user47db" )
            cursor = db.cursor()
            cursor.execute('select data from user_data where uname = "' + cred_dict[1] + '"')
            data = cursor.fetchone()
            data = data[0]
            if(data == None):
                data = ""
            dd = data.split(',')
            print(dd)
            if dd[0] == '':
                dd = []
            ans = []
            for each in dd:
                r = int(each)
                cursor.execute('select title,content,ddl,length from event_list where id = ' + str(r))
                de = cursor.fetchone()
                print(de)
                ans.append(item(r,de[0],de[1],de[2],de[3]))
            ans = deal_event(ans)
            db.commit()
            anss = ""
            for x in ans:
                anss += ';'
                anss += x.to_str()
            await websocket.send("fb" + anss)
            db.close()
        if cred_dict[0] == 'del': #删除某个事件
            b = sql.connect("119.3.164.126","DB_USER47","DB_USER47@123","user47db" )
            cursor = db.cursor() 
            print('delete from event_list where id=' + cred_dict[2])
            cursor.execute('delete from event_list where id=' + cred_dict[2])
            db.commit()
            cursor.execute('select data from user_data where uname ="' + cred_dict[1] + '"')
            dd = cursor.fetchone()
            dd = dd[0]
            dd = dd.split(',')
            val = int(cred_dict[2])
            ans = []
            print(dd)
            for x in dd:
                if int(x) != val:
                    ans.append(int(x))
            ss = ''
            print(ss)
            for x in ans:
                ss += str(x) + ','   
            ss = ss[:-1]
            print(ss)
            cursor.execute('update user_data set data="'+ss+'" where uname = "'+cred_dict[1]+'"')
            db.commit()
            dd = ss.split(',')
            ans = []
            if dd[0] == '':
                dd = []
            print(dd)
            for each in dd:
                r = int(each)
                cursor.execute('select title,content,ddl,length from event_list where id = ' + str(r))
                de = cursor.fetchone()
                print(de)
                ans.append(item(r,de[0],de[1],de[2],de[3]))
            ans = deal_event(ans)
            anss = ""
            for x in ans:
                anss += ';'
                anss += x.to_str()
            await websocket.send("fb" + anss)
        if cred_dict[0] == 'add': #添加某个事件
            db = sql.connect("119.3.164.126","DB_USER47","DB_USER47@123","user47db" )
            cursor = db.cursor()
            cursor.execute('select max(id) from event_list')
            data = cursor.fetchone()
            data = data[0]
            print(data)
            if(data == None):
                data = 1
            else:
                data = data + 1
            cursor.execute('insert into event_list (id,title,content,ddl,length) values (' + str(data) + ',"' + cred_dict[1] + '","' + cred_dict[2] + '","' + cred_dict[3] + '",'+ cred_dict[4] + ')')
            db.commit()
            cursor.execute('select data from user_data where uname ="' + cred_dict[5] + '"')
            dd = cursor.fetchone()
            dd = dd[0]
            if dd == None:
                dd = ''
            if dd != '':
                dd += ','
            dd += str(data)
            cursor.execute('update user_data set data="'+dd+'" where uname = "'+cred_dict[5]+'"')
            dd = dd.split(',')
            ans = []
            for each in dd:
                r = int(each)
                cursor.execute('select title,content,ddl,length from event_list where id = ' + str(r))
                de = cursor.fetchone()
                print(de)
                ans.append(item(r,de[0],de[1],de[2],de[3]))
            ans = deal_event(ans)
            db.commit()
            anss = ""
            for x in ans:
                anss += ';'
                anss += x.to_str()
            await websocket.send("fb" + anss)
# 服务器端主逻辑
async def main_logic(websocket, path):
    print(1)
    await check_permit(websocket)

    await recv_msg(websocket)

start_server = websockets.serve(main_logic, '10.128.240.40', 5678) #建立websocket


asyncio.get_event_loop().run_until_complete(start_server) #构建协程
asyncio.get_event_loop().run_forever()