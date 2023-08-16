from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello.py")
async def read_root(name: str, email: str, message: str):
    return {"name": name, "email": email, "message": message}
