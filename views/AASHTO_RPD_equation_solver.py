import streamlit as st
import sympy as sp

# Title
st.header('AASHTO Rigid Pavement Design Equation Solver')

# Equation
st.write("#### Design Equation")

st.latex(r"""
\log_{10}W_{18} = Z_R S_o + 7.35 \log_{10}(D+1) - 0.06 + 
\frac{\log_{10}(\Delta PSI / 3.0)}{1 + \left[ \frac{1.624 \times 10^7}{(D+1)^{8.46}} \right]} 
+ (4.22 - 0.32 TSI) \log_{10} \left( \frac{S_c' C_d \left[ D^{0.75} - 1.132 \right]}{215.63 J \left[ D^{0.75} - \left( \frac{18.42}{(E_c/k)^{0.25}} \right) \right]} \right)
""")

# Option to choose which variable to solve for
solve_for = st.radio("Select what to solve for:", ('D (Thickness)', 'W18 (Cumulative 18-kips ESAL)'))

# Given constants input
st.write("#### Parameters")

with st.container(border=True):
    col1a, col1b, col1c = st.columns(3, gap='small')

    if solve_for == 'D (Thickness)':
        with col1a:
            W18 = st.number_input('W18 (cumulative)', value=None, placeholder='18-Kips ESAL')

    else:
        with col1a:
            D = st.number_input('D (Thickness)', value=None, placeholder='inch', format='%0.4f')

    with col1b:
        Z_R = st.number_input('Zr', value=None, format='%0.4f')

    with col1c:
        S_o = st.number_input('Standard Deviation (So)', value=None, format='%0.4f')

    col2a, col2b, col2c = st.columns(3, gap='small')

    with col2a:
        delta_PSI = st.number_input('ΔPSI', value=None)

    with col2b:
        tsi = st.number_input('TSI', value=None)

    with col2c:
        S_c_prime = st.number_input("Concrete Modulus of Rupture (S'c)", value=None, placeholder='lb/in^2')

    col3a, col3b, col3c = st.columns(3, gap='small')

    with col3a:
        C_d = st.number_input('Drainage Coefficient (Cd)', value=None)

    with col3b:
        J = st.number_input('Load Transfer Coefficient (J)', value=None)

    with col3c:
        E_c = st.number_input('Concrete Modulus of Elasticity (Ec)', value=None, placeholder='lb/in^2')

    col4a, col4b, col4c = st.columns(3, gap='small')

    with col4a:
        k = st.number_input('Modulus of Sub-grade Reaction (k)', value=None, placeholder='lb/in^3')

if solve_for == 'D (Thickness)':
    # Check if all inputs are provided before calculation
    if all(x is not None for x in [W18, Z_R, S_o, delta_PSI, tsi, S_c_prime, C_d, J, E_c, k]):
        try:
            # Define variable
            D = sp.Symbol('D', positive=True, real=True)

            # Define the AASHTO Rigid Pavement equation
            equation = -(sp.log(W18, 10)) + (Z_R * S_o + 7.35 * sp.log(D + 1, 10) - 0.06 +
                                             sp.log(delta_PSI / 3.0, 10) / (1 + (1.624 * 10 ** 7 / (D + 1) ** 8.46)) +
                                             (4.22 - 0.32 * tsi) * sp.log(
                        (S_c_prime * C_d * (D ** 0.75 - 1.132)) /
                        (215.63 * J * (D ** 0.75 - (18.42 / (E_c / k) ** 0.25))), 10))

            # Use nsolve to solve the equation with an initial guess
            D_solution = sp.nsolve(equation, D, 7)  # Initial guess of D is set to 7 inches

            # Display result
            st.write("#### Result")
            st.success(f'Solution: D = {D_solution:.4f} inches')

        except ValueError as e:
            st.error(f"Error in solving the equation: {e}")
        except sp.SympifyError:
            st.error("SympifyError: Unable to parse equation or input values.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please fill in all the inputs to calculate D.")

else:
    # Check if all inputs are provided before calculation
    if all(x is not None for x in [D, Z_R, S_o, delta_PSI, tsi, S_c_prime, C_d, J, E_c, k]):
        try:
            # Define variable
            W18 = sp.Symbol('W18', positive=True, real=True)

            # Define the AASHTO Rigid Pavement equation
            equation = -(sp.log(W18, 10)) + (Z_R * S_o + 7.35 * sp.log(D + 1, 10) - 0.06 +
                                             sp.log(delta_PSI / 3.0, 10) / (1 + (1.624 * 10 ** 7 / (D + 1) ** 8.46)) +
                                             (4.22 - 0.32 * tsi) * sp.log(
                        (S_c_prime * C_d * (D ** 0.75 - 1.132)) /
                        (215.63 * J * (D ** 0.75 - (18.42 / (E_c / k) ** 0.25))), 10))

            # Use nsolve to solve the equation with an initial guess
            W18_solution = sp.nsolve(equation, W18, 10000)  # Initial guess of D is set to 7 inches

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
        st.warning("Please fill in all the inputs to calculate W18.")
