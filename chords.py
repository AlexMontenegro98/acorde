import pandas as pd
import streamlit as st 
import json

# https://stackoverflow.com/questions/43596579/how-to-use-python-pandas-stylers-for-coloring-an-entire-row-based-on-a-given-col

# streamlit run C:\Python\Acordes\chords.py

color_grey = st.color_picker('Pick A Color', '#2d2d2d')
st.write('The current color is', color_grey)

df = pd.read_csv(r"/Notas Violão - Página1.csv")
notes = ['Do','Do#','Re','Re#','Mi','Fa','Fa#','Sol','Sol#','La','La#','Si']
eadgbe = ['Mi','Si','Sol','Re','La','Mi']
chord_C = [0,1,0,2,3,0]
chords = {'C':[0,1,0,2,3,7], 'D':[2,3,2,0,7,7]}

filee = json.load(open(r'/chords.json'))
chords = filee['chords']

chord_name = st.radio("What\'s the chord?", chords)

chord = chords[chord_name]

def highlight_cells(x):
    #chord = chords['D']
    df = x.copy()
    #set default color
    #df.loc[:,:] = 'background-color: papayawhip' 
    df.loc[:,:] = '' 
    #set particular cell colors
    for i in range(6):
        if chord[i] == 0:
            df.iloc[i,chord[i]] = f'background-color: {color_grey}'
        elif chord[i] == -7:
            df.iloc[i,chord[i]] = 'background-color: black'
        else:
            df.iloc[i,chord[i]] = 'background-color: green'
    return df 

t = df.style.apply(highlight_cells, axis=None)
st.dataframe(t)
