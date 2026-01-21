from pydantic import BaseModel
from datetime import datetime
import mysql.connector
from typing import List



class Base_data(BaseModel):
    timestamp: datetime
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int


class Extra_data(Base_data):
    temperature_category: str 
    wind_category: str 

List[Extra_data]



DB_CONFIG = {'host': 'localhost', 'user': 'root', 'password': 'pass', 'database': 'weather'}
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()




def create_table_if_not_exists():
    """Creates the records_weather table"""
    try:
        
        query = """
        CREATE TABLE IF NOT EXISTS records_weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            location_name VARCHAR(100),
            country VARCHAR(100),
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            wind_speed FLOAT,
            humidity INT,
            temperature_category VARCHAR(100),
            wind_category VARCHAR(100)
        )
        """
        
        cursor.execute(query)
        conn.commit()
        print("Table created")
        
    except Exception as e:
        print(f"Error: {e}")
        


def insert_all_records(records):
    """Insert all records from list into database"""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        query = """
        INSERT INTO records_weather 
        (timestamp, location_name, country, latitude, longitude, temperature, wind_speed, humidity, temperature_category, wind_category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        for record in records:
            params = (
                record["timestamp"],
                record["location_name"],
                record["country"],
                record["latitude"],
                record["longitude"],
                record["temperature"],
                record["wind_speed"],
                record["humidity"],
                record["temperature_category"],
                record["wind_category"]
            )
            cursor.execute(query, params)
        
        conn.commit()
        print(f"Inserted {len(records)} records")
        
    except Exception as e:
        print(f"Error inserting: {e}")
        if conn:
            conn.rollback()


def setup(records: List[dict] = None):  
    create_table_if_not_exists()
    
    if records is None:
        records = list_of_dicts.copy()  
    
    pydantic_records = [Extra_data(**record) for record in records]
    
    insert_all_records([r.model_dump() for r in pydantic_records])
    
    print(f"✓ Setup complete: {len(pydantic_records)} validated records")
    return pydantic_records  


class Querys:

    @staticmethod
    def get_all():
        # endpoint: GET /records
        query = """
            SELECT * 
            FROM records_weather
            """
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    @staticmethod
    def count_by_region():
        # endpoint: GET /records/count
        query = """
            SELECT location_name ,COUNT(*) as count 
            FROM records_weather
            GROUP BY location_name
            ORDER BY count DESC 
            """
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    @staticmethod
    def avg_temp_by_region():
        # endpoint: GET /records/avg-temperature
        query = """
            SELECT location_name, AVG(temperature) 
            FROM records_weather
            GROUP BY location_name
            """
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    
    @staticmethod
    def max_wind_by_region():
        # endpoint: GET /records/max-wind
        query = """
            SELECT location_name, MAX(wind_speed) 
            FROM records_weather
            GROUP BY location_name
            """
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    
    @staticmethod
    def extreme_locations():
        # endpoint: /records/extreme
        query = """
            SELECT * 
            FROM records_weather
            WHERE (temperature_category = 'hot' AND  wind_category = 'calm')
            OR
            (temperature_category = 'cold' AND  wind_category = 'windy')
            ORDER BY timestamp DESC
            """
        cursor.execute(query)
        records = cursor.fetchall()
        return records


# Run it
setup()






cursor.close()
conn.close()



