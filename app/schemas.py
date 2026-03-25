from pydantic import BaseModel
from typing import Optional

# --- Item Schemas ---
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None

class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        from_attributes = True

# --- User Schemas ---
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str