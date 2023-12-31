from model.rules import R
import streamlit as st

# Function to perform the CYK Algorithm
def cykParse(words):
    n = len(words)

    # Initialize the table
    T = [[set([]) for _ in range(n)] for _ in range(n)]

    # Filling in the table
    for j in range(n):
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == words[j]:
                    T[j][j].add(lhs)

        for i in range(j - 1, -1, -1):
            # Iterate over the range i to j + 1
            for k in range(i, j):
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        # If a terminal is found
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

    # If the sentence can be formed by rules of the given grammar
    if "K" in T[0][n - 1]:
        st.write(":green[Selamat, kalimat Anda sudah sesuai]")
    else:
        st.write(":red[Maaf, kalimat anda belum sesuai dengan aturan]")
        
        
# input_sentence = "Tono Memasak Rendang"
# words = input_sentence.split()

# Function Call
# cykParse(words)