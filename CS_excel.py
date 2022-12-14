#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:02:53 2022

@author: namnguyen
"""
 

import numpy as np
import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

#%%# Create a None Database

# =============================================================================
# DB['secc']=str
# DB['unid']=str
# DB['norm']=str
# DB['coef_horm']= float
# DB['coef_arma']= float
# DB['coef_pret']= float
# DB['punt_contorno']=[0:{'punt':1, 'X':0,'Y':0},'punt':2, 'X':2,'Y':0},...] # pandasDataFrame.to_dict('records')
# DB['horm']=float
# DB['contorno_Poligonal']=[0:{'Punto_1':1,'Punto_2':2,'Punto_3':3,'Punto_4':4,...}]
# DB['hc']=[0:{'Punto_Central':5,'Radio':0.3}]
# DB['arma']=float
# DB['punt_armadura']=[0:{'Punto_Inicial':6,'Punto_Final':7,'No_Armadura':10, 'Area':0.000314}]
# DB['LC']=[0:{"Axil":-10, 'monento_X':5, 'monento_Y':2}]
# 
# =============================================================================

#%%# 

st.subheader('Preview data')
# Input excel 
input_DB = pd.read_excel(
    r'//Users/namnguyen/Desktop/CARSEC_STREAMLIT/CARSEC.xlsx',
    sheet_name=None, header=0, index_col=None)
#Show all tables in excel
list_tables=list(input_DB.keys())

for k in list_tables:  
    st.write(k)
    st.write(input_DB[k].head(10))
    

 
ID_list = (input_DB['Properties']['ID'].unique()).tolist()
    
DB = defaultdict(dict)

for i in ID_list:
    DB[i]['Properties'] = input_DB['Properties'][input_DB['Properties']['ID'] == i]
    DB[i]['Geometries'] = input_DB['Geometries'][input_DB['Geometries']['ID'] == i]
    DB[i]['LC'] = input_DB['LC'][input_DB['LC']['ID'] == i]
    DB[i]['Caracteristicas'] = input_DB['Caracteristicas'][input_DB['Caracteristicas']['ID'] == i]
    DB[i]['hp'] = input_DB['hp'][input_DB['hp']['ID'] == i]
    DB[i]['hc'] = input_DB['hc'][input_DB['hc']['ID'] == i]










