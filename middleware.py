from logger import logger
from fastapi import Request
import time


async def log_middleware(request: Request, call_next):
    # Time when middleware is first invoked
    start = time.time()

    # Continue processing request to next middleware or the handler
    response = await call_next(request)

    process_time = time.time() - start

    log_dict = {
        "method": request.method,
        "url": request.url.path,
        "process_time": process_time,
    }

    # if you want keys to appear top level and searchable pass dict as extra
    logger.info(log_dict, extra=log_dict)
    return response
