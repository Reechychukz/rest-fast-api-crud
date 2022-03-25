from datetime import date
from pydantic import BaseModel

class User(BaseModel):
 name : str
 age : int
 message : str
 createDate : date