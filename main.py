# Description: This is the main file for the FastAPI application. It contains the FastAPI application and the code to run the application using Uvicorn.
# The FastAPI application has two routes: the root route ("/") and the "/file-upload" route.
# The root route returns a simple JSON response, while the "/file-upload" route returns a message indicating that files can be uploaded there.
# The code to run the application using Uvicorn is at the bottom of the file.
import uvicorn
from logger import logger
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from middleware import log_middleware

app = FastAPI()

# Register middleware
app.add_middleware(BaseHTTPMiddleware, log_middleware)
logger.info("FastAPI application started...")


@app.get("/")
async def read_root() -> dict:
    return {"Hello": "World"}


@app.get("/file-upload")
async def file_upload() -> dict:
    return {"message": "Upload files here"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
