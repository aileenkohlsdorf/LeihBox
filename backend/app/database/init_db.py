from sqlmodel import SQLModel
from app.database.connection import engine
from app.models import User, Device, Loan

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Datenbanktabellen wurden erfolgreich erstellt!")


if __name__ == "__main__":
    create_db_and_tables()