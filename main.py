from typing import Optional

from fastapi import FastAPI
import joblib
import pickle


import pandas as pd
import numpy as np


app = FastAPI() # 建立一個 Fast API application

@app.get("/") # 指定 api 路徑 (get方法)
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}") # 指定 api 路徑 (get方法)
def read_user(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}


@app.get("/date/{year}/{month}") # 指定 api 路徑 (get方法)
def read_price_date(year: str, month: str):
    yearMonth = year +'/'+ month
    stock = pd.read_excel('corporate_rating.xlsx')
    price = stock.iloc[:, 4][stock.iloc[:, 0] == yearMonth]
    return {"price": price.to_string(index=False)}


@app.get("/rating1/{Sector}/{currentRatio}/{quickRatio}/{cashRatio}/{daysOfSalesOutstanding}/{netProfitMargin}/{pretaxProfitMargin}/{grossProfitMargin}/{operatingProfitMargin}/{returnOnAssets}/{returnOnCapitalEmployed}/{returnOnEquity}/{assetTurnover}/{fixedAssetTurnover}/{debtEquityRatio}/{debtRatio}/{effectiveTaxRate}/{freeCashFlowOperatingCashFlowRatio}/{freeCashFlowPerShare}/{cashPerShare}/{companyEquityMultiplier}/{ebitPerRevenue}/{enterpriseValueMultiple}/{operatingCashFlowPerShare}/{operatingCashFlowSalesRatio}/{payablesTurnover}")
def read_price_date1(Sector: str, currentRatio: float, quickRatio: float, cashRatio: float, daysOfSalesOutstanding: float, netProfitMargin: float, pretaxProfitMargin: float, grossProfitMargin: float, operatingProfitMargin: float, returnOnAssets: float, returnOnCapitalEmployed: float, returnOnEquity: float, assetTurnover: float, fixedAssetTurnover: float, debtEquityRatio: float, debtRatio: float, effectiveTaxRate: float, freeCashFlowOperatingCashFlowRatio: float, freeCashFlowPerShare: float, cashPerShare: float, companyEquityMultiplier: float, ebitPerRevenue: float, enterpriseValueMultiple: float, operatingCashFlowPerShare: float, operatingCashFlowSalesRatio: float, payablesTurnover: float):
    #LR_model = joblib.load('LR_model')
    LR_model = pickle.load(open('LR_model', "rb"))


    Sector_name_mapping = {'Basic Industries': 0,
                'Capital Goods': 1,
                'Consumer Durables': 2,
                'Consumer Non-Durables': 3,
                'Consumer Services': 4,
                'Energy': 5,
                'Finance': 6,
                'Health Care': 7,
                'Miscellaneous': 8,
                'Public Utilities': 9,
                'Technology': 10,
                'Transportation': 11}
    
    Sector_ = Sector_name_mapping[Sector]
    
    y_pred_LR = LR_model.predict(np.array([[Sector_, currentRatio, quickRatio, cashRatio, daysOfSalesOutstanding, netProfitMargin, pretaxProfitMargin, grossProfitMargin, 
                                  operatingProfitMargin, returnOnAssets, returnOnCapitalEmployed, returnOnEquity, assetTurnover, fixedAssetTurnover, debtEquityRatio, 
                                  debtRatio, effectiveTaxRate, freeCashFlowOperatingCashFlowRatio, freeCashFlowPerShare, cashPerShare, companyEquityMultiplier, 
                                  ebitPerRevenue, enterpriseValueMultiple, operatingCashFlowPerShare, operatingCashFlowSalesRatio, payablesTurnover],]))
    

    Sector_name_mapping = {0: 'A',
                           1: 'AA',
                           2: 'AAA',
                           3: 'B',
                           4: 'BB',
                           5: 'BBB',
                           6: 'C',
                           7: 'CC',
                           8: 'CCC',
                           9: 'D'}

    return {"Rating1": Sector_name_mapping[y_pred_LR[0]]}

@app.get("/rating2/{Sector}/{currentRatio}/{quickRatio}/{cashRatio}/{daysOfSalesOutstanding}/{netProfitMargin}/{pretaxProfitMargin}/{grossProfitMargin}/{operatingProfitMargin}/{returnOnAssets}/{returnOnCapitalEmployed}/{returnOnEquity}/{assetTurnover}/{fixedAssetTurnover}/{debtEquityRatio}/{debtRatio}/{effectiveTaxRate}/{freeCashFlowOperatingCashFlowRatio}/{freeCashFlowPerShare}/{cashPerShare}/{companyEquityMultiplier}/{ebitPerRevenue}/{enterpriseValueMultiple}/{operatingCashFlowPerShare}/{operatingCashFlowSalesRatio}/{payablesTurnover}")
def read_price_date2(Sector: str, currentRatio: float, quickRatio: float, cashRatio: float, daysOfSalesOutstanding: float, netProfitMargin: float, pretaxProfitMargin: float, grossProfitMargin: float, operatingProfitMargin: float, returnOnAssets: float, returnOnCapitalEmployed: float, returnOnEquity: float, assetTurnover: float, fixedAssetTurnover: float, debtEquityRatio: float, debtRatio: float, effectiveTaxRate: float, freeCashFlowOperatingCashFlowRatio: float, freeCashFlowPerShare: float, cashPerShare: float, companyEquityMultiplier: float, ebitPerRevenue: float, enterpriseValueMultiple: float, operatingCashFlowPerShare: float, operatingCashFlowSalesRatio: float, payablesTurnover: float):
    #LR_model = joblib.load('LR_model')
    LR_model = pickle.load(open('GBT_model', "rb"))


    Sector_name_mapping = {'Basic Industries': 0,
                'Capital Goods': 1,
                'Consumer Durables': 2,
                'Consumer Non-Durables': 3,
                'Consumer Services': 4,
                'Energy': 5,
                'Finance': 6,
                'Health Care': 7,
                'Miscellaneous': 8,
                'Public Utilities': 9,
                'Technology': 10,
                'Transportation': 11}
    
    Sector_ = Sector_name_mapping[Sector]
    
    y_pred_LR = LR_model.predict(np.array([[Sector_, currentRatio, quickRatio, cashRatio, daysOfSalesOutstanding, netProfitMargin, pretaxProfitMargin, grossProfitMargin, 
                                  operatingProfitMargin, returnOnAssets, returnOnCapitalEmployed, returnOnEquity, assetTurnover, fixedAssetTurnover, debtEquityRatio, 
                                  debtRatio, effectiveTaxRate, freeCashFlowOperatingCashFlowRatio, freeCashFlowPerShare, cashPerShare, companyEquityMultiplier, 
                                  ebitPerRevenue, enterpriseValueMultiple, operatingCashFlowPerShare, operatingCashFlowSalesRatio, payablesTurnover],]))
    

    Sector_name_mapping = {0: 'A',
                           1: 'AA',
                           2: 'AAA',
                           3: 'B',
                           4: 'BB',
                           5: 'BBB',
                           6: 'C',
                           7: 'CC',
                           8: 'CCC',
                           9: 'D'}

    return {"Rating2": Sector_name_mapping[y_pred_LR[0]]}

@app.get("/rating3/{Sector}/{currentRatio}/{quickRatio}/{cashRatio}/{daysOfSalesOutstanding}/{netProfitMargin}/{pretaxProfitMargin}/{grossProfitMargin}/{operatingProfitMargin}/{returnOnAssets}/{returnOnCapitalEmployed}/{returnOnEquity}/{assetTurnover}/{fixedAssetTurnover}/{debtEquityRatio}/{debtRatio}/{effectiveTaxRate}/{freeCashFlowOperatingCashFlowRatio}/{freeCashFlowPerShare}/{cashPerShare}/{companyEquityMultiplier}/{ebitPerRevenue}/{enterpriseValueMultiple}/{operatingCashFlowPerShare}/{operatingCashFlowSalesRatio}/{payablesTurnover}")
def read_price_date3(Sector: str, currentRatio: float, quickRatio: float, cashRatio: float, daysOfSalesOutstanding: float, netProfitMargin: float, pretaxProfitMargin: float, grossProfitMargin: float, operatingProfitMargin: float, returnOnAssets: float, returnOnCapitalEmployed: float, returnOnEquity: float, assetTurnover: float, fixedAssetTurnover: float, debtEquityRatio: float, debtRatio: float, effectiveTaxRate: float, freeCashFlowOperatingCashFlowRatio: float, freeCashFlowPerShare: float, cashPerShare: float, companyEquityMultiplier: float, ebitPerRevenue: float, enterpriseValueMultiple: float, operatingCashFlowPerShare: float, operatingCashFlowSalesRatio: float, payablesTurnover: float):
    #LR_model = joblib.load('LR_model')
    LR_model = pickle.load(open('MLP_model', "rb"))


    Sector_name_mapping = {'Basic Industries': 0,
                'Capital Goods': 1,
                'Consumer Durables': 2,
                'Consumer Non-Durables': 3,
                'Consumer Services': 4,
                'Energy': 5,
                'Finance': 6,
                'Health Care': 7,
                'Miscellaneous': 8,
                'Public Utilities': 9,
                'Technology': 10,
                'Transportation': 11}
    
    Sector_ = Sector_name_mapping[Sector]
    
    y_pred_LR = LR_model.predict(np.array([[Sector_, currentRatio, quickRatio, cashRatio, daysOfSalesOutstanding, netProfitMargin, pretaxProfitMargin, grossProfitMargin, 
                                  operatingProfitMargin, returnOnAssets, returnOnCapitalEmployed, returnOnEquity, assetTurnover, fixedAssetTurnover, debtEquityRatio, 
                                  debtRatio, effectiveTaxRate, freeCashFlowOperatingCashFlowRatio, freeCashFlowPerShare, cashPerShare, companyEquityMultiplier, 
                                  ebitPerRevenue, enterpriseValueMultiple, operatingCashFlowPerShare, operatingCashFlowSalesRatio, payablesTurnover],]))
    

    Sector_name_mapping = {0: 'A',
                           1: 'AA',
                           2: 'AAA',
                           3: 'B',
                           4: 'BB',
                           5: 'BBB',
                           6: 'C',
                           7: 'CC',
                           8: 'CCC',
                           9: 'D'}

    return {"Rating3": Sector_name_mapping[y_pred_LR[0]]}


#



@app.post("/todo")
def create_todo(year: str, month: str, closePrice: str):

    yearMonth = year +'/'+ month
    stock = pd.read_excel('corporate_rating.xlsx')
    
    stock.loc[len(stock)] = [yearMonth,	None, None, None, closePrice, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    stock.to_excel('corporate_rating.xlsx', index=False)
    return "create year:"+year+", month:"+month+", closePrice:"+closePrice



@app.put("/todo")
def update_todo(year: str, month: str, closePrice: str):
    print(closePrice)
    yearMonth = year +'/'+ month
    stock = pd.read_excel('corporate_rating.xlsx')
    stock.iloc[stock.iloc[:, 0] == yearMonth, 4] = closePrice
    stock.to_excel('corporate_rating.xlsx', index=False)
    return "update year:"+year+", month:"+month+", closePrice:"+closePrice



@app.delete("/todo")
def delete_todo(year: str, month: str):
    
    yearMonth = year +'/'+ month    
    stock = pd.read_excel('corporate_rating.xlsx')

    print(stock.iloc[:, 0] != yearMonth)

    stock = stock.loc[stock.iloc[:, 0] != yearMonth]

    stock.to_excel('corporate_rating.xlsx', index=False)
    return "delete year:"+year+", month:"+month