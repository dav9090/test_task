from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models import Organization, Building
from schemas import OrganizationSchema
from dependencies import get_db
from utils import haversine

router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.get("/search", response_model=list[OrganizationSchema], summary="Search organizations by name", description="Поиск организаций по части названия (регистронезависимо).")
def search_organizations(name: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(Organization)
    if name:
        query = query.filter(Organization.name.ilike(f"%{name}%"))
    return query.all()

@router.get("/near", response_model=list[OrganizationSchema], summary="Find organizations near location", description="Поиск организаций по координатам и радиусу (в километрах). Используется haversine-фильтрация.")
def organizations_near(lat: float, lon: float, radius_km: float = 1.0, db: Session = Depends(get_db)):
    buildings = db.query(Building).all()
    near_ids = [b.id for b in buildings if haversine(lat, lon, b.latitude, b.longitude) <= radius_km]
    return db.query(Organization).filter(Organization.building_id.in_(near_ids)).all()

@router.get("/{org_id}", response_model=OrganizationSchema, summary="Get organization by ID", description="Получить полную информацию об организации по её ID.")
def get_organization(org_id: int, db: Session = Depends(get_db)):
    org = db.query(Organization).get(org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Not found")
    return org
