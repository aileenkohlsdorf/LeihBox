from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Loan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    device_id: int = Field(foreign_key="device.id")
    start_date: date
    end_date: date
    status: str = Field(default="pending")

    user: Optional["User"] = Relationship(back_populates="loans")
    device: Optional["Device"] = Relationship(back_populates="device")