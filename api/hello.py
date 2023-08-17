from fastapi import FastAPI
import os
import resend
from fastapi.responses import RedirectResponse

resend.api_key = os.environ["RESEND_API_KEY"]

app = FastAPI()


@app.get("/api/hello")
async def read_root(name: str, email: str, message: str):
    params = {
        "from": "kouheihand@yahoo.co.jp",
        "to": [email],
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }
    result = "できたよ"  # await resend.Emails.send(params)
    # return {
    #     "name": name,
    #     "email": email,
    #     "message": message,
    #     "result": result,
    # }
    return RedirectResponse("../index.html")
