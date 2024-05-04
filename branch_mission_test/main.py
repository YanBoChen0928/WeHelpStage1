# main.py
from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()

# 設置靜態文件目錄
app.mount("/static", StaticFiles(directory="static"), name="static")

#初始化
templates = Jinja2Templates(directory="templates")

# 啟用 SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# 定義用戶狀態的鍵
USER_STATE_KEY = "SIGNED-IN"

# 驗證成功時設置用戶狀態為已登錄
def set_user_signed_in(request: Request):
    request.session[USER_STATE_KEY] = True # key: value

# 登出時設置用戶狀態為未登錄
def set_user_signed_out(request: Request):
    request.session.pop(USER_STATE_KEY, None) # 刪除 SIGNED-IN 的key

# 檢查用戶是否已登錄的依賴
def check_user_signed_in(request: Request):
    signed_in = request.session.get(USER_STATE_KEY, False)
    return signed_in


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # static_css = request.url_for('static', path='style.css')
    return templates.TemplateResponse("index.html", {"request": request, "home_url": request.url_for('home')})

@app.post("/signin")
async def signin_post(request: Request, username: str = Form(None), password: str = Form(None), checkbox: bool = Form(None)):

    # authentication logic
    if not username or not password:
        # 如果用戶名或密碼為空，重定向到錯誤頁面，並顯示消息
        return RedirectResponse(url="/error?message=請輸入帳號密碼")

    if username != "test" or password != "test":
        # 如果用戶名或密碼不正確，重定向到錯誤頁面，並顯示消息
        return RedirectResponse(url="/error?message=帳號、密碼輸入錯誤")

    # 如果用戶名和密碼正確，重定向到成功頁面
    set_user_signed_in(request)
    return RedirectResponse(url="/member", status_code=303)  # 303 將本來應該需要用post傳輸允許用get

#show不同訊息的錯誤頁面
@app.post("/error", response_class=HTMLResponse)
async def error(request: Request, message: str = ""):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

#success 登入頁面member
@app.get("/member", response_class=HTMLResponse, dependencies=[Depends(check_user_signed_in)])
async def member(request: Request): 
     # 檢查用戶是否已登錄
    signed_in = request.session.get(USER_STATE_KEY, False)
    if not signed_in:
        # 如果未登錄，重定向到首頁
        return RedirectResponse(url="/", status_code=303)
    
    return templates.TemplateResponse("member.html", {"request": request})

# 登出端點
@app.get("/signout")
async def signout(request: Request):
    # 登出，設置用戶狀態為未登錄
    set_user_signed_out(request)
    # 重定向到首頁
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
