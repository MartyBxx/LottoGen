import streamlit as st
import random as rd

st.title('Willkommen zum Lottozahlengenerator')

lotterie = st.selectbox('Für welche Lotterie willst du Zahlen generieren?', ('Eurojackpot', '6aus49'))

if lotterie == 'Eurojackpot':

    ej_hz_min = st.slider('Hauptzahlen Min', 1, 50, 1)
    ej_hz_max = st.slider('Hauptzahlen Max', 1, 50, 50)
    ej_hzn = st.slider('Wieviele Hauptzahlen willst du generieren?', 5, 12, 5)
    ej_zz_min = st.slider('Zusatzzahlen Min', 1, 12, 1)
    ej_zz_max = st.slider('Zusatzzahlen Max', 1, 12, 12)
    ej_zzn = st.slider('Wieviele Zusatzzahlen willst du generieren?', 0, 10, 2)

    btn = st.button('Zahlen generieren')
    if btn:
        if ej_hz_min > ej_hz_max:
            st.error('Hauptzahlen Min muss schon kleiner als Hauptzahlen Max sein :woozy_face:')
        elif ej_hz_max < ej_hz_min:
            st.error('Hauptzahlen Max muss schon größer als Hauptzahlen Min sein :woozy_face:')
        elif ej_zz_max < ej_zz_min:
            st.error('Zusatzzahlen Max muss schon größer als Zusatzzahlen Min sein :woozy_face:')
        elif ej_zz_min > ej_zz_max:
            st.error('Zusatzzahlen Min muss schon kleiner als Zusatzzahlen Max sein :woozy_face:')
        else:
            ej_h_zahlen = set([rd.randint(ej_hz_min, ej_hz_max) for i in range(ej_hzn)])
            ej_z_zahlen = set([rd.randint(ej_zz_min, ej_zz_max) for i in range(ej_zzn)])
            st.info(sorted(ej_h_zahlen))
            st.info(sorted(ej_z_zahlen))
            st.write('Mögen dies deine Glückszahlen sein! :four_leaf_clover:')

else:
    hz_min = st.slider('Hauptzahlen Min', 1, 49, 1)
    hz_max = st.slider('Hauptzahlen Max', 1, 49, 49)
    hzn = st.slider('Wieviele Hauptzahlen willst du generieren?', 6, 12, 6)
    zz_min = st.slider('Zusatzzahlen Min', 0, 9, 0)
    zz_max = st.slider('Zusatzzahlen Max', 0, 9, 9)
    zzn = st.slider('Wieviele Zusatzzahlen willst du generieren?', 1, 2, 1)

    btn = st.button('Zahlen generieren')
    if btn:
        if hz_min > hz_max:
            st.error('Hauptzahlen Min muss schon kleiner als Hauptzahlen Max sein :woozy_face:')
        elif hz_max < hz_min:
            st.error('Hauptzahlen Max muss schon größer als Hauptzahlen Min sein :woozy_face:')
        elif zz_max < zz_min:
            st.error('Zusatzzahlen Max muss schon größer als Zusatzzahlen Min sein :woozy_face:')
        elif zz_min > zz_max:
            st.error('Zusatzzahlen Min muss schon kleiner als Zusatzzahlen Max sein :woozy_face:')
        else:
            h_zahlen = [rd.randint(hz_min, hz_max) for i in range(hzn)]
            z_zahlen = [rd.randint(zz_min, zz_max) for i in range(zzn)]
            st.info(sorted(h_zahlen))
            st.info(sorted(z_zahlen))
            st.write('Mögen dies deine Glückszahlen sein! :four_leaf_clover:')
