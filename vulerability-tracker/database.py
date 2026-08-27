from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, Session
from typing import Optional, Literal
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

app = FastAPI()


class Base(DeclarativeBase):
    pass


class Define_sev(BaseModel):
    severity: Literal["low", "high", "medium", "critical"]


class Define_Vul(BaseModel):
    cve_id: str
    severity: Literal["low", "high", "medium", "critical"]
    description: Optional[str] = None


class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    id: Mapped[int] = mapped_column(primary_key=True)
    cve_id: Mapped[str] = mapped_column(nullable=False, unique=True)
    severity: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)


class VulnerabilityResponse(BaseModel):
    id: int
    cve_id: str
    severity: Literal["low", "high",
                      "medium", "critical"]
    description: Optional[str] = None


database_url = "postgresql+psycopg://postgres:PASS@localhost:5432/vulnerability_tracker"

engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    yield (db)
    db.close()


@app.get("/vulnerabilities/{cve_id}", response_model=VulnerabilityResponse)
def get_vul(cve_id: str, db: Session = Depends(get_db)):
    result = db.execute(select(Vulnerability).where(
        Vulnerability.cve_id == cve_id))
    v = result.scalar_one_or_none()
    if v is None:
        raise HTTPException(404, detail="Vulnerability not found")
    else:
        return v


@app.get("/vulnerabilities")
def get_all_vul(limit: Optional[int] = None,
                off: Optional[int] = None,
                severity: Optional[Literal["low", "high",
                                           "medium", "critical"]] = None,
                sort: Optional[Literal["id"]] = None,
                order: Optional[Literal["asc", "desc"]] = None,
                db: Session = Depends(get_db)):

    result = select(Vulnerability)

    if severity is not None:
        result = result.where(Vulnerability.severity == severity)

    if limit is not None:
        result = result.limit(limit)

    if off is not None:
        result = result.offset(off)

    if order is not None:
        if order == "asc":
            result = result.order_by(Vulnerability.id.asc())
        elif order == "desc":
            result = result.order_by(Vulnerability.id.desc())

    result = db.execute(result)
    v = result.scalars().all()
    return v


@app.post("/vulnerabilities", response_model=VulnerabilityResponse)
def post_vul(v: Define_Vul, db: Session = Depends(get_db)):
    new_vul = Vulnerability(
        cve_id=v.cve_id, severity=v.severity, description=v.description)
    db.add(new_vul)
    try:
        db.commit()
        return new_vul
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,
                            detail="CVE already exists")


@app.put("/vulnerabilities/{cve_id}")
def put_vul(cve_id: str, severity: Define_sev, db: Session = Depends(get_db)):
    result = db.execute(select(Vulnerability).where(
        Vulnerability.cve_id == cve_id))
    v = result.scalar_one_or_none()
    if v is None:
        raise HTTPException(404, detail="Vulnerability not found")
    else:
        v.severity = severity.severity
        db.commit()
        return v


@app.delete("/vulnerabilities/{cve_id}")
def delete_vul(cve_id: str, db: Session = Depends(get_db)):
    result = db.execute(select(Vulnerability).where(
        Vulnerability.cve_id == cve_id))
    v = result.scalar_one_or_none()
    if v is None:
        raise HTTPException(404, detail="Vulnerability Not Found")
    else:
        db.delete(v)
        db.commit()
        return {"message": "Vulnerability deleted successfully"}


Base.metadata.create_all(engine)
