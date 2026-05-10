class StrategyAgent:
    def generate_strategy(self, forecast):
        strategies = []
        for value in forecast:
            if value > 1000:
                strategies.append("Increase inventory and marketing spend")
            else:
                strategies.append("Focus on targeted promotions")
        return strategies
