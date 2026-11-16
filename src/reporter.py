import pandas as pd

class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, data, title = 'None'):
        df = pd.DataFrame(data)
        if title != 'None':
            return print(title)

        col_cnt = df.shape[1]
        str_cnt = df.shape[0]
        dub_cnt = df.duplicated().sum()
        dub_pcnt = format(df.duplicated().sum()/df.shape[0], self.percent_format)

        report_text = (f'Количество столбцов: {col_cnt}\n'
                      f'Количество строк: {str_cnt}\n'
                      f'Количество дубликатов: {dub_cnt}\n'
                      f'Доля дубликатов: {dub_pcnt}')
        
        return print(report_text)

    # добавьте в класс метод show_report
    
reporter = DataFrameReporter()

import pandas as pd

data = pd.read_csv('data/payments.csv')

# вызовите метод show_report для reporter, передав в него датафрейм

reporter.show_report(data)