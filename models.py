from pydantic import BaseModel
from fastapi import Body


class PasswordOptions(BaseModel):
    """Class for validate password input"""

    length: int = Body(gt=0, lt=90)
    lowercase: bool = True
    uppercase: bool = True
    digits: bool = True
    symbols: bool = True
