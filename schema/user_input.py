from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    age: int  = Field(..., gt=0, lt=120, description='Age of the user')
    weight: float = Field(..., gt=0, description='Weight of user in kg', )
    height: float = Field(..., gt=0, description='Height of user in m', )
    income_lpa: float = Field(..., ge=0, description='Annual income in LPA', )
    smoker: bool = Field(..., description='Whether the user is a smoker', )
    city: str = Field(..., description='City of residence', )
    occupation: Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'] = Field(...,  description='User occupation',)

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @field_validator('city')
    @classmethod
    def normalize_city(cls, val: str) -> str:
        val = val.strip().title()
        return val