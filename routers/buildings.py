from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Building, Organization
from schemas import BuildingSchema, OrganizationSchema
from dependencies import get_db

router = APIRouter(prefix="/buildings", tags=["Buildings"])

@router.get("/", response_model=list[BuildingSchema], summary="List all buildings", description="Получить список всех зданий с координатами и адресами.")
def list_buildings(db: Session = Depends(get_db)):
    return db.query(Building).all()

@router.get("/{building_id}/organizations", response_model=list[OrganizationSchema], summary="Organizations in building", description="Получить список организаций, расположенных в указанном здании.")
def get_organizations_by_building(building_id: int, db: Session = Depends(get_db)):
    return db.query(Organization).filter(Organization.building_id == building_id).all()
