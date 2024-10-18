import sympy as sp

# Define variables
D = sp.Symbol('D', positive=True, real=True)

# Given constants
W18 = 10579671
Z_R = -1.645
S_o = 0.45
delta_PSI = 1.9
k = 300
E_c = 4.5 * 10**6
S_c_prime = 900
J = 3.2
C_d = 1.0
tsi = 2.5

# Define the AASHTO Rigid Pavement equation
equation = -(sp.log(W18, 10)) + (Z_R * S_o + 7.35 * sp.log(D + 1, 10) - 0.06 +
            sp.log(delta_PSI / 3.0, 10) / (1 + (1.624 * 10**7 / (D + 1)**8.46)) +
            (4.22 - 0.32 * tsi) * sp.log(
                (S_c_prime * C_d * (D**0.75 - 1.132)) /
                (215.63 * J * (D**0.75 - (18.42 / (E_c / k)**0.25))), 10))

# Use nsolve to solve the equation with an initial guess
D_solution = sp.nsolve(equation,D, 7)  # Initial guess close to expected value

print("The solution for D is:", round(D_solution, 3))
