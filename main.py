from database.db_connection import create_tables
# from database.agent_db import AgentDB
from database.mission_db import MissionDB
# agentdb = AgentDB()
# agentdb.create_agent()
# agentdb.create_agent({"name": "menachm" ,"specialty": "tora", "agent_rank":"Junior"})
# agentdb.get_all_agents()

missiondb = MissionDB()
missiondb.create_mission()