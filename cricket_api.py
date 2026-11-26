import requests
import streamlit as st

BASE_URL = "https://api.datasportsapi.com"


def get_api_key():
    return st.secrets["DATASPORTSAPI_KEY"]


def api_get(endpoint, params=None):
    headers = {
        "Authorization": f"Bearer {get_api_key()}"
    }

    response = requests.get(
        f"{BASE_URL}{endpoint}",
        headers=headers,
        params=params,
        timeout=20
    )

    response.raise_for_status()
    return response.json()


def get_cricket_fixtures(date):
    return api_get(
        "/v2/fixtures",
        params={
            "date": str(date),
            "sport": "cricket"
        }
    )


def get_live_cricket_scores():
    return api_get(
        "/v2/livescores",
        params={
            "sport": "cricket"
        }
    )


def get_fixture_details(fixture_id):
    return api_get(f"/v2/fixtures/{fixture_id}")


def get_fixture_lineups(fixture_id):
    return api_get(f"/v2/fixtures/{fixture_id}/lineups")


def get_fixture_scorecard(fixture_id):
    return api_get(f"/v2/fixtures/{fixture_id}/scorecard")
