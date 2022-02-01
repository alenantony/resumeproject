from datetime import date
import re
from typing import List, Optional
from pydantic import BaseModel, validator


class Profiles(BaseModel):
    network: Optional[str]
    username: Optional[str]
    url: Optional[str]


class Location(BaseModel):
    address: str
    postalCode: str
    city: str
    countryCode: str
    region: str


class Basics(BaseModel):
    name: str
    label: str
    image: str
    email: str
    phone: str
    url: str
    summary: str
    location: Location
    profiles: List[Profiles]

    @validator('email')
    def email_validation(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            return True
        else:
            print("Invalid Email")
            return False


class Work(BaseModel):
    name: str
    location: str
    description: Optional[str]
    position: str
    url: str
    startDate: str
    endDate: str
    summary: str
    highlights: Optional[list]
    keywords: Optional[list]


class Volunteer(BaseModel):
    organization: str
    position: str
    url: str
    startDate: str
    endDate: str
    summary: str
    highlights: list


class Education(BaseModel):
    institution: str
    url: str
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
    url: str
    issuer: str


class Publications(BaseModel):
    name: str
    publisher: str
    releaseDate: str
    url: str
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
    id: Optional[int]
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
