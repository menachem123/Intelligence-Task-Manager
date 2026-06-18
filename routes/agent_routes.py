from fastapi import APIRouter
from database.agent_db import AgentDB, logger

agentdb = AgentDB()
router = APIRouter(prefix="/agents")

@router.post("")
def create_agent(data:dict):
    logger.debug("create asent")
    return agentdb.create_agent(data)

@router.get("")
def get_all_agents():
    logger.debug("retern all agents")
    return agentdb.get_all_agents()

@router.get("/{id}")
def get_agent_by_id(id):
    logger.debug("retern agent by id")
    return agentdb.get_agent_by_id(id)

@router.put("/{id}/deactivate")
def deactivate_agent_to_false(id:int):
    return agentdb.deactivate_agent(id)

