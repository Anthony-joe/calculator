import streamlit as st
import pandas as pd
import numpy as np

col1, col2 = st.beta_columns([0.1,1])
col2.title("Calculateur rentabilité")
col1.image("logo.png",width = 50)

addr = st.text_input("Infos adresse")
Prix_du_bien = st.number_input('Prix du bien (FAI)',step=1)
Loyer = st.number_input('Loyer CC',step=1)
Charges = st.number_input('Charges / mois',step=1)
Taxe = st.number_input('Taxe foncière / an',step=1)
Surface = st.number_input('Surface moyenne',step=1)
Ameublement = st.selectbox('Ameublement', [True,False])
Travaux = st.selectbox('Travaux', ["Pas de travaux - 0€/m²","Rafraîchissement peinture - 250€/m²","Rénovation légère - 450€/m²","Rénovation moyenne - 700€/m²","Rénovation lourde - 900€/m²"])

cost=0

if Travaux == "Pas de travaux - 0€/m²":
    cost = 0
elif Travaux == "Rafraîchissement peinture - 250€/m²":
    cost = 250
elif Travaux == "Rénovation légère - 450€/m²":
    cost = 450
elif Travaux == "Rénovation moyenne - 700€/m²":
    cost = 700
elif Travaux == "Rénovation lourde - 900€/m²":
    cost = 900

ameub = 0

if Ameublement == True :
    ameub = 120
else :
    ameub = 0

Couts_travaux = Surface*(ameub + cost )

notaire =min((min(6500,Prix_du_bien)*(3.945/100)+max(0,min((Prix_du_bien-6500),10500)*(1.627/100))+max(0,min((Prix_du_bien-6500-10500),43000)*(1.085/100))+max(0,(Prix_du_bien-6500-10500-43000)*(0.814/100))),0.1*Prix_du_bien)*1.2+5.9/100*Prix_du_bien+1200

Beanstock = 0

if Prix_du_bien<140000 :
    Beanstock = 10000
else :
    Beanstock = Prix_du_bien*0.072

budget_total = Beanstock+ notaire + Couts_travaux + Prix_du_bien

rentability =round(((Loyer*12)-(Charges*12+Taxe))/(budget_total),3)

#reset= st.button("rest")


st.write(" ")

st.write("Infos adresse :")
st.write(addr)

st.write("Coûts travaux :")
st.write(Couts_travaux, "€")

st.write("Budget Total:")
st.write(budget_total,"€")

st.write("rentability :")
st.write(rentability*100,"%" )
