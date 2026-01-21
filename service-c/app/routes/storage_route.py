from fastapi import routing, Depends
from models.weather import WeatherModel
from typing import List
from core.db import get_cursor
from service.weather_service import StorageService


router = routing.APIRouter(prefix="/records", tags=["records"])


@router.post('')
def create_records(data: List[WeatherModel], cursor = Depends(get_cursor)):
    return StorageService(cursor).insert_all_records(data)

@router.get('')
def get_all_records(cursor = Depends(get_cursor)):
    return StorageService(cursor).get_all()

@router.get('/count')
def get_records_count(cursor = Depends(get_cursor)):
    return StorageService(cursor).count_by_region()

@router.get('/avg-temperature')
def get_avg_temp(cursor = Depends(get_cursor)):
    return StorageService(cursor).avg_temp_by_region()

@router.get('/max-wind')
def get_max_wind(cursor = Depends(get_cursor)):
    return StorageService(cursor).max_wind_by_region()

@router.get('/extreme')
def get_extreme(cursor = Depends(get_cursor)):
    return StorageService(cursor).extreme_locations()

