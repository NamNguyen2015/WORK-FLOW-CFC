DROP DATABASE MiTrabajo;

CREATE DATABASE MiTrabajo;
USE MiTrabajo;

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
#List_keys=['secc', 'unid', 'norm', 'coef_horm', 'coef_arma','coef_pret','punt','horm','punt_contorno','hc','arma', 'punt_armadura','calc_inte']

#secc: str
#unid: str
#norm:str
#coef_horm: float
#coef_arma: float
#coef_pret: float
#punt: DataFrame
#horm:int
#punt_contorno: DataFrame
#hc: DataFrame
#arma: intGEOMETRIES
#punt_armadura: DataFrame
#calc_inte: DataFrame
CREATE TABLE GEOMETRIES (
				 id_punt varchar(12),
                 punto int,
                 X float(2),
                 Y float(2),
                 id int,
				 primary key (id_punt)			
);
DESCRIBE GEOMETRIES;

CREATE TABLE PUNT_CONTORNO (
				 id_punt_contorno varchar(12),
                 Punto_1 int,
                 Punto_2 int,
                 Punto_3 int,
                 Punto_4 int,
				 primary key (id_punt_contorno)			
);
DESCRIBE PUNT_CONTORNO;
CREATE TABLE HC (
				 id_hc varchar(12),
                 Punto_1 int,
                 Punto_2 int,
                 Punto_3 int,
                 Punto_4 int,
				 primary key (id_hc)
);
DESCRIBE HC;

CREATE TABLE PUNT_ARMADURA (
				 id_punt_armadura varchar(12),
                 punto_inicial int,
                 punto_final int,
                 numero_cables int,
                 area_cable float(5),
				 primary key (id_punt_armadura)			
);
DESCRIBE PUNT_ARMADURA;
CREATE TABLE LC (
				 id_calc_inte varchar(12),
                 Axil float(2),
                 momento_X float(2),
                 momento_Y float(2),
				 primary key (id_calc_inte)
);
DESCRIBE LC;

CREATE TABLE CARSEC (
					id int,
					secc varchar(12),
                    unid varchar(12),
					norm varchar(12),
                    coef_horm float(2),
                    coef_arma float(2),
                    coef_pret float(2),
                    id_punt varchar(12),
                    horm int,
                    id_punt_contorno varchar(12),
                    id_hc varchar(12),
                    arma int,
                    id_punt_armadura varchar(12),
                    id_calc_inte varchar(12),
				
					PRIMARY KEY (id),  
					FOREIGN KEY (id_punt) REFERENCES GEOMETRIES (id_punt),
                    FOREIGN KEY (id_punt_contorno) REFERENCES PUNT_CONTORNO (id_punt_contorno),
                    FOREIGN KEY (id_hc) REFERENCES HC (id_hc),
                    FOREIGN KEY (id_punt_armadura) REFERENCES PUNT_ARMADURA (id_punt_armadura),
                    FOREIGN KEY (id_calc_inte) REFERENCES LC (id_calc_inte)
									
);
DESCRIBE CARSEC;






