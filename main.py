from src.data_ingestion import data_ingestion
# Define orchestron Model: Entry Point
def main(): # Function Defination
  # Step1: Data Ingestion
  df = data_ingestion()
  print(df.head())
main()