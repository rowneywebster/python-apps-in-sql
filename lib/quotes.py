import requests

def get_todays_random_quote():
    results = requests.get("https://dummyjson.com/quotes/random").json()
    results_json = results.get("quote")
    return results_json

