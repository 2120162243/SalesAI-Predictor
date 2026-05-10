from predictor import SalesPredictor
from strategy_agent import StrategyAgent

class MultiAgentManager:
    def __init__(self):
        self.predictor = SalesPredictor()
        self.strategy_agent = StrategyAgent()
    
    def run_pipeline(self, data, features, target):
        self.predictor.train(data, features, target)
        forecast = self.predictor.predict(data, features)
        strategies = self.strategy_agent.generate_strategy(forecast)
        return forecast, strategies
