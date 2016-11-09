import json
import pandas as pd

df = pd.read_csv("ListingSecurityList.csv", sep=";", header=None, encoding='windows-1251')

df.columns = df.iloc[0]
df = df.drop([0])
model = ['model.stock' for i in range(305)]
id = [i for i in range(1,306)]
instrument = df['INSTRUMENT_TYPE'].tolist()
ticker = df['TRADE_CODE'].tolist()
company_name = df['EMITENT_FULL_NAME'].tolist()
nominal_price = df['NOMINAL'].tolist()
stock_curr = df['CURRENCY'].tolist()
stock_curr = df['CURRENCY'].tolist()
company_site = df['DISCLOSURE_PART_PAGE'].tolist()
company_disclosure_site = df['DISCLOSURE_RF_INFO_PAGE'].tolist()

i = [{'model': model, 'id': id} for m, i in zip(model, id)]
# df.to_json("MOEX_Listings.json",)
