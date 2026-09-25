from fastapi import Depends, FastAPI
from sqlmodel import Session, select
from models import Usuario, Reserva, SQLModel
from database import engine, get_session, init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# CRUD Usuarios
@app.post("/usuarios/")
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@app.get("/usuarios/")
def listar_usuarios(session: Session = Depends(get_session)):
    return session.exec(select(Usuario)).all()

# CRUD Reservas
@app.post("/reservas/")
def crear_reserva(reserva: Reserva, session: Session = Depends(get_session)):
    session.add(reserva)
    session.commit()
    session.refresh(reserva)
    return reserva

@app.get("/reservas/")
def listar_reservas(session: Session = Depends(get_session)):
    return session.exec(select(Reserva)).all()

