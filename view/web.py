import streamlit as st
import pandas as pd
from controller import app
from model.rules import R
from controller.app import cykParse

def run_streamlit():
    # st.set_page_config(layout='wide')
    st.write("<h1 style='text-align:center; '>Syntactic Parsing dengan CYK Algorithm</h1>", unsafe_allow_html=True)
    input_sentence = st.text_input(' ',placeholder='Masukkan Kalimat Anda')
    button_click = st.button('Check', type='primary') # membuah sebuah button dengan text dalam button = 'Check'
    if button_click:
            if len(input_sentence) == 0: st.write(":red[Kalimat Tidak Boleh Kosong]")    # ketika input kosong
            else:
                words = input_sentence.split()
                n = len(words)

                # Initialize the table
                T = [[set([]) for _ in range(n)] for _ in range(n)]

                # Filling in the table
                cykParse(words)

                # if "K" in T[0][n - 1]:
                #     st.write(":green[Selamat, kalimat anda memenuhi syarat]")
                # else:
                #     st.write(":yelow[Maaf sepertinya kalimat anda belum memenuhi syarat]")
                