import pandas as pd 
import datetime

#### funcs to convert df <-> redash result ####
def df_to_redash(df_orig, index_to_col=False):
    import numpy as np
    df = df_orig.copy()
    if index_to_col:
        df.reset_index(inplace=True)
    result = {'columns': [], 'rows': []}
    conversions = [
        {'pandas_type': np.integer, 'redash_type': 'integer',},
        {'pandas_type': np.inexact, 'redash_type': 'float',},
        {'pandas_type': np.datetime64, 'redash_type': 'datetime', 'to_redash': lambda x: x.dt.strftime('%Y-%m-%d %H:%M:%S')},
        {'pandas_type': np.bool_, 'redash_type': 'boolean'},
        {'pandas_type': np.object, 'redash_type': 'string'}
    ]
    labels = []
    for dtype, label in zip(df.dtypes, df.columns):
        for conversion in conversions:
            if issubclass(dtype.type, conversion['pandas_type']):
                result['columns'].append({'name': label, 'friendly_name': label, 'type': conversion['redash_type']})
                labels.append(label)
                func = conversion.get('to_redash')
                if func:
                    df[label] = func(df[label])
                break
    result['rows'] = df[labels].replace({np.nan: None}).to_dict(orient='records')
    return result

def redash_to_df(result, col_to_index=False):
    import pandas as pd
    conversions = [
        {'redash_type': 'datetime', 'to_pandas': lambda x: pd.to_datetime(x, infer_datetime_format=True)},
        {'redash_type': 'date', 'to_pandas': lambda x: pd.to_datetime(x, infer_datetime_format=True)},
    ]
    df = pd.DataFrame.from_dict(result['rows'], orient='columns')
    labels = []
    for column in result['columns']:
        label = column['name']
        labels.append(label)
        for conversion in conversions:
            if conversion['redash_type'] == column['type']:
                func = conversion.get('to_pandas')
                if func:
                    df[label] = df[label].apply(func)
                break
    df = df[labels]
    if col_to_index and labels:
        df.set_index(labels[0], inplace=True)
    return df


df = redash_to_df( get_query_result({query_id}) )

########################################

############# YOUR CODES ###############
result_df = 
########################################


result = df_to_redash(result_df)