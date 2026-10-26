from typing import Optional, Literal

from pydantic import BaseModel, AnyUrl, EmailStr, Field, field_validator, ValidationError, model_validator, \
    computed_field
import datetime

class Location(BaseModel):
    city: str
    country: str

class JobApplication(BaseModel):
    company: str
    role: str
    job_url: AnyUrl
    recruiter_email: Optional[EmailStr] = None
    status: Literal["Applied", "Assessment", "Interview", "Offer", "Rejected"]
    salary: Optional[int] = Field(default=None, gt=0)
    applied_on: datetime.date
    location: Location


    @field_validator("company")
    @classmethod
    def company_validator(cls, v):
        if v and v.strip():
            company_name = v.strip().title()
            return company_name
        else:
            raise ValueError("Company name is required")

    @model_validator(mode="after")
    def salary_validator(self):
        if self.status == "Offer":
            if self.salary is None:
                raise ValueError("Salary is required")
        return self

    @computed_field
    @property
    def days_since_applied(self) -> int:
        if self.applied_on:
            today = datetime.date.today()
            difference = today - self.applied_on
            return difference.days
        else:
            raise ValueError("Job date is required")







