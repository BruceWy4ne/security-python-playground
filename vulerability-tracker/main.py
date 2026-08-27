from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from typing import Literal

app = FastAPI()

vul = []


class Message(BaseModel):
    username: str
    message: Optional[str] = None


class Define_sev(BaseModel):
    severity: Literal["High", "Low", "Medium", "Critical"]


class Define_Vul(BaseModel):
    cve_id: str
    severity: Literal["High", "Low", "Medium", "Critical"]
    description: Optional[str] = None


@app.post("/vulnerabilites", status_code=201)
def Vulner(v: Define_Vul):
    vul.append(v)
    return v


@app.post("/message")
def mes(m: Message):
    return m


@app.get("/")
def home():
    return {"message": "Vulnerability Tracker API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/about")
def about_me():
    return {"project": "Vulnerability Tracker", "Version": "1.0"}


@app.get("/search")
def search(severity: str, status: str):
    return {
        "severity": severity,
        "status": status
    }


@app.get("/vulnerabilities/{cve}")
def get_vulnerability(cve: str):
    for i in vul:
        if i.cve_id == cve:
            return i
    raise HTTPException(404, detail="Vul not found")


@app.put("/vulnerabilities/{cve_id}")
def put_sev(cve_id: str, data: Define_sev):
    for i in vul:
        if i.cve_id == cve_id:
            i.severity = data.severity
            return i
    raise HTTPException(404, detail="Vulnerabiliy not found")


@app.delete("/vulnerabilities/{cve_id}")
def del_vul(cve_id: str):
    for i in vul:
        if i.cve_id == cve_id:
            vul.remove(i)
            return "Removed"
    raise HTTPException(404, detail="CVE not found")
