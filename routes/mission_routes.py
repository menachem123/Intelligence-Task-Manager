from fastapi import APIRouter 
from database.mission_db import MissionDB, logger

missiondb = MissionDB()
router = APIRouter(prefix="/missions")

@router.post("")
def create_mission(data:dict):
    logger.debug("create mission")
    return missiondb.create_mission(data)

@router.get("")
def get_all_missions():
    logger.debug("return all missions")
    return missiondb.get_all_missions()
@router.get("/{id}")
def get_mission_by_id(id):
    logger.debug(" return mission by id")
    return missiondb.get_mission_by_id(id)

@router.put("/{id}/start")
def update_mission_status_to_start(id:int):
    return missiondb.update_mission_status(id,status="ASSIGNED")

@router.put("/{id}/complete")
def update_mission_status_to_completed(id:int):
    return missiondb.update_mission_status(id,status="completed")