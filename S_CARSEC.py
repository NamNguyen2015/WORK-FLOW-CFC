#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:57:10 2022

@author: namnguyen
"""

import numpy as np
import math
import streamlit as st
import json
import pandas as pd
import os
import io
import subprocess
import re
import sys
import pathlib
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


path= os.getcwd()


#%% Changing working directory to where the files are located
print('Changing working directory to where the files are located')



Path_Python_Folder = pathlib.Path(__file__).parent.resolve()


try:
    os.chdir(Path_Python_Folder)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(Path_Python_Folder))
except NotADirectoryError:
    print("{0} is not a directory".format(Path_Python_Folder))
except PermissionError:
    print("You do not have permissions to change to {0}".format(Path_Python_Folder))




#%% 

#import CARSEC as CS

#%%

st.title('📊 CARSEC')
st.image("https://media-exp1.licdn.com/dms/image/C4E0BAQF-5O5stYOVnA/company-logo_200_200/0/1519880154681?e=2147483647&v=beta&t=JfMPNm2p8aQC7iHLqp8S4096lFDmShsodp8A73sRnWQ",width=100)
st.header('Company: CFC.SL' )
st.markdown("**Nam Nguyen** ")
st.markdown("**Pedram Manouchehri** ")

st.subheader("Introduction:")
st.write(" This program calculates the caracteristics of one or varirous concrete sections by coordinated the vertices. It is possible to use the concrte of different caractics for the long section.")
st.write(" It is also possible to use different types of steels.")
st.write("Moreover,  it permiss to calculate the moments of the section and draw the diagram of interaction.")

st.subheader("Input datas (Single input):")

Dict={}

st.write("* Tipo de seccion:")
Dict['secc']=st.selectbox('sección', options=['horm'])
st.write("* Unidades a emplear:")
Dict['unid']=st.selectbox('unidad', options=['tm','knm','lbin'])
st.write("* Normativa a emplear:")
Dict['norm']=st.selectbox('normativa', options=['ehe','aashto'])
st.write("* Coefficients :")
Dict['coef horm']=st.text_input("horm",  )
Dict['coef arma']=st.text_input("arma",  )
Dict['coef pret']=st.text_input("pret",  )


#*************************
st.write("* Punto de contorno:")

# punto
df_puntos = pd.DataFrame(
    '',
    index=range(10),
    columns=['punt', 'X', 'Y']
)

with st.form('Punto de contorno') as f:
    st.header('Punto de contorno')
    response = AgGrid(df_puntos, editable=True, fit_columns_on_grid_load=True)
    st.form_submit_button()

st.write(response['data'])


Dict['punt']=response['data']

#*************************


  
st.write("* Definition del hormigon:")

t_h=st.selectbox("tipo de hormigon",options=["kN/m2","t/m2"])

Dict['horm']=st.text_input("hormigon", )

#*************************
# hp

df_hp = pd.DataFrame(
    '',
    index=range(2),
    columns=['Punto 1','Punto 2','Punto 3','Punto 4']
)

with st.form(' Contorno Poligonal') as f:
    st.header('Contorno Poligonal')
    response = AgGrid(df_hp, editable=True, fit_columns_on_grid_load=True)
    st.form_submit_button()
st.write(response['data'])

Dict['punt contorno']=response['data']

#*************************
# hc
Dict['hc']=st.selectbox('hc', options=['hc'])
df_hc = pd.DataFrame(
    '',
    index=range(2),
    columns=['Punto Central','Radio']
)

with st.form('Punto central') as f:
    st.header('Punto central')
    response = AgGrid(df_hc, editable=True, fit_columns_on_grid_load=True)
    st.form_submit_button()
st.write(response['data'])

Dict['hc']=response['data']
#*************************

st.write("* Definicion de acero pasivo:fyk")

t_a=st.selectbox("tipo de armadura",options=["kN/m2","t/m2"])
Dict['arma']=st.text_input("armadura", )

#*************************

# Caracteristicas
df_Caracteristicas = pd.DataFrame(
    '',
    index=range(2),
    columns=['Punto Inicial', 'Punto Final', 'No Armadura', 'Area']
)

with st.form('Caracteristicas') as f:
    st.header('Caracteristicas')
    response = AgGrid(df_Caracteristicas, editable=True, fit_columns_on_grid_load=True)
    st.form_submit_button()
st.write(response['data'])

Dict['punt armadura']=response['data']

#*************************
st.write("* Calculate of section")
calc=st.selectbox("Indicate calculation", options=["dibu", "inte"])


df_LC = pd.DataFrame(
    '',
    index=range(2),
    columns=['Axil', 'monento X', 'momento Y']
)

with st.form('LC') as f:
    st.header('LC')
    response = AgGrid(df_LC, editable=True, fit_columns_on_grid_load=True,use_checkbox=True)
    st.form_submit_button()
st.write(response['data'])

Dict['calc inte']=response['data']



#%%

st.subheader("Show the final excel file")
Dict
st.write("The file has " + str(len(Dict.keys()))+" sheet_names")

option=list(Dict.keys())

data=st.selectbox("which tab do you want to execute?", option,0)
   
st.write(Dict[data])


#%%
# =============================================================================
# 
# # =============================================================================
# # 
# # def CARSEC_Writer(Dict,name='CARSEC'):
# #     with open(name+'.txt', 'w') as f:
# #         f.write('CARSEC'+' \n')
# #         f.write('secc '+Dict['secc']+' \n')
# #         f.write('unid '+Dict['unid']+' \n')
# #         f.write('norm '+Dict['norm']+' \n')
# #         f.write('coef horm '+Dict['coef horm']+' arma '+Dict['coef arma'] + ' pret '+Dict['coef pret']+  ' \n')
# # 
# # 
# # 
# # 
# # 
# #         f.write('punt '+str(Dict['punt'])+'\n')
# # 
# # =============================================================================
# 
# # =============================================================================
# # 
# #         for k in Dict['punt'].keys():
# #             k1=str(Dict['punt'][k][0])
# #             k2=str(Dict['punt'][k][1])
# #             f.write(str(k)+' '+ k1+' ' + k2 +' \n')
# #             
# #             
# # =============================================================================
#             
#         f.write('horm '+Dict['horm']+' \n')
# # =============================================================================
# #         f.write('* punto contorno '+'\n')    
# #         [f.write(str(i)+' ') for i in Dict['punt contorno']] 
# #         f.write('\n')
# #                  
# #         f.write('hc ') 
# #         for k in Dict['hc'].keys():
# #             k1=str(Dict['hc'][k])          
# #             f.write( k1 +' ')
# #         f.write('\n')
# # =============================================================================
#         f.write('arma '+Dict['arma']+' \n')
# # =============================================================================
# #         for k in Dict['punt armadura'].keys():
# #             k1=str(Dict['punt armadura'][k])          
# #             f.write( k1+' ')
# #         f.write('\n')
# #         f.write('calc inte'+' \n')
# #         for k in Dict['calc inte'].keys():
# #             k1=str(Dict['calc inte'][k])          
# #             f.write( k1+ ' ')
# # =============================================================================
#         f.write('\n')
#         f.write('fin')
#                           
#     
# def save_to_json(Dict,name='my_dict'):
#     with open(name+'.json', 'w') as f:
#         json.dump(Dict, f)
#         
# def load_json(path='my_dict.json'):
#     f= open('my_dict.json', 'r')
#     Dict=json.load(f)
#     f.close()
#     return Dict
# 
# #%%
# # =============================================================================
# # buffer = io.BytesIO()  
# CARSEC_Writer(Dict, name='CarSec12345')
# # 
# # Download_btn=st.download_button(
# #     label="📥  DOWNLOAD FILE .txt",
# #     data=buffer,
# #     file_name='CarSec12345',
# #     mime='text/txt',
# # )
# # 
# # if Download_btn:
# #     st.success("Excel file is saved")
# # 
# # 
# # =============================================================================
# 
# =============================================================================
