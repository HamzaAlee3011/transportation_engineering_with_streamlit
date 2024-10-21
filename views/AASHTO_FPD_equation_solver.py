import streamlit as st
import sympy as sp

# Title
st.header('AASHTO Flexible Pavement Design Equation Solver')

# Equation
st.write("#### Design Equation")

st.latex(r"""
\log_{10}W_{18} = Z_R S_o + 9.36 \log_{10}(SN+1) - 0.20 + 
\frac{\log_{10}(\Delta PSI / 2.7)}{0.40 + \left[ \frac{1094}{(SN+1)^{5.19}} \right]} 
+ 2.32 \log_{10}(M_R) - 8.07
""")

# Option to choose which variable to solve for
solve_for = st.radio("Select what to solve for:", ('SN (Structural Number)', 'W18 (Cumulative 18-kips ESAL)'))

# Given constants input
st.write("#### Parameters")

with st.container(border=True):
    col1a, col1b, col1c = st.columns(3, gap='small')

    if solve_for == 'SN (Structural Number)':
        with col1a:
            W18 = st.number_input('W18 (cumulative)', value=None, placeholder='18-Kips ESAL')

    else:
        with col1a:
            SN = st.number_input('SN (Structural Number)', value=None)

    with col1b:
        Z_R = st.number_input('Zr', value=None, format='%0.4f')

    with col1c:
        S_o = st.number_input('Standard Deviation (So)', value=None, format='%0.4f')

    col2a, col2b, col2c = st.columns(3, gap='small')

    with col2a:
        delta_PSI = st.number_input('ΔPSI', value=None)

    with col2b:
        M_R = st.number_input("Resilient Modulus (MR)", value=None, placeholder='psi')

if solve_for == 'SN (Structural Number)':

    # Check if all inputs are provided before calculation
    if all(x is not None for x in [W18, Z_R, S_o, delta_PSI, M_R]):
        try:
            # Define variable
            SN = sp.Symbol('SN', positive=True, real=True)

            # Define the AASHTO Flexible Pavement equation
            equation = -(sp.log(W18, 10)) + (Z_R * S_o + 9.36 * sp.log(SN + 1, 10) - 0.20 +
                                             sp.log(delta_PSI / 2.7, 10) /
                                             (0.40 + (1094 / (SN + 1)**5.19)) +
                                             2.32 * sp.log(M_R, 10) - 8.07)

            # Use nsolve to solve the equation with an initial guess
            SN_solution = sp.nsolve(equation, SN, 5)  # Initial guess of SN is set to 5

            # Display result
            st.write("#### Result")
            st.success(f'Solution: SN = {SN_solution:.4f}')

        except ValueError as e:
            st.error(f"Error in solving the equation: {e}")
        except sp.SympifyError:
            st.error("SympifyError: Unable to parse equation or input values.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please fill in all the inputs to calculate SN.")

else:
    # Check if all inputs are provided before calculation
    if all(x is not None for x in [SN, Z_R, S_o, delta_PSI, M_R]):
        try:
            # Define variable
            W18 = sp.Symbol('W18', positive=True, real=True)

            # Define the AASHTO Flexible Pavement equation
            equation = -(sp.log(W18, 10)) + (Z_R * S_o + 9.36 * sp.log(SN + 1, 10) - 0.20 +
                                             sp.log(delta_PSI / 2.7, 10) /
                                             (0.40 + (1094 / (SN + 1) ** 5.19)) +
                                             2.32 * sp.log(M_R, 10) - 8.07)

            # Use nsolve to solve the equation with an initial guess
            W18_solution = sp.nsolve(equation, W18, 10000)  # Initial guess of SN is set to 5

            # Display result
            st.write("#### Result")
            st.success(f'Solution: W18 = {round(W18_solution, 3)} 18-kips ESAL')

        except ValueError as e:
            st.error(f"Error in solving the equation: {e}")
        except sp.SympifyError:
            st.error("SympifyError: Unable to parse equation or input values.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please fill in all the inputs to calculate  W18.")
