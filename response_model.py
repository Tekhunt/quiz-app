from pydantic import BaseModel
from typing import List


class Quiz_Respose(BaseModel):
    store_name: str
    quiz_id: List[str]