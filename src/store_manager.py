import os
import uuid
import datetime
from zoneinfo import ZoneInfo
import MySQLdb

class StoreManager:
    def __init__(self):
        self.__db = MySQLdb.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            passwd=os.environ.get("MYSQL_PASSWORD"),
            db=os.environ.get("MYSQL_DATABASE")
        )

        self.__cursor = self.__db.cursor()
    
    def show_table(self):
        self.__cursor.execute("SELECT * FROM main_app_store")
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)
        
        return rows

    def insert(self, place_id, name, type, open, photo_url, rating, price_level):
        try:
            id = str(uuid.uuid4()).replace("-","")
            record_datetime = datetime.datetime.now(ZoneInfo(key='Asia/Tokyo'))
            archive = 0
            recommend = 1
            number_of_reservation = 0
            
            query = f"INSERT INTO main_app_store VALUES('{id}', '{place_id}', '{name}', '{type}', '{open}', '{rating}', '{price_level}', '{record_datetime}', {archive}, {number_of_reservation}, {recommend}, '{photo_url}')"
            
            self.__cursor.execute(query)
            self.__db.commit()

            return True
        
        except Exception as e:
            print(e)
            return False
    
    def delete_all(self):
        try:
            query = f"DELETE FROM main_app_store"
            
            self.__cursor.execute(query)
            self.__db.commit()

            return True
        
        except Exception as e:
            print(e)
            return False
    