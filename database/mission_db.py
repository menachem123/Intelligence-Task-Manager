from .db_connection import *

connect = get_connection()

class MissionDB:
    
    def create_mission(self,data):
        cursor = connect.cursor(dictionary=True)
        cursor.execute("INSERT INTO missions(" \
        "id, title, description, location, difficulty, importance ,status," \
        " risk_level,assigned_agent_id)" \
        " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (data[])
                       )
        connect.commit()
        cursor.close()












# get_all_missions()
# get_mission_by_id(id)
# assign_mission(m_id, a_id)
# update_mission_status(id, status)
# get_open_missions_by_agent(id)
# count_all_missions()
# count_by_status(status)
# count_open_missiocns()
# count_critical_missions()
# get_top_agent()

