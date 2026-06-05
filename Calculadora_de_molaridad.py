#Programa que calcula la cantidad a pesar o medir de algún compuesto químico utilizado para análisis químicos.
import streamlit as st
st.title("Calculadora de concentraciones químicas")
st.write("Esta aplicación permite calcular la cantidad de compuesto químico de interés que se desea pesar o medir para cierta molaridad y volumen.")

opcion=st.selectbox("Compuesto",["Ácido Acético Glacial (CH3COOH)", "Ácido Clorhídrico (HCl)", "Ácido Fluorhídrico (HF)", "Ácido Fosfórico (H3PO4)",
"Ácido Nítrico (HNO3)", "Ácido Perclórico (HClO4)", "Ácido Sulfámico (H3NSO3)", "Ácido Sulfúrico (H2SO4)",
"Amoníaco (Solución Acuosa) (NH3)", "Azul de Metileno (C16H18ClN3S)", "Bicarbonato de Sodio (NaHCO3)", "Butilitio (n-Butillitio) (C4H9Li)",
"Carbonato de Calcio (CaCO3)", "Carbonato de Sodio (Na2CO3)", "Cloruro de Amonio (NH4Cl)", "Cloruro de Bario (BaCl2)",
"Cloruro de Calcio (CaCl2)", "Cloruro de Deuterio (DCl)", "Cloruro de Plata (AgCl)", "Cloruro de Potasio (KCl)",
"Cloruro de Sodio (NaCl)", "Dicromato de Potasio (K2Cr2O7)", "EDTA Disódico Dihidratado (C10H14N2Na2O8.2H2O)", "Etanol Absoluto (C2H5OH)",
"Ferrocianuro de Potasio (K4[Fe(CN)6])", "Fezoato de Potasio (KHC8H4O4)", "Glucosa (C6H12O6)", "Hidróxido de Bario (Ba(OH)2)",
"Hidróxido de Potasio (KOH)", "Hidróxido de Sodio (NaOH)", "Metanol (CH3OH)", "Metóxido de Sodio (CH3ONa)",
"Ninhidrina (C9H6O4)", "Nitrato de Plata (AgNO3)", "Permanganato de Potasio (KMnO4)", "Peróxido de Hidrógeno (Agua Oxigenada) (H2O2)",
"Reactivo de Karl Fischer (Base) (C5H5N.SO2)", "Sacarosa (C12H22O11)", "Sulfato de Aluminio (Al2(SO4)3)", "Sulfato de Cobre Anhidro (CuSO4)",
"Sulfato de Cobre Pentahidratado (CuSO4.5H2O)", "Sulfato de Magnesio Heptahidratado (Sal de Epsom) (MgSO4.7H2O)", "Sulfato de Potasio (K2SO4)", "Sulfato Ferroso (FeSO4)",
"Tetraóxido de Osmio (OsO4)", "Tiosulfato de Sodio (Na2S2O3)", "Trifluoruro de Boro en Metanol (BF3.CH4O)", "Tris(hidroximetil)aminometano (C4H11NO3)",
"Yodato de Potasio (KIO3)", "Yoduro de Potasio (KI)"
                                ])

Mol=st.number_input("Molaridad deseada (M)")
Vol_ml=st.number_input("Volumen deseado (ml)")
Vol=Vol_ml/1000
Prz=st.number_input("Pureza del compuesto (%)", 1.0, 100.0, step=0.1)

a=opcion
b=a.split(" ")
c=b[-1]
d=c[1:-1]

comp = {
  "NaOH" : {"nombre" : "Hidróxido de Sodio", "Masa molar" : 39.997, "Estado" : "Sólido", "Densidad": None},
  "KHC8H4O4" : {"nombre" : "Ftalato Ácido de Potasio", "Masa molar" : 204.22, "Estado" : "Sólido", "Densidad": None},
  "Na2CO3" : {"nombre" : "Carbonato de Sodio", "Masa molar" : 105.99, "Estado" : "Sólido", "Densidad": None},
  "NaCl" : {"nombre" : "Cloruro de Sodio", "Masa molar" : 58.44, "Estado" : "Sólido", "Densidad": None},
  "Na2S2O3" : {"nombre" : "Tiosulfato de Sodio", "Masa molar" : 158.11, "Estado" : "Sólido", "Densidad": None},
  "HCl" : {"nombre" : "Ácido Clorhídrico", "Masa molar" : 36.46, "Estado" : "Líquido", "Densidad": 1.19},
  "H2SO4" : {"nombre" : "Ácido Sulfúrico", "Masa molar" : 98.08, "Estado" : "Líquido", "Densidad": 1.84},
  "HNO3" : {"nombre" : "Ácido Nítrico", "Masa molar" : 63.01, "Estado" : "Líquido", "Densidad": 1.4},
  "CH3COOH" : {"nombre" : "Ácido Acético Glacial", "Masa molar" : 60.05, "Estado" : "Líquido", "Densidad": 1.05},
  "H3PO4" : {"nombre" : "Ácido Fosfórico", "Masa molar" : 97.99, "Estado" : "Líquido", "Densidad": 1.69},
  "C10H14N2Na2O8.2H2O" : {"nombre" : "EDTA Disódico dihidratado", "Masa molar" : 372.24, "Estado" : "Sólido", "Densidad": None},
  "AgNO3" : {"nombre" : "Nitrato de Plata", "Masa molar" : 169.87, "Estado" : "Sólido", "Densidad": None},
  "K2Cr2O7" : {"nombre" : "Dicromato de Potasio", "Masa molar" : 294.18, "Estado" : "Sólido", "Densidad": None},
  "KIO3" : {"nombre" : "Yodato de Potasio", "Masa molar" : 214, "Estado" : "Sólido", "Densidad": None},
  "KMnO4" : {"nombre" : "Permanganato de Potasio", "Masa molar" : 158.03, "Estado" : "Sólido", "Densidad": None},
  "CuSO4.5H2O" : {"nombre" : "Sulfato de Cobre Pentahidratado", "Masa molar" : 249.68, "Estado" : "Sólido", "Densidad": None},
  "BaCl2" : {"nombre" : "Cloruro de Bario", "Masa molar" : 208.23, "Estado" : "Sólido", "Densidad": None},
  "HF" : {"nombre" : "Ácido Fluorhídrico", "Masa molar" : 20.01, "Estado" : "Líquido", "Densidad": 1.15},
  "HClO4" : {"nombre" : "Ácido Perclórico", "Masa molar" : 100.46, "Estado" : "Líquido", "Densidad": 1.66},
  "CH3ONa" : {"nombre" : "Metóxido de Sodio", "Masa molar" : 54.02, "Estado" : "Sólido", "Densidad": None},
  "OsO4" : {"nombre" : "Tetraóxido de Osmio", "Masa molar" : 254.23, "Estado" : "Sólido", "Densidad": None},
  "C9H6O4" : {"nombre" : "Ninhidrina", "Masa molar" : 178.14, "Estado" : "Sólido", "Densidad": None},
  "C5H5N.SO2" : {"nombre" : "Reactivo de Karl Fischer (Base)", "Masa molar" : 143.16, "Estado" : "Líquido", "Densidad": 0.93},
  "BF3.CH4O" : {"nombre" : "Trifluoruro de Boro en Metanol", "Masa molar" : 99.87, "Estado" : "Líquido", "Densidad": 0.87},
  "C4H9Li" : {"nombre" : "Butilitio (n-Butillitio)", "Masa molar" : 64.06, "Estado" : "Líquido", "Densidad": 0.68},
  "DCl" : {"nombre" : "Cloruro de Deuterio", "Masa molar" : 37.47, "Estado" : "Líquido", "Densidad": 1.2},
  "K4[Fe(CN)6]" : {"nombre" : "Ferrocianuro de Potasio", "Masa molar" : 368.35, "Estado" : "Sólido", "Densidad": None},
  "C4H11NO3" : {"nombre" : "Tris(hidroximetil)aminometano", "Masa molar" : 121.14, "Estado" : "Sólido", "Densidad": None},
  "H3NSO3" : {"nombre" : "Ácido Sulfámico", "Masa molar" : 97.1, "Estado" : "Sólido", "Densidad": None},
  "C16H18ClN3S" : {"nombre" : "Azul de Metileno", "Masa molar" : 319.85, "Estado" : "Sólido", "Densidad": None},
  "KOH": {"nombre": "Hidróxido de Potasio", "Masa molar": 56.11, "Estado": "Sólido", "Densidad": None},
  "AgCl": {"nombre": "Cloruro de Plata", "Masa molar": 143.32, "Estado": "Sólido", "Densidad": None},
  "NH3": {"nombre": "Amoníaco (Solución Acuosa)", "Masa molar": 17.03, "Estado": "Líquido", "Densidad": 0.90},
  "K2SO4": {"nombre": "Sulfato de Potasio", "Masa molar": 174.26, "Estado": "Sólido", "Densidad": None},
  "CuSO4": {"nombre": "Sulfato de Cobre Anhidro", "Masa molar": 159.61, "Estado": "Sólido", "Densidad": None},
  "CaCO3": {"nombre": "Carbonato de Calcio", "Masa molar": 100.09, "Estado": "Sólido", "Densidad": None},
  "CaCl2": {"nombre": "Cloruro de Calcio", "Masa molar": 110.98, "Estado": "Sólido", "Densidad": None},
  "KCl": {"nombre": "Cloruro de Potasio", "Masa molar": 74.55, "Estado": "Sólido", "Densidad": None},
  "NaHCO3": {"nombre": "Bicarbonato de Sodio", "Masa molar": 84.01, "Estado": "Sólido", "Densidad": None},
  "C6H12O6": {"nombre": "Glucosa", "Masa molar": 180.16, "Estado": "Sólido", "Densidad": None},
  "C12H22O11": {"nombre": "Sacarosa", "Masa molar": 342.30, "Estado": "Sólido", "Densidad": None},
  "MgSO4.7H2O": {"nombre": "Sulfato de Magnesio Heptahidratado (Sal de Epsom)", "Masa molar": 246.47, "Estado": "Sólido", "Densidad": None},
  "FeSO4": {"nombre": "Sulfato Ferroso", "Masa molar": 151.91, "Estado": "Sólido", "Densidad": None},
  "Al2(SO4)3": {"nombre": "Sulfato de Aluminio", "Masa molar": 342.15, "Estado": "Sólido", "Densidad": None},
  "Ba(OH)2": {"nombre": "Hidróxido de Bario", "Masa molar": 171.34, "Estado": "Sólido", "Densidad": None},
  "NH4Cl": {"nombre": "Cloruro de Amonio", "Masa molar": 53.49, "Estado": "Sólido", "Densidad": None},
  "KI": {"nombre": "Yoduro de Potasio", "Masa molar": 166.00, "Estado": "Sólido", "Densidad": None},
  "CH3OH": {"nombre": "Metanol", "Masa molar": 32.04, "Estado": "Líquido", "Densidad": 0.79},
  "C2H5OH": {"nombre": "Etanol Absoluto", "Masa molar": 46.07, "Estado": "Líquido", "Densidad": 0.789},
  "H2O2": {"nombre": "Peróxido de Hidrógeno (Agua Oxigenada)", "Masa molar": 34.01, "Estado": "Líquido", "Densidad": 1.45}
}

MM=comp[d]["Masa molar"]
Est=comp[d]["Estado"]
Dens=comp[d]["Densidad"]

if len(Est)==6:
    gr=(Mol*Vol*MM)/(Prz/100)
    gr_limpio=round(gr, 4)
    st.write(f"Se necesitan {gr_limpio} gramos de {opcion}")
elif len(Est)==7:
    vp=(Mol*Vol*MM)/((Prz/100)*Dens)
    vp_limpio=round(vp, 4)
    st.write(f"Se necesitan {vp_limpio} ml de {opcion}")