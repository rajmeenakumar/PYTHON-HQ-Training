import time
import logging
from fastapi import Request

logging.basicConfig(filename='app.log', level=logging.INFO)

async def logging_middleware(request: Request, call_next):
    start_time = time.time()

    # Log request
    logging.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    # Log response
    process_time = time.time() - start_time
    logging.info(f"Response: status_code={response.status_code}, time_taken={process_time}s")

    return response
