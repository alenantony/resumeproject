from nturl2path import url2pathname
from typing import List, Optional
from pydantic import BaseModel







class Profiles(BaseModel):
    network : Optional[str]
    username : Optional[str]
    url : Optional[str]

class Location(BaseModel):
    address : str
    postalCode : str
    city : str
    countryCode : str
    region : str

class Basics(BaseModel):
    name : str
    label : str
    image : str
    email : str
    phone : str
    url : str
    summary : str
    location : Location
    profiles : List[Profiles] = []


class Work(BaseModel):
    name : str
    location : str
    description : Optional[str]
    position : str
    url : str
    startDate : str
    endDate : str
    summary : str
    highlights : Optional[list]
    keywords : Optional[list]


class Volunteer(BaseModel):
    position : str
    url : str
    startDate : str
    endDate : str
    summary : str
    highlights : list


class Education(BaseModel):
    institution : str
    url : str
    area : str
    endDate : str
    score : float
    courses : list


class Awards(BaseModel):
    title : str
    date : str
    awarder : str
    summary : str



class Resume(BaseModel):
    id : Optional[int]
    coverLetter : Optional[str]
    basics : Basics
    work : List[Work] =[] #Optional[list]
    volunteer : List[Volunteer] =[] #Optional[list]
    education : List[Education] = [] #Optional[list]
    awards : List[Awards] #Optional[list]
    certificates : Optional[list]
    publications : Optional[list]
    skills : Optional[list]
    languages : Optional[list]
    interests : Optional[list]
    references : Optional[list]
    projects : Optional[list]
