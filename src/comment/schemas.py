from datetime import datetime

from pydantic import BaseModel


class CommentCreate(BaseModel):
    id: int
    id_coin: int
    id_user: int
    message: str
    data_time: datetime
