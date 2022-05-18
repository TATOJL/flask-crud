
from flask import Flask, render_template, request,redirect,url_for, flash
import app_module as m

app = Flask(__name__)
app.secret_key ="secret key"



  
@ app.route('/')
def index():
        return render_template('index.html')

@ app.route('/signup' ,methods=['GET','POST'])
def signup():
        return render_template('signup.html')
@ app.route('/signupinsert',methods=['POST'])
def signupinsert():
    if request.method == 'POST':
            a=request.form['account']
            p=request.form['password']
            u= request.form['username']
            e=request.form['email']
            i=request.form['identity_type']
            while True:
               if not m.sql_selectone(a) ==None:
                   flash("註冊失敗，此帳號: "+a+" 已被註冊!","danger") 
                   break
               m.sql_insert(a,p,u,e,i)
               flash("已成功註冊會員:  "+a,"success")
               break
            return redirect(url_for('signup'))     
        
@ app.route('/crud' ,methods=['GET','POST'])
def crud():
        datas= m.sql_read()
        text=['ID','帳號','密碼','會員身分','會員名稱','email','註冊時間','刪除','修改']
        return render_template('crud.html',members=datas,titles=text)

@ app.route('/search',methods=['POST'])
def search():
     if request.method == 'POST':
        a=request.form['searchaccount']
        data= m.sql_search(a)
        datas= m.sql_read()
        while True:
               if not m.sql_selectone(a) ==None:
                   flash("查詢成功，已找到帳號為 "+a+" 的會員","success") 
                   break
               
               flash("查詢失敗，找不到帳號為 "+ a +" 的會員","danger")
               break
    
        text=['ID','帳號','密碼','會員身分','會員名稱','email','註冊時間','刪除','修改']
        return render_template('crud.html',member=data,members=datas,titles=text)


@ app.route('/insert',methods=['POST'])
def insert():
    if request.method == 'POST':
            a=request.form['account']
            p=request.form['password']
            u= request.form['username']
            e=request.form['email']
            i=request.form['identity_type']
            while True:
               if not m.sql_selectone(a) ==None:
                   flash("新增失敗，此帳號: "+a+" 已被註冊!","danger") 
                   break
               m.sql_insert(a,p,u,e,i)
               flash("已成功新增會員:  "+a,"success")
               break
            return redirect(url_for('crud')) 

@ app.route('/update',methods=['POST'])
def update():
    if request.method == 'POST':
            a=request.form['account']
            ad=request.form['accountdata']
            p=request.form['password']
            u= request.form['username']
            e=request.form['email']
            i=request.form['identity_type']
            while True:
               if not m.sql_selectone(a) ==None and a !=ad:
                   flash("修改失敗，此帳號: "+a+" 已被註冊!","danger") 
                   break
              
               m.sql_update (a,p,u,e,i,ad)        
               flash("已成功將原會員:" +ad+" /"+"帳號修改為:"+a+" /"+"密碼修改為:"+p+" /"+"會員名稱修改為:"+u+" /"+"email修改為:"+e+" /"+"身分修改為:"+i,"success")
               break
            return redirect(url_for('crud')) 
           
                       
     
   
@ app.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        a=request.form['accountdata']
        m.sql_delete(a)
        flash("已成功刪除會員:" +a,"success")
        return redirect(url_for('crud'))              


if __name__ == '__main__':
    app.run(debug=True)
id_data=str(request.form['id'])
print(id_data)