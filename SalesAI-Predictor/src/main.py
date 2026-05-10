from data_loader import load_crm_data, load_market_data, merge_data
from multi_agent_manager import MultiAgentManager
import pandas as pd

if __name__ == "__main__":
    crm_data = load_crm_data()
    market_data = load_market_data()
    merged_data = merge_data(crm_data, market_data)
    
    features = ['Marketing_Spend', 'Previous_Sales']
    target = 'Sales'
    
    manager = MultiAgentManager()
    forecast, strategies = manager.run_pipeline(merged_data, features, target)
    
    # 保存预测报告
    merged_data['Forecast'] = forecast
    merged_data.to_excel("outputs/forecast_report.xlsx", index=False)
    
    with open("outputs/strategy_recommendation.txt", "w") as f:
        for s in strategies:
            f.write(s + "\n")
    
    print("预测和策略生成完成！")
