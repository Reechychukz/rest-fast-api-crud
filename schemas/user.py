from datetime import date
from pydantic import BaseModel

class User(BaseModel):
 id : int
 name : str
 age : int
 message : str
 createDate : date