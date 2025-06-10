# utils/congress_api.py

import os
import requests

API_KEY = os.getenv("CONGRESS_API_KEY")  
BASE_URL = "https://api.congress.gov/v3"

def search_bills(query, limit=10):
    """
    Search for bills matching the query.
    """
    endpoint = f"{BASE_URL}/bill"
    params = {
        "query": query,
        "limit": limit,
        "api_key": API_KEY
    }
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()

def get_bill_details(congress, bill_type, bill_number):
    """
    Retrieve detailed information about a specific bill.
    """
    endpoint = f"{BASE_URL}/bill/{congress}/{bill_type}/{bill_number}"
    params = {
        "api_key": API_KEY
    }
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()
