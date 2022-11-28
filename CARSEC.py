#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:05:50 2022

@author: namnguyen
"""

import json
import pandas as pd
from collections import defaultdict



#%% Load the DataFrame

input_Dict = pd.read_excel(r'/Users/namnguyen/Documents/PROGRAMING/Python/Training_in_CFC/DataTrasformation/CARSEC.xlsx', 
                   sheet_name=None,header=0, index_col=None)

DB = defaultdict(dict)

ID_list=input_Dict['Properties']['ID'].unique()

for i in ID_list:
    DB[i]['Properties']=input_Dict['Properties'][input_Dict['Properties']['ID']==i]
    DB[i]['Geometries']=input_Dict['Geometries'][input_Dict['Geometries']['ID']==i]
    DB[i]['LC']=input_Dict['LC'][input_Dict['LC']['ID']==i]
    DB[i]['Caracteristicas']=input_Dict['Caracteristicas'][input_Dict['Caracteristicas']['ID']==i]
    DB[i]['hp']=input_Dict['hp'][input_Dict['hp']['ID']==i]
    DB[i]['hc']=input_Dict['hc'][input_Dict['hc']['ID']==i]

Dict_A=DB[ID_list[0]]


    
#%% Functions 

def CARSEC_Writer(Dict,name='CARSEC'):
    with open(name+'.txt', 'w') as f:
    #title
        f.write('CARSEC'+' \n') 
    # * Tipo de seccion
        f.write('secc '+str(Dict['Properties']['secc'][0])+' \n')
    # * Unidades para emplear. opciones: tm - knm - lbin
        f.write('unid '+str(Dict['Properties']['unid'][0])+' \n')
    # * Normativa a emplear. Opciones: ehe - aashto
        f.write('norm '+str(Dict['Properties']['norm'][0])+' \n')
    # * Coeficientes de seguridad EHE o coeficientes phi AASHTO. No es obligatoria
        f.write('coef horm '+str(Dict['Properties']['coef horm'][0])+' arma '
                   +str(Dict['Properties']['coef arma'][0]) + ' pret '+str(Dict['Properties']['coef pret'][0])+  ' \n')
    # * Puntos de contorno
        f.write('punt '+'\n')
        for i in range(len(Dict['Geometries']['no'])):

            f.write(str(Dict['Geometries']['no'][i])+' '+ str(Dict['Geometries']['X'][i])+' ' + str(Dict['Geometries']['Y'][i]) +' \n')
  
    # * Definicion del hormigon 
        f.write('horm '+str(Dict['Properties']['horm'][0])+' \n')
        f.write(str(Dict['hp']['Punto 1'][0])+ ' '+str(Dict['hp']['Punto 2'][0])+ ' '+str(Dict['hp']['Punto 3'][0])+ ' '+str(Dict['hp']['Punto 4'][0])+ ' \n')
        f.write('hc '+str(Dict['hc']['Punto Central'][0])+ ' '+str(Dict['hc']['Radio'][0])+ ' \n')
    # * Definicion del acero pasivo: fyk
        f.write('arma '+str(Dict['Caracteristicas']['arma'][0])+' \n')
        f.write(str(Dict['Caracteristicas']['Punto Inicial'][0])+ ' '+str(Dict['Caracteristicas']['Punto Final'][0])+ ' '
                +str(Dict['Caracteristicas']['No Armadura'][0])+ ' '+str(Dict['Caracteristicas']['Area'][0])+ ' '+' \n')
    # * Calculo de la seccion
        f.write('calc inte'+' \n')

        f.write( str(Dict['LC']['Axil'][0])+ ' '+str(Dict['LC']['momento X'][0])+ ' '+str(Dict['LC']['momento Y'][0])+ ' \n')
    # * fin 
        f.write('fin')
                          
    
def save_to_json(Dict,name='my_dict'):
    with open(name+'.json', 'w') as f:
        json.dump(Dict, f)
        
def load_json(path='my_dict.json'):
    f= open('my_dict.json', 'r')
    Dict=json.load(f)
    f.close()
    return Dict

#%% 
CARSEC_Writer(Dict_A,name='CARSEC_111')







#%% Input Dict_1
# =============================================================================
# Dict_1={}
# Dict_1['norm']='ehe'
# Dict_1['secc']='horm'
# Dict_1['unid']='tm'
# # coef
# Dict_1['coef horm']= str(1.50)
# Dict_1['coef arma']= str(1.15)
# Dict_1['coef pret']= str(1.15)
# # punt
# 
# Dict_1['punt']={1:[0,0],2:[2,0],3:[2,2],4:[0,2],5:[1,1],6:[0.05,0.05],7:[1.95,0.05]}
# 
# Dict_1['horm']=str(3500)
# Dict_1['punt contorno']= [1,2,3,4] #{1:Dict_1[punt][0],2:Dict_1[punt][1],3:Dict_1[punt][2],4:Dict_1[punt][3]}
# Dict_1['hc']={'punto central ':5,' radial ':0.30}
# Dict_1['arma']=str(51000)
# Dict_1['punt armadura']={' punto inicial ': 6,' punto final ': 7,' numero armaduras ':10,' area ':0.000314}
# 
# Dict_1['calc inte']={' Axil ':-10,' momento X': 5.0,' momento Y': 2.0}
# 
# #%% Execute
# CARSEC_Writer(Dict=Dict_1)
# save_to_json(Dict=Dict_1)
# #%% Load json file
# Dict_2=load_json(path='my_dict.json')
# #%% 
# CARSEC_Writer(Dict=Dict_2,name='CARSEC_from_json')
# save_to_json(Dict=Dict_2,name='json_from_json')
# =============================================================================


# =============================================================================
# 
# 
# def CARSEC_Writer(Dict,name='CARSEC'):
#     with open(name+'.txt', 'w') as f:
#         f.write('CARSEC'+' \n')
#         f.write('secc '+Dict['secc']+' \n')
#         f.write('unid '+Dict['unid']+' \n')
#         f.write('norm '+Dict['norm']+' \n')
#         f.write('coef horm '+Dict['coef horm']+' arma '+Dict['coef arma'] + ' pret '+Dict['coef pret']+  ' \n')
# 
#         f.write('punt '+'\n')
#         for k in Dict['punt'].keys():
#             k1=str(Dict['punt'][k][0])
#             k2=str(Dict['punt'][k][1])
#             f.write(str(k)+' '+ k1+' ' + k2 +' \n')
#         f.write('horm '+Dict['horm']+' \n')
#         f.write('* punto contorno '+'\n')    
#         [f.write(str(i)+' ') for i in Dict['punt contorno']] 
#         f.write('\n')
#                  
#         f.write('hc ') 
#         for k in Dict['hc'].keys():
#             k1=str(Dict['hc'][k])          
#             f.write( k1 +' ')
#         f.write('\n')
#         f.write('arma '+Dict['arma']+' \n')
#         for k in Dict['punt armadura'].keys():
#             k1=str(Dict['punt armadura'][k])          
#             f.write( k1+' ')
#         f.write('\n')
#         f.write('calc inte'+' \n')
#         for k in Dict['calc inte'].keys():
#             k1=str(Dict['calc inte'][k])          
#             f.write( k1+ ' ')
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
# =============================================================================
