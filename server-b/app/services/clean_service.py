from datetime import datetime
import pandas as pd
import numpy as np

from models.weather_model import WeatherInModel


from external_api.registry_server_c import get_resource as get_server_c_resource


class WeatherService:


    def convert_to_df(self, data: WeatherInModel) -> pd.DataFrame:
        data = data.model_dump(mode='json').get('data')
        print(type(data))
        return pd.DataFrame(data)
        

    def clean_data(self, df: pd.DataFrame):
        pass


    def crate_category_temperature(self, df: pd.DataFrame):

        conditions = [df['temperature'] > 25,
                      (df['temperature'] >= 18) & (df['temperature'] <= 25)]

        choices = ['hot', 'moderate']

        df['temperature_category'] = np.select(
            conditions,
            choices,
            default='cold'
        )
        
    
    def crate_status_wind(self, df: pd.DataFrame):

        conditions =  [10 <= df['wind_speed']]
        
        choices = ['windy']

        df['wind_category'] = np.select(conditions, choices, default='calm')

    
    async def handle_clean_pipeline(self, data: WeatherInModel) -> list[dict]:
        df = self.convert_to_df(data)

        self.clean_data(df)
        self.crate_category_temperature(df)
        self.crate_status_wind(df)

        res = await get_server_c_resource('create').call(json=df.to_dict(orient='records'))

        return res.data



