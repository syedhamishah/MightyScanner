import requests

class ThreatIntelligence:
    def fetch_threats(self):
        response = requests.get("https://threatfeed.api")
        return response.json()
