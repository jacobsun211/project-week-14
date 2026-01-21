
class StorageService:

    def __init__(self, cursor):
        self.cursor = cursor


    def get_all(self):
        # endpoint: GET /records
        query = """
            SELECT * 
            FROM records_weather
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def count_by_region(self):
        # endpoint: GET /records/count
        query = """
            SELECT location_name ,COUNT(*) as count 
            FROM records_weather
            GROUP BY location_name
            ORDER BY count DESC 
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def avg_temp_by_region(self):
        # endpoint: GET /records/avg-temperature
        query = """
            SELECT location_name, AVG(temperature) 
            FROM records_weather
            GROUP BY location_name
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def max_wind_by_region(self):
        # endpoint: GET /records/max-wind
        query = """
            SELECT location_name, MAX(wind_speed) 
            FROM records_weather
            GROUP BY location_name
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def extreme_locations(self):
        # endpoint: /records/extreme
        query = """
            SELECT * 
            FROM records_weather
            WHERE (temperature_category = 'hot' AND  wind_category = 'calm')
            OR
            (temperature_category = 'cold' AND  wind_category = 'windy')
            ORDER BY timestamp DESC
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    #     self.cursor = cursor

    def get_all(self):
        # endpoint: GET /records
        query = """
            SELECT * 
            FROM records_weather
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def count_by_region(self):
        # endpoint: GET /records/count
        query = """
            SELECT location_name ,COUNT(*) as count 
            FROM records_weather
            GROUP BY location_name
            ORDER BY count DESC 
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def avg_temp_by_region(self):
        # endpoint: GET /records/avg-temperature
        query = """
            SELECT location_name, AVG(temperature) 
            FROM records_weather
            GROUP BY location_name
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def max_wind_by_region(self):
        # endpoint: GET /records/max-wind
        query = """
            SELECT location_name, MAX(wind_speed) 
            FROM records_weather
            GROUP BY location_name
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def extreme_locations(self):
        # endpoint: /records/extreme
        query = """
            SELECT * 
            FROM records_weather
            WHERE (temperature_category = 'hot' AND  wind_category = 'calm')
            OR
            (temperature_category = 'cold' AND  wind_category = 'windy')
            ORDER BY timestamp DESC
            """
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def insert_all_records(self, records):
    
        query = """
        INSERT INTO records_weather 
        (timestamp, location_name, country, latitude, longitude, temperature, wind_speed, humidity, temperature_category, wind_category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = []

        for record in records:
            params.insert (
                (
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
            )

            self.cursor.executemany(query, params)
    