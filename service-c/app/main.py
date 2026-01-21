from pydantic import BaseModel
from datetime import datetime
import mysql.connector
from typing import List
from core.settings import setting
from fastapi import FastAPI




# @asynccontextmanager
# async def lifespan(app: FastAPI):

    










def setup(records: List[dict] = None):  
    
    if records is None:
        records = list_of_dicts.copy()  
    
    pydantic_records = [Extra_data(**record) for record in records]
    
    insert_all_records([r.model_dump() for r in pydantic_records])
    
    print(f"✓ Setup complete: {len(pydantic_records)} validated records")
    return pydantic_records  




# Run it
setup()










