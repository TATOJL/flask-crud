import mysql.connector as my
def sql_delete(id):
    conn = my.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
            # Create a new record
            sql = "DELETE FROM `member` WHERE ˋmember_idˋ= %s"
            cur.execute(sql, (id))
    # conn is not autocommit by default. So you must commit to save your changes.
        conn.commit()   

             

# Connect to the database
# create a pymysql.connect object 'conn'
conn = my.connect(host='localhost',
                             user='root',
                             password='kjh123efr',
                             database='aiweb',
                             charset='utf8mb4')
#with conn session 
with conn:
    #with conn.cur object cur session
    with conn.cursor() as cur:
        # 使用 cur.execute() 執行select sql script
        sql = "select member_id,account, password, username,email, \
            DATE_FORMAT(date, '%Y-%m-%d %T') \
            from `member`"
        cur.execute(sql)
        #使用 cur.fetchall() 從cur中取出資料
        #return value 'rows' --> tuple of tuples
        rows=cur.fetchall() 
for r in rows:
    print(r)