import pandas as pd 
def data_ingestion():
  '''
  Data: Composite Cement Strength
  ------------------------------------------------------------------------------
  Target: 'Concrete compressive strength(MPa, megapascals)'
  ------------------------------------------------------------------------------
  Independent Column: ''Cement (component 1)(kg in a m^3 mixture)',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)',
       'Fly Ash (component 3)(kg in a m^3 mixture)',
       'Water  (component 4)(kg in a m^3 mixture)',
       'Superplasticizer (component 5)(kg in a m^3 mixture)',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)',
       'Fine Aggregate (component 7)(kg in a m^3 mixture)', 'Age (day)'
  ------------------------------------------------------------------------------
  '''
  return df
df = pd.read_csv(r'C:\CompositeCementStrength_PredictionModel\data\Concrete_Data - Concrete_Data.csv')
