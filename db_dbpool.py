import pymysql

from DBUtils.PooledDB import PooledDB
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    host='127.0.0.1',
    port=3306,
    user='root',
    password='19941228',
    database='flask',
    charset='utf8'
)

def get_conn():
    conn = POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

def reset_conn(conn, cursor):
    cursor.close()
    conn.close()

def fetch_all(sql,args):
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。


    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')

    conn, cursor=get_conn()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    # print(result)
    reset_conn(conn, cursor)
    return result

def insert_one(sql, args):
    conn, cursor=get_conn()
    result =cursor.execute(sql, args)
    conn.commit()
    # print(result)
    reset_conn(conn, cursor)
    return result

# res = fetch_all('select * from users where id=%s',(1,))
res = fetch_all('select * from users',())
print(res)
# count = insert_one("insert into users(name) values (%s)",("sqlhelper",))
# print(count)

# if __name__ == '__main__':
#
#     func()