from utils.preprocessing import load_data, filter_country, handle_missing
from config import DATA_PATH

class DataAgent:

    def fetch(self, country):
        df = load_data(DATA_PATH)
        df = filter_country(df, country)
        df = handle_missing(df)
        return df
