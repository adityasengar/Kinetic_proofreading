import numpy as np
import pandas as pd
import os
from src.kinetic_model import run_simulation

def load_parameters(filepath):
    """Loads kinetic parameters from a CSV file."""
    # This is a placeholder for loading real experimental data/rates
    # For now, we'll use a default set if the file doesn't exist.
    if not os.path.exists(filepath):
        print(f"Warning: Parameter file not found at {filepath}. Using default parameters.")
        return {
            'k1': 1.0, 'k_1': 0.1, 'k2': 0.5,
            'k3': 0.2, 'k4': 0.01, 'S': 1.0
        }
    
    # Assuming a simple format: param_name,value
    params = pd.read_csv(filepath, index_col=0).to_dict()['value']
    return params

def main():
    """Main script to run the kinetic simulation."""
    # --- Configuration ---
    PARAMS_FILE = "Rates/default_rates.csv" # Example path
    OUTPUT_FILE = "results.csv"
    
    # Simulation time
    t_span = (0, 100)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)

    # Initial conditions: [C, I, E, EC, EI, P]
    initial_conditions = [10.0, 10.0, 1.0, 0, 0, 0]

    # --- Load & Run ---
    params = load_parameters(PARAMS_FILE)
    
    print("Running simulation...")
    solution = run_simulation(params, initial_conditions, t_span, t_eval)

    # --- Process and Save Results ---
    results_df = pd.DataFrame(solution.y.T, columns=['C', 'I', 'E', 'EC', 'EI', 'P'])
    results_df['time'] = solution.t
    
    results_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Simulation finished. Results saved to {OUTPUT_FILE}")
    print("\n--- Final Concentrations ---")
    print(results_df.iloc[-1])

if __name__ == "__main__":
    main()
