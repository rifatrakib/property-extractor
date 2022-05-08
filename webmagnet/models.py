from datetime import datetime
from pydantic import BaseModel
from typing import conlist, Dict


class GeometryModel(BaseModel):
    type: str
    coordinates: conlist(float, min_items=2, max_items=2)


class PropertyModel(BaseModel):
    id: str
    serial_number: int
    list_year: int
    date_recorded: str
    town: str
    address: str
    assessed_value: float
    sales_amount: float
    sales_ratio: float
    property_type: str
    residential_type: str
    non_use_code: str
    remarks: str
    opm_remarks: str
    geo_coordinates: Dict[GeometryModel]


def AutomobileModel(BaseModel):
    id: str
    business_name: str
    business_address: str
    city: str
    state: str
    zip_code: str
    license_num: str
    license_type: str
    license_expiration: datetime
    geo_coordinates: Dict[GeometryModel]
