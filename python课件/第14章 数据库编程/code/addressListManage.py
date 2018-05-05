import sqlite3

def menu():
    '''本函数用来显示主菜单'''
    
    usage = ('\tL/l: List all the information.', 
             '\tD/d: Delete the information of certain people.',
             '\tA/a: Add new information for a new people',
             '\tQ/q: Exit the system.',
             '\tH/h: Help, view all commands.')
    print('Main menu'.center(70, '='))
    for u in usage:
        print(u)

def doSql(sql):
    '''用来执行SQL语句，尤其是INSERT和DELETE语句'''
    
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    
def add():
    '''本函数用来接收用户输入，检查格式，然后插入数据库'''
    
    print('Add records'.center(70, '='))
    
    #获取输入，只接受正确格式的数据
    while True:
        record = input('Please input name, sex, age, department, telephone, qq(Q/q to return):\n')
        #输入q或Q表示退出，结束插入记录的过程，返回主菜单
        if record in ('q', 'Q'):
            print('\tYou have stopped adding record.')            
            return
        
        #正确的格式应该恰好包含5个英文逗号
        if record.count(',') != 5:
            print('\tformat or data error.')
            continue
        else:
            name, sex, age, department, telephone, qq = record.split(',')
            #性别必须是F或M
            if sex not in ('F', 'M'):
                print('\tsex must be F or M.')
                continue
            #手机号和qq必须是数字字符串
            if (not telephone.isdigit()) or (not qq.isdigit()):
                print('\ttelephone and qq must be integers.')
                continue
            
            #年龄必须是介于1到130之间的整数
            try:
                age = int(age)
                if not 1<=age<=130:
                    print('\tage must be between 1 and 130.')
                    continue
            except:
                print('\tage must be an integer.')
                continue
            
        sql = 'INSERT INTO addressList(name,sex,age,department,telephone,qq) VALUES("'
        sql = sql + name + '","' + sex + '",' + str(age) + ',"' + department + '","'
        sql = sql + telephone + '","' + qq + '")'
        doSql(sql)
        print('\tYou have add a record.')

def exist(recordId):
    '''本函数用来测试数据表中是否存在recordId的id'''
    
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(id) from addressList where id=' + str(recordId))
    c = cur.fetchone()[0]
    conn.close()
    return c!=0

def remove():
    '''本函数用来接收用户输入的id号，并删除数据库中该id对应的记录'''
    
    print('Delete records'.center(70, '='))
    
    while True:
        #输入q或Q，返回上一级目录
        x = input('Please input the ID to delete(Q/q to return):\n')
        if x in ('q', 'Q'):
            print('\tYou have stopped removing record.')
            return

        #要删除的id必须是数字，并且已存在于数据库中
        try:
            recordId = int(x)
            if not exist(recordId):
                print('\tThis id does not exists.')
            else:
                sql = 'DELETE FROM addressList where id=' + x
                doSql(sql)
                print('\tYou have deleted a record.')
        except:
            print('\tid must be an integer')
            
def listInformation():
    '''本函数用来查看所有记录'''
    
    sql = 'SELECT * FROM addressList ORDER BY id ASC'
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    if not result:
        print('\tDatabase has no record at this time.')
    else:
        #格式化输出所有记录
        print('All records'.center(70, '='))
        print('Id    Name    Sex    Age    Department        Telephone    QQ')
        for record in result:
            print(str(record[0]).ljust(6), end='')
            print(record[1].ljust(8), end='')
            print(record[2].ljust(7), end='')
            print(str(record[3]).ljust(7), end='')
            print(record[4].ljust(18), end='')
            print(record[5].ljust(13), end='')
            print(record[6])
        print('='*30)
    conn.close()
    
def main():
    '''系统主函数'''
    
    print('Welcome to the addresslist manage system.')
    menu()
    while True:
        command = input('Please choose a command:')
        if command in ('L', 'l'):
            listInformation()
        elif command in ('D', 'd'):
            remove()
            menu()
        elif command in ('A', 'a'):
            add()
            menu()
        elif command in ('Q', 'q'):
            break
        elif command in ('H', 'h'):
            menu()
        else:
            print('\tYou have input a wrong command.')

#调用主函数，启动系统
main()
