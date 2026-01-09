import numpy as np

# --- Species Definitions ---
# These correspond to the species listed in the SI.
SPECIES = [
    "C3+", "iC4+", "H+", "H+", "C+", "iC4", "C7", "C3", "C7", "Cn="
]

# --- Default Rate Constants ---
# These are placeholder values. Actual values would come from experimental
# data or detailed quantum chemical calculations as in the paper.
# Using generic values for now, based on typical kinetic ranges.
DEFAULT_RATE_CONSTANTS = {
    "k1": 1.0, "k2": 0.8, "k3": 0.1, "k4": 0.5,
    "k5": 0.3, "k6": 0.05, "k7": 0.02, "k9": 0.6,
    "k10": 0.4, "k11": 0.01
}

# --- Initial Concentrations ---
# Example initial conditions for species. These can be adjusted.
# Order should match SPECIES definition.
DEFAULT_INITIAL_CONDITIONS = {
    "C3+": 1.0, "iC4+": 0.0,
    "H+": 0.0, "H+": 0.0,
    "C+": 0.0, "iC4": 0.0,
    "C7": 0.0, "C3": 0.0,
    "C7": 0.0, "Cn=": 0.0
}
