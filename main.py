import openpyxl
import pandas as pd
from openai import OpenAI
import os

class NovaExcelAnalyst:
    """
    NOVA Excel AI Analyst Plugin
    Intelligently process, compare, and model spreadsheet data using generative AI.
    """
    def __init__(self, api_key=None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def analyze_sheet(self, file_path, sheet_name=0):
        print(f"--- Loading workbook {file_path} ---")
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        data_summary = df.describe(include='all').to_string()
        
        prompt = f"""
        You are NOVA, the institutional finance AI analyst. Here is a summary of our spreadsheet data:
        {data_summary}
        
        Provide:
        1. Top 3 key business insights.
        2. Potential data anomalies or outliers.
        3. Recommended financial forecasting models to apply.
        """
        print("--- Running NOVA Analysis ---")
        res = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content

if __name__ == "__main__":
    analyst = NovaExcelAnalyst(api_key="mock-api-key")
    print("NOVA Excel AI Analyst loaded successfully!")
