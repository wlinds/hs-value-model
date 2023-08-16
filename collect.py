import requests
import pandas as pd

def get_cards(url):
    response = requests.get(url)

    if response.status_code == 200:
        cards = response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}")

    df = pd.DataFrame(cards)
    return df


if __name__ == "__main__":
    df = get_cards()
    print(df.head())