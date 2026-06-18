from .db_connection import *

connect = get_connection()
# from logs.setup_logger import logger
class AgentDB:
    def create_agent(self,data):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("INSERT INTO(name, specialty, agent_rank) VALUES (%s,%s,%s)",
                           (data["name"], data["specialty"], data["agent_rank"]))
            #    (Menchem, lernen tora, Junior )
            connect.commit()
            id = cursor.lastrowid()
            row= cursor.execute("select * from agents where id = %s",(id,))
            cursor.close()
            return  row
        except Error as e:
            print(e) 
    def get_all_agents(self):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("select * from agents")
            all_agents = cursor.fetchall()
            cursor.close()
            return all_agents
        except Error as e:
            print(e) 
    def get_agent_by_id(self,id):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("SELECT * FROM agents WHERE id = %s",(id,))
            x = cursor.fetchall()
            cursor.close() 
            return x
        except Error as e:
            print(e)
            return None
    def update_agent(self, id, data):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("UPDATA agents SET data[name] = %s WHERE id = %s",(id,))
            cursor.close() 
            return {"message":"success"}
        except Error as e:
            return {"message":e}
    def deactivate_agent(self, id):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("UPDATA agents SET is_active = false WHERE id = %s",(id,))
            cursor.close() 
            return {"message":"success"}
        except Error as e:
            return {"message":e}
        
    
    def increment_completed(self, id):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("UPDATA agents SET completed_missions +=1 WHERE id = %s",(id,))
            cursor.close() 
            return {"message":"success"}
        except Error as e:
            return {"message":e}
    def increment_failed(self, id):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("UPDATA agents SET failed_missions -=1 WHERE id = %s",(id,))
            cursor.close() 
            return {"message":"success"}
        except Error as e:
            return {"message":e}
        
    def get_agent_performance(self, id):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("SELECT * FROM agents WHERE id = %s",(id,))
            x = cursor.fetchall()
            completed=
            failed= 
            total=
            success_rate =(completed / total) *100
            cursor.close() 
            dic_ret ={completed:{completed},failed:{failed},total:{total},success_rate:{success_rate}}
            return dic_ret
        except Error as e:
            print(e)
            return None
    def count_active_agents(self):
        try:
            cursor = connect.cursor(dictionary=True)
            cursor.execute("SELECT COUNTE (*) FROM agents WHERE is_active = True")
            count_active = cursor.fetchall()
            cursor.close() 
            return {"message":{count_active}}
        except Error as e:
            return {"message":e}
