from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Device(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    inventory_number: str = Field(unique=True, index=True)
    status: str = Field(default="available")

    loans: List["Loan"] = Relationship(back_populates="device")