import numbers
from secrets import choice
import sqlite3
conn = sqlite3.connect(r"C:\Users\LENOVO\Desktop\pu\project.db")
c = conn.cursor()

#สร้างตาราง สมาชิก(ลูกค้า)
"""
create = ''' CREATE TABLE "info_members" (
	"id"	INTEGER NOT NULL,
	"nickname"	TEXT NOT NULL,
	"phone_number"	TEXT(10) NOT NULL,
	"point"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);'''
c.execute(create)
"""

#สร้างตาราง พนักงาน
"""
create2 = '''CREATE TABLE "employee" (
    "id"    INTEGER,
    "fname" TEXT NOT NULL,
    "lname" TEXT NOT NULL,
    "password"  TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT) 
);'''
c.execute(create2)
"""


#พนักงาน login
def login():

    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\pu\project.db') #สร้างออบเจ็กต์เชื่อมต่อ sqlite3.connect() ซึ่งเป็นตัวติดต่อกับฐานข้อมูล
    c = conn.cursor() #ตัวที่ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูล
    #บันทึกข้อมูล พนักงาน

    #try : #คำสั่งที่ต้องการตรวจจับข้อผิดพลาด
    #    data = ('Kanthida','Untapunya','1111'),('Sasitorn','Phakdeeburud','0000') #ข้อมูลของพนักงาน
    #    c.executemany('''INSERT INTO employee (id,fname,lname,password) VALUES (NULL+1,?,?,?)''',data)
    #    conn.commit() #ใช้บันทึกข้อมูล ใช้เมื่อมีการเปลี่ยนแปลงข้อมูล
    #except sqlite3.Error as e: #สิ่งที่จะทำถ้าเกิดข้อผิดพลาด
    #    print(e)

    #ให้พนักงานใส่รหัสผ่าน
    pass_code = str(input('\n\t    🔍 กรุณาป้อนรหัสผ่านเพื่อเข้าสู่ระบบ : '))
    if pass_code == '0000' :
        print('\n\t✅✅ พนักงาน Sasitorn เข้าสู่ระบบเรียบร้อย ✅✅')
    elif pass_code == '1111' :
        print('\n\t✅✅ พนักงาน Kanthida เข้าสู่ระบบเรียบร้อย ✅✅')
    elif pass_code != '0000' or pass_code != '1111':
        print('   ⚠️  รหัสผ่านไม่ถูกต้อง ป้อนรหัสผ่านใหม่อีกครั้ง')
        login()


#เมนูไว้เลือกว่าจะทำรายการอะไร
def menu():
    global choice 
    print('\n'+'='*45+'\n\tโปรแกรมสมัครสมาชิกร้านขายของ 🛒\n'+'='*45)
    print('🟡 สมัครสมาชิก          กด👆 1\n🟢 แสดงรายชื่อสมาชิก     กด👆 2\n🔵 แก้ไขข้อมูลสมาชิก      กด👆 3\n🟣 สะสมแต้ม            กด👆 4\n⚪ แสดงการแลกแต้ม      กด👆 5\n🔴 ออกจากโปรแกรม      กด👆 6')
    choice = int(input('\nกรุณาเลือกรายการ : ')) #inputว่าจะทำรายกายใด 


#สมัครสมาชิก > อินพุต id(int ห้ามซ้ำ เรียง),ชื่อเล่น(text),เบอร์โทร(text)
def apply():
    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\pu\project.db')
    c = conn.cursor()
    x = [['ไอดี','ชื่อ','เบอร์โทรศัพท์','แต้ม']] #สร้างใหม่
    for i in c.execute('''SELECT * FROM info_members'''):
        x.append(i) #เอาข้อมูล i ไปต่อลิส x
    print('\n'+'\n\t\t   🟡 สมัครสมาชิก 🟡')

    def input_nickname(): #ป้อนชื่อ
        global nickname
        nickname = input('\n\t❇️  กรุณาป้อนชื่อเล่น : ')
        if nickname.isalpha() == True :
            input_phone_number()
        if nickname.isalpha() == False : #ถ้าเป็นอักษรแปลกๆ เช่น ตัวเลข หรือ *)% เป็นต้น
            print('⚠️  กรุณาป้อนชื่อที่ถูกต้อง')
            print('⚠️  ป้อนได้เฉพาะตัวอักษร a-z')
            input_nickname()
    
    def input_phone_number(): #ป้อนหมายเลขโทรศพท์
        global phone_number
        phone_number = input('\n\t📞 กรุณาป้อนหมายเลขโทรศัพท์ : ')
        for i in range(len(x)):
                if phone_number == x[i][2] :
                    print('⚠️  หมายเลขโทรศัพท์ซ้ำ')
                    print('⚠️  กรุณาป้อนข้อมูลหมายเลขโทรศัพท์ที่ถูกต้อง')
                    input_phone_number()
        if phone_number.isdigit() == False :
            print('⚠️  กรุณาป้อนเฉพาะตัวเลขและป้อนให้ครบ 10 ตัว')
            input_phone_number()
        elif len(phone_number) != 10 :
            print('⚠️  กรุณาป้อนป้อนตัวเลขให้ครบ 10 ตัว ')
            input_phone_number()
        elif phone_number.isdigit() == True or len(phone_number) == 10 :
            exit

    input_nickname()
    point = 0
    print('\n✅ สมัครสมาชิกเรียบร้อยแล้ว')
    c.execute('''INSERT INTO info_members VALUES(NULL+1,?,?,?)''',(nickname,phone_number,point)) #เพิ่มข้อมูล
    conn.commit() #ใช้บันทึกข้อมูล ใช้เมื่อมีการเปลี่ยนแปลงข้อมูล


#แสดงชื่อสมาชิก>ไอดี,ชื่อ,เบอร์,แต้ม
def show_members():
    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\pu\project.db') #สร้างออบเจ็กต์เชื่อมต่อ sqlite3.connect() ซึ่งเป็นตัวติดต่อกับฐานข้อมูล
    c = conn.cursor() #ตัวที่ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูล
    global x,i #xคือลิสที่สร้างขึ้นมา , iคือข้อมูลในตาราง
    print('\n\t   🟢 แสดงรายชื่อสมาชิก 🟢')
    x = [['ไอดี','ชื่อ','เบอร์โทรศัพท์','แต้ม']] #สร้างใหม่
    for i in c.execute('''SELECT * FROM info_members'''):
        x.append(i) #เอาข้อมูล i ไปต่อลิส x
    for i in range(len(x)): # lenx คือ จำนวนสมาชิก 
        if i == 0:
            print('-'*53)
            print('{:<15}{:<11}{:^24}{:^11}'.format(x[i][0],x[i][1],x[i][2],x[i][3])) #ปริ้นหัวตาราง
            print('-'*53)
        else:
            print('{:<14}{:<14}{:<16}{:>6}'.format(x[i][0],x[i][1],x[i][2],x[i][3])) #ข้อมูลสมาชิก


#แก้ไข้ข้อมูลสมาชิก 
def edit():
    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\pu\project.db') #สร้างออบเจ็กต์เชื่อมต่อ sqlite3.connect() ซึ่งเป็นตัวติดต่อกับฐานข้อมูล
    c = conn.cursor() #ตัวที่ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูล
    print('\n\n\t    🔵 แก้ไขข้อมูลสมาชิก 🔵')
    id = input('\nโปรดป้อนไอดีที่ต้องการแก้ไข : ') #ชี้ตำแหน่ง id ที่ต้องการแก้ไข
    x = [['ไอดี','ชื่อ','เบอร์โทรศัพท์','แต้ม']] #สร้างใหม่

    for i in c.execute('''SELECT * FROM info_members WHERE id = ?''',id): ##ค้นหาข้อมูลในตาราง info_members ให้แสดงเฉพาะ id = ?(ที่ป้อนเข้ามา)
        x.append(i) #เอาข้อมูลไปต่อลิสx

    #แสดงข้อมูลสมาชิกที่ป้อน id เข้ามา
    for i in range(len(x)):
        if i == 0:
            print('-'*53)
            print('{:<15}{:<11}{:^24}{:^11}'.format(x[i][0],x[i][1],x[i][2],x[i][3]))
            print('-'*53)
        else :
            print('{:<14}{:<14}{:<16}{:>6}'.format(x[i][0],x[i][1],x[i][2],x[i][3]))
        conn.commit() #ใช้บันทึกข้อมูล

    #เลือกรายการที่ต้องการแก้ไข
    edit_members = int(input('\n   --- รายการแก้ไข ---\n⏺️  ชื่อ  กด👆 1\n⏺️  หมายเลขโทรศัพท์  กด👆 2\n⏺️  ทั้ง 2 รายการ  กด👆 3\n\nกรุณาเลือกรายการที่ต้องการแก้ไข : '))
    
    def edit_nickname():
        nickname = input('\n❇️  กรุณาป้อนชื่อที่ต้องการแก้ไข : ')
        if nickname.isalpha() == True :
            data = (nickname,id)
            c.execute(''' UPDATE info_members SET nickname = ? WHERE id = ? ''',data)
            conn.commit()
            print('✅ แก้ไขข้อมูลชื่อเป็น {} เรียบร้อยแล้ว'.format(nickname))
        if nickname.isalpha() == False : #ถ้าเป็นอักษรแปลกๆ เช่น ตัวเลข หรือ *)% เป็นต้น
            print('⚠️  กรุณาป้อนชื่อที่ถูกต้อง')
            print('⚠️  ป้อนได้เฉพาะตัวอักษร')
            edit_nickname()
 
    def edit_phone_number():
        phone_number = input('\n📞 กรุณาป้อนเบอร์โทรศัพท์ที่ต้องการแก้ไข : ')
        for i in range(len(x)):
            if phone_number == x[i][2] :
                print('⚠️  หมายเลขโทรศัพท์ซ้ำ')
                print('⚠️  กรุณาป้อนข้อมูลหมายเลขโทรศัพท์ที่ถูกต้อง')
                edit_phone_number()
        if phone_number.isdigit() == False :
            print('⚠️  กรุณาป้อนเฉพาะตัวเลขและป้อนให้ครบ 10 ตัว')
            edit_phone_number()
        if len(phone_number) != 10 :
            print('⚠️  กรุณาป้อนป้อนตัวเลขให้ครบ 10 ตัว ')
            edit_phone_number()
        if phone_number.isdigit() == True and len(phone_number) == 10 :
            data = (phone_number,id)
            c.execute(''' UPDATE info_members SET phone_number = ? WHERE id = ? ''',data)
            conn.commit()
            print('✅ แก้ไขข้อมูลเบอร์โทรศัพท์เป็น {} เรียบร้อยแล้ว'.format(phone_number))
            exit
        

    if edit_members == 1 : #แก้ไขชื่อ
        edit_nickname()
    if edit_members == 2: #แก้ไขเบอร์โทร
        edit_phone_number()
    if edit_members == 3: #แก้ไขทั้งสอง
        edit_nickname()
        edit_phone_number()


#สะสมแต้ม 
def collect_points():
    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\pu\project.db') #สร้างออบเจ็กต์เชื่อมต่อ sqlite3.connect() ซึ่งเป็นตัวติดต่อกับฐานข้อมูล
    c = conn.cursor() #ตัวที่ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูล

    x = [['ไอดี','ชื่อ','เบอร์โทรศัพท์','แต้ม']] #สร้างใหม่

    for i in c.execute('''SELECT * FROM info_members'''):
        x.append(i) #เอาข้อมูลไปต่อลิสx
 
    print('\n\t    🟣 สะสมแต้ม 🟣')
    id = int(input('👉 กรุณาป้อนไอดีที่ต้องการสะสมแต้ม : ')) # id ที่ต้องการเพิ่มแต้ม
    p = int(input('👉 กรุณาป้อนจำนวนแต้ม : ')) # แต้มที่สะสมได้ในครั้งนี้
    point = p + x[id][3] # point(เก่า) + point(ใหม่)
    try :
        data = (point,id) #ข้อมูลที่จะเอามาแทนที่ในตาราง
        c.execute('''UPDATE info_members SET point =? WHERE id = ? ''',data) #อัพเดตข้อมูลในตาราง
        print('✅ สะสมแต้มเรียบร้อยแล้ว')
        print('❇️  คุณ {}  มีแต้มสะสมรวม {} แต้ม'.format(x[id][1],point))
    except sqlite3.Error as e : #ถ้าเออเร่อให้บอกว่าเออเร่อ
        print(e)
    conn.commit() #ใช้บันทึกข้อมูล


#แสดงการแลกแต้มเป็นคูปองส่วนลด
def exchange_points():
    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\pu\project.db') #สร้างออบเจ็กต์เชื่อมต่อ sqlite3.connect() ซึ่งเป็นตัวติดต่อกับฐานข้อมูล
    c = conn.cursor() #ตัวที่ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูล
    print('\n\t    ⚪ แสดงการแลกแต้ม ⚪')
    id = input('👉 กรุณาป้อนไอดี : ') #ป้อนไอดีที่ต้องการแก้ไข เพื่อระบุตำแหน่ง

    x = [['ไอดี','ชื่อ','เบอร์โทรศัพท์','แต้ม']] #สร้างใหม่
    for i in c.execute('''SELECT * FROM info_members WHERE id = ?''',id): #อ่านข้อมูลแค่ id =?(ค่าที่ป้อนเข้ามา)
        x.append(i) #เอาข้อมูลไปต่อลิสx

    #แสดงข้อมูล id = ? (ที่ป้อนเข้ามา)
    for i in range(len(x)):
        if i == 0:
            print('-'*53)
            print('{:<15}{:<11}{:^24}{:^11}'.format(x[i][0],x[i][1],x[i][2],x[i][3]))
            print('-'*53)
        else :
            print('{:<14}{:<14}{:<16}{:>6}'.format(x[i][0],x[i][1],x[i][2],x[i][3]))
        conn.commit()
 
    if x[i][3] >= 100 and x[i][3] <= 499 : #ถ้าแต้มอยู่ในระหว่างนี้
        print('\nสามารถแลกเป็นคูปองส่วนลดได้ 3%')
        exchange = input('ต้องการแลกหรือไม่(Y/N) : ') #ให้เลือกว่า จะแลกแต้มหรือไม่
        if exchange == 'Y': #กรณีแลก
            point = x[i][3] - 100 #ลบพ้อยที่แลกออก #พ้อยใหม่
            try :
                data = (point,id) #ข้อมูลที่ต้องการอัพเดต
                c.execute('''UPDATE info_members SET point =? WHERE id = ? ''',data)
            except sqlite3.Error as e :
                print(e)
            print('แลกแต้มเรียบร้อยแล้ว')
        else : #กรณีไม่แลก 
            exit
    elif x[i][3] >= 300 and x[i][3] <= 499 :
        print('\nคุณสามารถแลกเป็นคูปองส่วนลดได้ 10%')
        exchange = input('ต้องการแลกหรือไม่ (Y/N) : ')
        if exchange == 'Y':
            point = x[i][3] - 300
            try :
                data = (point,id)
                c.execute('''UPDATE info_members SET point =? WHERE id = ? ''',data)
            except sqlite3.Error as e :
                print(e)
            print('แลกแต้มเรียบร้อยแล้ว')
        else :
            exit
    elif x[i][3] >= 500 and x[i][3] <= 699 :
        print('\nคุณสามารถแลกเป็นคูปองส่วนลดได้ 16%')
        exchange = input('ต้องการแลกหรือไม่ (Y/N) : ')
        if exchange == 'Y':
            point = x[i][3] - 500
            try :
                data = (point,id)
                c.execute('''UPDATE info_members SET point =? WHERE id = ? ''',data)
            except sqlite3.Error as e :
                print(e)
        else :
            exit
    elif x[i][3] >= 700 and x[i][3] <= 899 :
        print('\nคุณสามารถแลกเป็นคูปองส่วนลดได้ 23%')
        exchange = input('ต้องการแลกหรือไม่ (Y/N) : ')
        if exchange == 'Y':
            point = x[i][3] - 700
            try :
                data = (point,id)
                c.execute('''UPDATE info_members SET point =? WHERE id = ? ''',data)
            except sqlite3.Error as e :
                print(e)
            print('แลกแต้มเรียบร้อยแล้ว')
        else :
            exit
    elif x[i][3] >= 1000 :
        print('\nคุณสามารถแลกเป็นคูปองส่วนลดได้ 33%')
        exchange = input('ต้องการแลกหรือไม่(Y/N) : ')
        if exchange == 'Y':
            point = x[i][3] - 1000
            try :
                data = (point,id)
                c.execute('''UPDATE info_members SET point =? WHERE id = ? ''',data)
            except sqlite3.Error as e :
                print(e)
            print('แลกแต้มเรียบร้อยแล้ว')
        else :
            exit
    conn.commit()


login()
while True:
    menu()
    if choice == 1 :
        apply()
    if choice == 2 :
        show_members()
    if choice == 3 :
        edit()
    if choice == 4 :
        collect_points()
    if choice == 5 :
        exchange_points()
    if choice == 6 :
        print('✅ ออกจากโปรแกรมเรียบร้อยแล้ว')
        break