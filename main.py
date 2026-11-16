from src.reporter import DataFrameReporter

import pandas as pd
import os 

def main():
    file_path = os.path.join('data', 'payments.csv')

    df = pd.read_csv(file_path)

    reporter = DataFrameReporter()

    print(reporter.show_report(df))


if __name__ == '__main__':
    main()