from datetime import date
import re
from typing import List, Optional
from pydantic import AnyUrl, BaseModel, EmailStr, validator
from starlette.responses import JSONResponse

class Profiles(BaseModel):
    network: Optional[str]
    username: Optional[str]
    url: AnyUrl


class Location(BaseModel):
    address: str
    postalCode: str
    city: str
    countryCode: str
    region: str


class Basics(BaseModel):
    name: str
    label: str
    image: AnyUrl
    email: EmailStr
    phone: str
    url: AnyUrl
    summary: str
    location: Location
    profiles: List[Profiles]

    # @validator('email')
    # def email_validation(cls, v):
    #     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #     if (re.fullmatch(regex, v)):
    #         return True
    #     else: 
    #         raise ValueError("Email not valid")

    # @validator('image')
    # def image_validation(cls, v):
    #     regex
        

        # a.append("email error")
        # return v
        # else: 
        #     raise ValueError("Email not valid")
        # return v
        #     # return False 


class Work(BaseModel):
    name: str
    location: str
    description: Optional[str]
    position: str
    url: AnyUrl
    startDate: str
    endDate: str
    summary: str
    highlights: Optional[List[str]]
    keywords: Optional[List[str]]


class Volunteer(BaseModel):
    organization: str
    position: str
    url: AnyUrl
    startDate: str
    endDate: str
    summary: str
    highlights: List[str]


class Education(BaseModel):
    institution: str
    url: AnyUrl
    area: str
    studyType: str
    startDate: str
    endDate: str
    score: float
    courses: list


class Awards(BaseModel):
    title: str
    date: str
    awarder: str
    summary: str


class Certificates(BaseModel):
    name: str
    date: str
    url: AnyUrl
    issuer: str


class Publications(BaseModel):
    name: str
    publisher: str
    releaseDate: str
    url: AnyUrl
    summary: str


class Skills(BaseModel):
    name: str
    level: str
    keywords: list


class Languages(BaseModel):
    language: str
    fluency: str


class Interests(BaseModel):
    name: str
    keywords: List[str]


class References(BaseModel):
    name: str
    reference: str


class Projects(BaseModel):
    name: str
    description: str
    highlights: List[str]
    keywords: List[str]
    startDate: str
    endDate: str
    url: str
    roles: List[str]
    entity: str
    type: str


class Resume(BaseModel):
    id: Optional[str]
    coverLetter: Optional[str]
    basics: Basics
    work: Optional[List[Work]] #Optional[list]
    volunteer: Optional[List[Volunteer]] #Optional[list]
    education: List[Education] #Optional[list]
    awards: Optional[List[Awards]] #Optional[list]
    certificates: Optional[List[Certificates]] #Optional[list]
    publications: Optional[List[Publications]] #Optional[list]
    skills: List[Skills] #Optional[list]
    languages: List[Languages] #Optional[list]
    interests: Optional[List[Interests]]
    references: Optional[List[References]] #Optional[list]
    projects: Optional[List[Projects]] #Optional[list]
