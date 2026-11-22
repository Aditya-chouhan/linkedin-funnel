"""
LinkedIn Funnel — Full-Funnel LinkedIn Growth & Pipeline Engineering System.
Created by Aditya Chouhan.
"""

from .qualification import qualify_prospect
from .validator import verify_repository
from .waterfall import generate_waterfall_plan

__version__ = "0.1.0"
__author__ = "Aditya Chouhan"
__all__ = ["qualify_prospect", "generate_waterfall_plan", "verify_repository"]
