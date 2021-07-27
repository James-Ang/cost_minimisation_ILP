# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:19:50 2021

@author: James Ang
"""

from collections import defaultdict

import json
import pandas as pd

#%%
def get_data():
    
    # Opening JSON file 
    # f = open('test.json',)
      
    # data_json = json.load(f)
    
    df = pd.read_excel('Truck Consolidation_v9.xlsx',sheet_name='demandAggre')

    return df

def createjson(df):
    
    json_doc = defaultdict(list)
    json_doc2 = defaultdict(list)
    
    for _id in df.T:
        # print(_id)
        data = df.T[_id]
        # print(data)
        key = data.course
        key2 = data.course2
        
        for elt in json_doc[key]:   # level 1
            print(elt)
            # if elt["date"] == data.date:
            #     elt[data.student] = data.grade
            #     break
        else:
            for elt2 in json_doc2[key2]:
                print(elt2)
                
            else:
                values2 = {
                    'product': data['product'], 
                    'quantity': data.quantity}
                # json_doc2[key2].append(values2)
            
            values = {
                        'customer': data.customers,
                        'buyerZipcode': data.buyerZipcode, 
                        'deliveryWeek': data.deliveryWeek, 
                        data.course2 : values2 }
            json_doc[key].append(values)
            
    print(json.dumps(json_doc, indent=4)) #DONE

def main():
    df = get_data()
    
    createjson(df)
    
if __name__ == '__main__':
    main()