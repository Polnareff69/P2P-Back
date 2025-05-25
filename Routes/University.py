# Routers/university.py

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from Schemas.university import UniversityCreate, UniversityUpdate, UniversityOut
from Services.University import UniversityService
from Utils.Auth import verify_token

university = APIRouter(tags=["Universidades"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@university.post('/university', response_model=UniversityOut)
def create_university(data: UniversityCreate, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        university_created = UniversityService.create_university(data)
        return UniversityOut.model_validate(university_created)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@university.get('/university/{university_id}', response_model=UniversityOut)
def get_university_by_id(university_id: UUID):
    university = UniversityService.get_university_by_id(university_id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return UniversityOut.model_validate(university)


@university.get('/universities', response_model=list[UniversityOut])
def get_all_universities():
    return UniversityService.get_all_universities()


@university.put('/university/{university_id}', response_model=UniversityOut)
def update_university(university_id: UUID, data: UniversityUpdate):
    updated = UniversityService.update_university(university_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="University not found")
    return UniversityOut.model_validate(updated)


@university.delete('/university/{university_id}')
def delete_university(university_id: UUID):
    result = UniversityService.delete_university(university_id)
    if not result:
        raise HTTPException(status_code=404, detail="University not found")
    return JSONResponse(status_code=200, content={"message": "University deleted successfully"})
