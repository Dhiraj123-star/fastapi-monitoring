import os
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from prometheus_fastapi_instrumentator import Instrumentator

# Database Configuration
DATABASE_URL= os.getenv("DATABASE_URL","postgresql://user:password@db:5432/fastapi_db")
engine = create_engine(DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base= declarative_base()

# Simple Datbase Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Monitoring Service")

# Dependency to get DB session
def get_db():
    db= SessionLocal()
    try: yield db
    finally: db.close()



# New health check endpoint
@app.get("/health",tags=["Health Check"])
async def health_check():
    return {"status":"healthy"}


@app.get("/")
async def root():
    return {
        "message": "Database persistence active!!"
        }

@app.post("/users/{name}")
def create_user(name:str,db:Session=Depends(get_db)):
    new_user= User(name=name)
    db.add(new_user)
    db.commit()
    return {"status":"User saved","name":name}

@app.get("/users")
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()

# This line captures request latencies,sizes, and counts automatically
Instrumentator().instrument(app).expose(app)