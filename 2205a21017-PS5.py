# Importing Streamlit library
import streamlit as st

# Define the DELTA to STAR conversion function
def DELTA_STAR(R12, R23, R31):
    """
    Calculate STAR network resistances (R1, R2, R3) 
    from DELTA network resistances (R12, R23, R31).
    """
    try:
        denominator = R12 + R23 + R31
        R1 = (R12 * R31) / denominator
        R2 = (R12 * R23) / denominator
        R3 = (R31 * R23) / denominator
        return R1, R2, R3
    except ZeroDivisionError:
        st.error("The sum of R12, R23, and R31 must not be zero.")

# Title for the web application
st.title("2205a21017-PS5: DELTA to STAR Conversion")

# Input Section
st.header("Enter the resistances of the DELTA network")
R12 = st.number_input("R12 (Ohms)", min_value=0.0, value=100.0, step=1.0)
R23 = st.number_input("R23 (Ohms)", min_value=0.0, value=100.0, step=1.0)
R31 = st.number_input("R31 (Ohms)", min_value=0.0, value=100.0, step=1.0)

# Button to compute STAR resistances
if st.button("Compute"):
    # Call the DELTA to STAR conversion function
    if R12 > 0 and R23 > 0 and R31 > 0:
        R1, R2, R3 = DELTA_STAR(R12, R23, R31)
        # Display results
        st.success("Computed STAR Resistances:")
        st.write(f"R1: {R1:.2f} Ohms")
        st.write(f"R2: {R2:.2f} Ohms")
        st.write(f"R3: {R3:.2f} Ohms")
    else:
        st.error("All resistance values must be greater than 0.") 