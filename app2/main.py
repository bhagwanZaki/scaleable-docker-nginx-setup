from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def helloWorld():
	return {"message":"hello world from app2"}

