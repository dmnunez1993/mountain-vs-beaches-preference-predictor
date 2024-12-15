import os

from dotenv import load_dotenv
import uvicorn

if os.path.isfile(".env"):
    print("Loading env file...")
    load_dotenv(".env")

from logger.fastapi import FASTAPI_LOG_CONFIG

DEBUG = os.environ.get("DEBUG", "false") == "true"
BACKEND_PORT = int(os.environ.get("BACKEND_PORT", "8000"))

if __name__ == "__main__":
    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        reload=DEBUG,
        port=BACKEND_PORT,
        log_config=FASTAPI_LOG_CONFIG,
    )
