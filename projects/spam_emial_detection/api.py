from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import Model

app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/check", response_class=HTMLResponse)
async def check_email(email: str = Form(...)):
    result = Model(email)
    
    if result == "Spam":
        return """
        <div id="result" class="spam">
            <div class="result-icon">
                <i class="fas fa-exclamation-triangle"></i>
            </div>
            <h2 class="result-title">Spam Detected!</h2>
            <p class="result-message">This email has been identified as spam.</p>
            <div class="result-warning">
                <i class="fas fa-exclamation-circle"></i> Be cautious with any links or attachments
            </div>
        </div>
        """
    else:
        return """
        <div id="result" class="ham">
            <div class="result-icon">
                <i class="fas fa-check-circle"></i>
            </div>
            <h2 class="result-title">Legitimate Email</h2>
            <p class="result-message">This email appears to be safe.</p>
        </div>
        """