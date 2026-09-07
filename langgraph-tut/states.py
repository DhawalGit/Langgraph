#Very first step - creating a graph and a state
import os
#1) typed DICT - most common approach
from typing import TypedDict
class State(TypedDict):
    topic :str
    summary: str
    score: str

#2) Pydantic aproach - its good in data validation and type checking at runtime
from pydantic import BaseModel, field_validator
class State(BaseModel):
    topic :str
    score: str
    summary: str = ""

    @field_validator
    def score_positive(cls, v):
        if v < 0:
            raise ValueError("Score must be positive")

#python data classes but it is used very rarely
from dataclasses import dataclass, field
@dataclass
class State(dataclass):
    topic : str = ""
    summary : str
    messages : list = field(default_factory=list)
    