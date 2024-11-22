import streamlit as st
st.title("2205A21017-PS5")
st.subheader("calculate the resistance vaues(R1,R2,R3) of the STAR connection network for the given DELTA connection network having resistance R12,R23 and R31")

def output(R12,R23,R13):
    R1 = (R12*R13)/(R12+R23+R13)
    R2 = (R12*R23)/(R12+R23+R13)
    R3 = (R23*R13)/(R12+R23+R13)
    return R1,R2,R3

col1,col2=st.columns(2)
with col1:
    R12=st.number_input("R12:ohms", value=100)
    R23=st.number_input("R23:ohms", value=100)
    R13=st.number_input("R31:ohms", value=100)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            R1,R2,R3=output(R12,R23,R13)
            st.write(f"R1 = {R1:.2f} ohms")
            st.write(f"R2={R2:.2f} ohms")
            st.write(f"R3={R3:.2f} ohms")