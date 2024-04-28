import numpy as np
from scipy.integrate import solve_ivp

def proofreading_model(t, y, k1, k_1, k2, k3, k4, S):
    """
    Defines the system of ODEs for a kinetic proofreading model.
    
    Species (y):
    y[0] = C (Correct substrate)
    y[1] = I (Incorrect substrate)
    y[2] = E (Enzyme)
    y[3] = EC (Enzyme-Correct complex)
    y[4] = EI (Enzyme-Incorrect complex)
    y[5] = P (Product)
    """
    C, I, E, EC, EI, P = y
    
    # Rate constants
    # k1: E + S -> ES (binding)
    # k_1: ES -> E + S (unbinding)
    # k2: ES -> EP (first irreversible step, e.g., phosphorylation)
    # k3: EP -> E + P (product release)
    # k4: EP -> D (discard pathway)

    # dC/dt
    dCdt = -k1 * E * C + k_1 * EC
    
    # dI/dt
    dIdt = -k1 * E * I + k_1 * EI
    
    # dE/dt
    dEdt = -k1 * E * (C + I) + (k_1 + k2) * (EC + EI)
    
    # dEC/dt
    dECdt = k1 * E * C - (k_1 + k2) * EC
    
    # dEI/dt
    dEIdt = k1 * E * I - (k_1 + k2) * EI
    
    # dP/dt
    # This is a simplified model where the proofreading step (k4) is implicitly
    # handled by the difference in k2 for correct vs incorrect.
    # A more complex model would have EP states.
    dPdt = k3 * EC # Assuming only correct complex makes product for simplicity
    
    return [dCdt, dIdt, dEdt, dECdt, dEIdt, dPdt]

def run_simulation(params, initial_conditions, t_span, t_eval):
    """
    Runs the ODE solver for the kinetic model.
    """
    solution = solve_ivp(
        proofreading_model,
        t_span,
        initial_conditions,
        args=tuple(params.values()),
        t_eval=t_eval,
        method='RK45'
    )
    return solution
