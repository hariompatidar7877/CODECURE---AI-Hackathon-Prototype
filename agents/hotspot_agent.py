from config import HOTSPOT_THRESHOLD

class HotspotAgent:

    def detect(self, df):
        growth = df['growth_rate'].iloc[-1]

        if growth > HOTSPOT_THRESHOLD:
            return "High Risk"
        elif growth > 0.05:
            return "Medium Risk"
        else:
            return "Low Risk"
