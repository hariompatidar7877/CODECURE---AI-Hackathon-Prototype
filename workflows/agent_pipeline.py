from agents.data_agent import DataAgent
from agents.trend_agent import TrendAgent
from agents.prediction_agent import PredictionAgent
from agents.hotspot_agent import HotspotAgent
from agents.explanation_agent import ExplanationAgent
from agents.policy_agent import PolicyAgent
from utils.feature_engineering import add_features


class AgentPipeline:

    def __init__(self):
        self.data_agent = DataAgent()
        self.trend_agent = TrendAgent()
        self.prediction_agent = PredictionAgent()
        self.hotspot_agent = HotspotAgent()
        self.explainer = ExplanationAgent()
        self.policy_agent = PolicyAgent()

    def run(self, country):

        df = self.data_agent.fetch(country)
        df = add_features(df)

        trend = self.trend_agent.analyze(df)
        prediction = self.prediction_agent.predict(df)
        risk = self.hotspot_agent.detect(df)

        explanation = self.explainer.explain(trend, risk)
        policy = self.policy_agent.suggest(risk)

        return prediction, trend, risk, explanation, policy
