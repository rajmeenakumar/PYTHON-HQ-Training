import time
import logging
from fastapi import Request

logging.basicConfig(level=logging.INFO , filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    logging.info(f"Processing request: {request.method} {request.url}")

    response = await call_next(request)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Request processing completed in {elapsed_time:.3f} seconds")
    # logging.info(f"Completed request: {request.method} {request.url}")

    return response