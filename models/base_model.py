#!/usr/bin/python3
"""
This File defines the BaseModel class that will
serve as the base class for all our models."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):
        """constructor it either deserialize
        a serialized class or initialize a new"""
