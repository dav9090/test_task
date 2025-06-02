from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models import Activity, Organization, organization_activity
from schemas import OrganizationSchema
from dependencies import get_db

router = APIRouter(prefix="/activities", tags=["Activities"])

def get_descendant_ids(activity: Activity) -> list[int]:
    ids = [activity.id]
    for child in activity.children:
        ids.extend(get_descendant_ids(child))
    return ids

@router.get("/{activity_id}/organizations", response_model=list[OrganizationSchema], summary="Get organizations by activity ID", description="Возвращает все организации, связанные с указанным видом деятельности и его вложенными подкатегориями.")
def get_organizations_by_activity(activity_id: int, db: Session = Depends(get_db)):
    activity = db.query(Activity).get(activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    ids = get_descendant_ids(activity)
    return db.query(Organization).join(organization_activity).filter(organization_activity.c.activity_id.in_(ids)).all()

@router.get("/by-name", response_model=list[OrganizationSchema], summary="Get organizations by activity name", description="Поиск организаций по названию вида деятельности. Включает вложенные подкатегории (до 3 уровней).")
def get_organizations_by_activity_name(query: str = Query(...), db: Session = Depends(get_db)):
    activity = db.query(Activity).filter(Activity.name.ilike(f"%{query}%")).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    ids = get_descendant_ids(activity)
    return db.query(Organization).join(organization_activity).filter(organization_activity.c.activity_id.in_(ids)).all()