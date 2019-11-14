import pandas as pd 

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
