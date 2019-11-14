import pandas as pd 

from datetime import datetime


def shift_to_next_timestep(data, col, new_col=None, group_col='ID'):

    if not new_col:
        new_col = '{}_p'.format(col)
        
    # Make new column
    data[new_col] = None

    for group in data[group_col].unique():
       
        group_idx = data[data['ID']==group].index
        seq_idx = data.loc[i_idx, 'i']

        for seq_id, group_id in zip(seq_idx, group_idx):
            
            # Next row of df
            next_id = group_id + 1
            
            try:
                # Get next sequence id 
                next_seq_id = data.loc[next_id]['i']
                
                # If group ID on next row is different, don't shift the value
                if data.loc[next_id, group_col] != group:
                    continue
                
                # Check if next_i value is +1 of current i
                if next_seq_id == seq_id + 1:
                    data.loc[next_id, new_col] = data.loc[group_id, col] 

            except KeyError:
                continue

    return data


def add_datetime_variables(data):
    
    data['year'], data['month'], data['season'] = zip(*data.date_time.map(parse_dt))
    
    return data

def parse_dt(dt_string):
    dt = datetime.strptime(dt_string, '%m/%d/%Y %H:%M')
    
    year = dt.year
    month = dt.month
    
    # {winter:1, spring:2, summer:3, fall:4}
    season = (month%12 + 3) // 3  
    
    return year, month, season