from pydantic import BaseModel
from typing import Union, List

class Query(BaseModel):
    query: Union[str, None] = None

class Result(BaseModel):
    success: bool = False
    exception: Union[str, None] = None
    result: List


