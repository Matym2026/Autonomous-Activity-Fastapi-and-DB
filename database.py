from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = "postgresql://postgres:clave123@database-1.cxuswsim2rg7.us-east-2.rds.amazonaws.com:5432/mibasedatos"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
