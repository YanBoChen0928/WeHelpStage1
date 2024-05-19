# main.py
from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector

#from fastapi.security import HTTPBasic, HTTPBasicCredentials #本考慮5/11新增（比對資料庫跟html帳號密碼）

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

mysql_config = {
    'host': 'localhost',
    'user': 'wehelp',
    'password': 'wehelp',
    'database': 'website'
}

app.add_middleware(SessionMiddleware, secret_key="your_secret_key") ##在正式上線的時候要用環境變數來處理

# 定義用戶狀態的鍵
USER_STATE_KEY = "SIGNED-IN"

# 驗證成功時設置用戶狀態為已登錄
def set_user_signed_in(request: Request):
    request.session[USER_STATE_KEY] = True # key: value 

# 登出時設置用戶狀態為未登錄
def set_user_signed_out(request: Request):
    request.session.pop(USER_STATE_KEY, None) # 刪除 SIGNED-IN 的key

# 檢查用戶是否已登錄
def check_user_signed_in(request: Request):
    signed_in = request.session.get(USER_STATE_KEY, False)
    return signed_in

# home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "home_url": request.url_for('home')})

#中間層 
#註冊 signup=register介面
@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    form = await request.form() #需要用 await （表示完成這一個動作，才能做後續的, form.get()內是"name")
    signup_username = form.get("signup_username")     # 先建立這個，後面才能判斷username有沒有重複

    with mysql.connector.connect(**mysql_config) as conn:
         with conn.cursor() as cursor:
            # 檢查數據庫中是否已經存在相同的用戶名
            cursor.execute("SELECT * FROM `member` WHERE username = %s", (signup_username,))
            existing_user = cursor.fetchone()

            if existing_user:
                return templates.TemplateResponse("error.html", {"request": request,"message": "重複的使用者帳號"})
            else:
                # 如果不存在重複的用戶名，插入新用戶信息到數據庫中
                # 要傳給 jinja2模板用
                signup_name = form.get("signup_name")
                signup_password = form.get("signup_password")
                cursor.execute("INSERT INTO `member` (name, username, password) VALUES (%s, %s, %s)", (signup_name, signup_username, signup_password))
                conn.commit()

                # 在寫入新用戶到資料庫後，將name, username設置到 session 中
                request.session["user"] = signup_name
                request.session["username"] = signup_username
                #print("User signed up:", request.session["user"]) 檢測用，確定有寫入session, OK

                # 重定向用戶到首頁
                return RedirectResponse(f"/?success=True&name={signup_name}", status_code=303)

#登入 signin route
@app.post("/signin") 
async def signin_post(request:Request, 
                      username: str = Form(None), 
                      password: str = Form(None)): #從表單來的資料，要放 Form() !!!!!!
    
    with mysql.connector.connect(**mysql_config) as conn:
        with conn.cursor() as cursor: #有待整理的 code
            try:
                # 使用 AND 來比對
                cursor.execute("SELECT username, password, name, id FROM `member` WHERE (username = %s AND password = %s)", (username, password))
                user = cursor.fetchone() # 獲取一行結果
                #print("User from database:", user)  # 在這裡打印用戶信息

                if user: # 如果用戶存在
                    set_user_signed_in(request) #本來的session
                    member_data = {
                    "username": user[0],
                    "password": user[1],
                    "name": user[2],
                    "id": user[3]
                }
                    #print(name)
                    # 將用戶名稱存入 session !!!!! 這裡蠻重要的，因為除了signup這邊是起始點。
                    name = member_data['name']
                    request.session["user"] = name
                    request.session["username"] = member_data['username']
                    request.session["id"] = member_data['id']
                    return RedirectResponse(url=f"/member?name={name}", status_code=303) 
                else:  
                    return RedirectResponse(url="/error?message=帳號、密碼輸入錯誤")
            except Exception as e:
                print("MySQL signin Error:", e)
                raise HTTPException(status_code=500)

    # 如果用戶名和密碼正確，重定向到成功頁面
    #set_user_signed_in(request) 本來的session
    #return RedirectResponse(url="/member", status_code=303)  # 303 將本來應該需要用post傳輸允許用get

#show不同訊息的錯誤頁面
@app.post("/error", response_class=HTMLResponse)
async def error(request: Request, message: str = ""):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

#success 登入頁面member
@app.get("/member", response_class=HTMLResponse, dependencies=[Depends(check_user_signed_in)])
async def member(request: Request, new_message: str = Form(None)): 
    signed_in = request.session.get(USER_STATE_KEY, False)
    if not signed_in:
        return RedirectResponse(url="/", status_code=303)

    with mysql.connector.connect(**mysql_config) as conn:
        # 執行 SQL 查詢，使用 JOIN 操作獲取留言資料與作者名稱 (用dictionary, 以後應該都要用這個處理^^, 因為mysql-connector轉換出來都是tuple)
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT message.content AS message, member.name AS name FROM message JOIN `member` ON message.member_id = member.id")
            messages = cursor.fetchall()

    name = request.session.get("user")
    return templates.TemplateResponse("member.html", {"request": request, "messages": messages, "name":name, "new_messages":new_message}) #把這些參數傳回到member.html

#新留言功能
@app.post("/createMessage")
async def create_message(request: Request, new_message: str =Form(None)): #!!!!! 再強調一次，注意要回傳的參數跟怎麼傳的

    signed_in = request.session.get(USER_STATE_KEY, False)
    if not signed_in:
        return RedirectResponse(url="/", status_code=303)
    
    name = request.session.get("user")
    #print("from createMessage:", name )
    username = request.session.get("username")
    #print("from createMessage:",username)

    try:
        with mysql.connector.connect(host="localhost", user="wehelp", password="wehelp", database="website") as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id FROM `member` WHERE username = %s", (username,))
                result = cursor.fetchone()
                if result:
                    member_id = result[0]
                else:
                    raise HTTPException(status_code=404, detail="Hi, I got you!! User not found")

            # 插入新留言到 message table 中
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (member_id, new_message))
                conn.commit()
    except mysql.connector.Error as e:
        print("MySQL Error:", e)

    return RedirectResponse(url=f"/member?name={name}", status_code=303)
    
# week7 創建backend指令（查詢會員名字） 新增 "Member Query API"
@app.get("/api/member")
async def get_member(request: Request, username: str = None): #因為只有簡單的一段字串，用字串就好，不要在前端建立 form
    signed_in = request.session.get(USER_STATE_KEY, False)
    print("check the value of")
    print(username)
    if not signed_in:
        return {"data": None} # 若沒有sign-in，返回 null
    
    with mysql.connector.connect(**mysql_config) as db_connection: #用dictionary去進行資料的回傳 Json格式
        # 使用 cursor 執行 SQL 查詢
        with db_connection.cursor() as db_cursor:
            # 使用 SQL 查詢條件來選擇會員
            db_cursor.execute("SELECT id, name, username FROM `member` WHERE username = %s", (username,))
            memberName = db_cursor.fetchone()  # 獲取第一條匹配的結果
            print("SELECT from MYSQL:")
            print(memberName)
            if memberName:
                # 將結果手動轉換為字典（這邊因為配合python3.9安裝的mysql-connector-python沒有支援 dict內建函式，所以手動處理）
                member_data = {
                    "id": memberName[0],
                    "name": memberName[1],
                    "username": memberName[2]
                }
                print(member_data)
                return {"data": member_data}  # 返回會員資料的字典
            else:
                return {"data": None}  # 若沒有匹配到會員，返回 null

# week7 （更新會員名字） 新增 "Name Update API"
@app.patch("/api/member")
async def update_name(request: Request,  data: dict): #!!!!
    data = await request.json()  #稍等fetch步驟完成，才能執行以下
    name = data.get('name')      
    print("whether fastAPI get name from patch:")
    print(name)

    if name is None or name.strip() == "":
        return {"error": True}
    
    signed_in = request.session.get(USER_STATE_KEY, False)

    if not signed_in:
        return {"error": True} 
    print(signed_in)
    #這次沒有傳 username, 從session抓取
    username = request.session.get('username') #記得「' '」
    
    try:
        with mysql.connector.connect(**mysql_config) as db_connection: 
            with db_connection.cursor() as db_cursor:
                # 使用 SQL 查詢條件來update會員
                db_cursor.execute("UPDATE `member` SET name = %s WHERE username = %s", (name, username))
                db_connection.commit() 
                # 要取出印出更新後的 member_data, 回傳member.html更新{{ name }} 其實採用實際執行的方式，在前端修改就好
                db_cursor.execute("SELECT name FROM `member` WHERE username = %s", (username,))
                updated_row = db_cursor.fetchone() #如果上沒有select出來，這邊就會變成 None
                '''
                print("Update from MYSQL:") # 确认这里有输出
                print(updated_row)
                '''
                if updated_row:
                    '''
                    # 將結果手動轉換為字典
                    member_data = {
                        "name": updated_row[0],
                    }
                    print(member_data)
                    '''
                    return {"ok": True}  # 返回會員資料的字典
                else:
                    return {"error": True}  # 若沒有匹配到會員，返回 null
    except mysql.connector.Error as e:
        print("MySQL Error when doing fetch_patch:", e)

# 登出端點
@app.get("/signout")
async def signout(request: Request):
    # 登出，設置用戶狀態為未登錄
    set_user_signed_out(request)
    # 重定向到首頁
    return RedirectResponse(url="/", status_code=303)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
