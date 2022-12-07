#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:16:21 2022

@author: namnguyen
"""


import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict


from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

#import CARSEC as CS

path= os.getcwd()
menu = ['Template','Single option', 'Multiple options', "Semi-Auto ML App"]
choice = st.sidebar.selectbox("Menu", menu)

if choice =='Template':
    
    st.subheader("Input datas (Single input):")

    Dict = {}

    st.write("* Tipo de seccion:")
    # 2-secc
    Dict['secc'] = st.selectbox('sección', options=['horm'])
    st.write("* Unidades a emplear:")
    # 3-unid
    Dict['unid'] = st.selectbox('"unid": indica las unidades de trabajo' , options=['tm'])
    st.write("* Normativa a emplear:")
    # 4-norm
    Dict['norm'] = st.selectbox('normativa', options=['ehe'])
    st.write("* Coefficients :")
    # 5-coef horm/ arma/ pret
    Dict['coef horm'] = st.text_input("horm", 1.5)
    Dict['coef arma'] = st.text_input("arma", 1.15)
    Dict['coef pret'] = st.text_input("pret", 1.15)

    # *************************
    st.write("* Punto de contorno:")

    # punto
    df_puntos = pd.DataFrame(
        '',
        index=range(7),
        columns=['punt', 'X', 'Y']
        
    )
    df_puntos['punt']=list(range(1,8))
    df_puntos['X']=[0,2,2,0,1,0.05,1.95]
    df_puntos['Y']=[0,0,2,2,1,0.05,0.05]

    with st.form('Punto de contorno') as f:
        st.header('Punto de contorno')
        response = AgGrid(df_puntos, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button()

    st.write(response['data'])
    data_json_punt = response['data'].to_json(orient='split')

    Dict['punt'] = data_json_punt
   

    # *************************

    st.write("* Definition del hormigon:")

    t_h = st.selectbox("tipo de hormigon", options=["t/m2"])

    Dict['horm'] = st.text_input("hormigon", 3500)

    # *************************
    # hp

    df_hp = pd.DataFrame(
        '',
        index=range(1),
        columns=['Punto 1', 'Punto 2', 'Punto 3', 'Punto 4']
    )
    df_hp['Punto 1']=[1]
    df_hp['Punto 2']=[2]
    df_hp['Punto 3']=[3]
    df_hp['Punto 4']=[4]



    with st.form(' Contorno Poligonal') as f:
        st.header('Contorno Poligonal')
        response = AgGrid(df_hp, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button()
    st.write(response['data'])
    # punto_dict=response['data'].to_dict()
    data_json_hp = response['data'].to_json(orient='split')

    Dict['punt contorno'] = data_json_hp

    # *************************
    # hc
    Dict['hc'] = st.selectbox('hc', options=['hc'])
    df_hc = pd.DataFrame(
        '',
        index=range(1),
        columns=['Punto Central', 'Radio']
    )
    df_hc['Punto Central']=[5]
    df_hc['Radio']=0.30

    with st.form('Punto central') as f:
        st.header('Punto central')
        response = AgGrid(df_hc, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button()
    st.write(response['data'])
    data_json_hc = response['data'].to_json(orient='split')

    Dict['hc'] = data_json_hc
    # *************************

    st.write("* Definicion de acero pasivo:fyk")

    t_a = st.selectbox("tipo de armadura", options=["t/m2"])
    Dict['arma'] = st.text_input("armadura", 51000)

    # *************************

    # Caracteristicas
    df_Caracteristicas = pd.DataFrame(
        '',
        index=range(1),
        columns=['Punto Inicial', 'Punto Final', 'No Armadura', 'Area']
    )
    df_Caracteristicas['Punto Inicial']=[6]

    df_Caracteristicas['Punto Final']=[7]
    df_Caracteristicas['No Armadura']=[10]
    df_Caracteristicas['Area']=[0.000314]
    with st.form('Caracteristicas') as f:
        st.header('Caracteristicas')
        response = AgGrid(df_Caracteristicas, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button()
    st.write(response['data'])
    data_json_Caracteristicas = response['data'].to_json(orient='split')

    Dict['punt armadura'] = data_json_Caracteristicas

    # *************************
    st.write("* Calculate of section")
    calc = st.selectbox("Indicate calculation", options=["inte"])

    df_LC = pd.DataFrame(
        '',
        index=range(1),
        columns=['Axil', 'monento X', 'momento Y']
    )
    df_LC['Axil']=[-10]
    df_LC['monento X']=[5]
    df_LC['momento Y']=[2]

    with st.form('LC') as f:
        st.header('LC')
        response = AgGrid(df_LC, editable=True, fit_columns_on_grid_load=True, use_checkbox=True)
        st.form_submit_button()
    st.write(response['data'])
    data_json_LC = response['data'].to_json(orient='split')

    Dict['calc inte'] = data_json_LC
    
    Dict['fin']=st.text_input('fin', 'fin')




if choice == 'Single option':

    st.subheader("Input datas (Single input):")

    Dict={}

    st.write("* Tipo de seccion:")
    #2-secc
    Dict['secc']=st.selectbox('sección', options=['horm'])
    st.write("* Unidades a emplear:")
    #3-unid
    Dict['unid']=st.selectbox('unidad', options=['tm','knm','lbin'])
    st.write("* Normativa a emplear:")
    #4-norm
    Dict['norm']=st.selectbox('normativa', options=['ehe','aashto'])
    st.write("* Coefficients :")
    #5-coef horm/ arma/ pret
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
    data_json_punt=response['data'].to_json(orient='split')

    Dict['punt']=data_json_punt
    # =============================================================================
    # list_main_keys=list(Dict['punt'].keys())
    # 
    # for k in list(Dict['punt'][list_main_keys[0]].keys()):
    #     k0=str(Dict['punt'][list_main_keys[0]][k])
    #     k1=str(Dict['punt'][list_main_keys[1]][k])
    #     k2=str(Dict['punt'][list_main_keys[2]][k])
    # =============================================================================


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
    #punto_dict=response['data'].to_dict()
    data_json_hp=response['data'].to_json(orient='split')

    Dict['punt contorno']=data_json_hp

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
    data_json_hc=response['data'].to_json(orient='split')

    Dict['hc']=data_json_hc
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
    data_json_Caracteristicas=response['data'].to_json(orient='split')

    Dict['punt armadura']=data_json_Caracteristicas

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
    data_json_LC=response['data'].to_json(orient='split')

    Dict['calc inte']=data_json_LC

     #****************************


# allow user to input multi-options controled by ID  
elif choice == 'Multiple options':
    
    st.subheader('Preview data')

    input_Dict = pd.read_excel(
        r'/Users/namnguyen/Documents/PROGRAMING/Python/Training_in_CFC/DataTrasformation/CARSEC.xlsx',
        sheet_name=None, header=0, index_col=None)
    
    option=list(input_Dict.keys())

    data=st.selectbox("which tab do you want to execute?", option,0)
       
    st.write(input_Dict[data].head(100))
# =============================================================================
#     
#     df_Properties= input_Dict['Properties']
#     
#     
#     with st.form('Properties') as f:
#         st.header('Properties')
#         response = AgGrid(df_puntos, editable=True, fit_columns_on_grid_load=True, enable_enterprise_modules=True,
#                           gridOptions = {
#                               # enable Master / Detail
#                               "masterDetail": True,
#                               "rowSelection": "single"})
#         st.form_submit_button()
# 
#     st.write(response['data'])
#     data_json_punt = response['data'].to_json(orient='split')
# 
# =============================================================================
    DB = defaultdict(dict)

    ID_list = input_Dict['Properties'].keys()
    #ID_list = input_Dict['Properties']['ID'].unique()

    #st.write(input_Dict)

    for i in ID_list:
        DB[i]['Properties'] = input_Dict['Properties'][input_Dict['Properties']['ID'] == i]
        DB[i]['Geometries'] = input_Dict['Geometries'][input_Dict['Geometries']['ID'] == i]
        DB[i]['LC'] = input_Dict['LC'][input_Dict['LC']['ID'] == i]
        DB[i]['Caracteristicas'] = input_Dict['Caracteristicas'][input_Dict['Caracteristicas']['ID'] == i]
        DB[i]['hp'] = input_Dict['hp'][input_Dict['hp']['ID'] == i]
        DB[i]['hc'] = input_Dict['hc'][input_Dict['hc']['ID'] == i]

    Dict_A = DB[ID_list[0]]
    
#*********************************
elif choice=="Semi-Auto ML App":

    st.subheader('Exploratory Data Analysis')
    
    data=st.file_uploader("Upload Dataset", type=['csv','json','xlsx','txt'])
   
    # create a download button
    mytext="Hello world"
    Download_btn=st.download_button(label="Download file", data=mytext, file_name="MyFile")

    if Download_btn:
        st.success("Excel file is saved")

