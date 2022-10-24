import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {'message': 'STARTED!!!'}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="localhost", port=8888)
