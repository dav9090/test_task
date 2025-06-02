from fastapi import Header, HTTPException, Depends
from settings import settings

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")