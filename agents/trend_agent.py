class TrendAgent:

    def analyze(self, df):
        latest_growth = df['growth_rate'].iloc[-1]

        if latest_growth > 0.1:
            return "Increasing"
        elif latest_growth < -0.1:
            return "Decreasing"
        else:
            return "Stable"
