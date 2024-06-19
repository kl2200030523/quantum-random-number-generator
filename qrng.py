import json
import os
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

def generate_random_numbers(token, num_shots=1024):
    print("Initializing IBM Quantum service...")
    service = QiskitRuntimeService(channel="ibm_quantum", token=token)
    backend = service.least_busy(operational=True, simulator=False)
    print(f"Selected backend: {backend}")
    
    # Create a simple Quantum Circuit for random number generation
    n_qubits = 5
    circuit = QuantumCircuit(n_qubits)
    
    # Apply Hadamard gates to all qubits to create superposition
    for qubit in range(n_qubits):
        circuit.h(qubit)
    circuit.measure_all()
    
    # Transpile the circuit for the backend
    print("Transpiling circuit...")
    transpiled_circuit = transpile(circuit, backend=backend)
    print("Circuit transpiled.")
    
    # Initialize Sampler with the backend
    sampler = Sampler(backend)
    
    # Execute job with Sampler
    print("Running job with Sampler...")
    job = sampler.run(transpiled_circuit, shots=num_shots)
    print("Job submitted.")
    
    # Retrieve and return the binary probabilities
    print("Fetching job result...")
    job_result = job.result()
    print("Job result fetched.")
    
    counts = job_result.quasi_dists[0]
    probabilities = {bitstring: count / num_shots for bitstring, count in counts.items()}
    
    return probabilities

def main():
    token = "YOUR_IBM_TOKEN"
    
    # Delete the existing random_numbers.json file if it exists
    if os.path.exists('random_numbers.json'):
        os.remove('random_numbers.json')
        print("Existing 'random_numbers.json' file deleted.")
    
    print("Generating random numbers...")
    random_numbers = generate_random_numbers(token)
    print("Random Numbers:", random_numbers)
    with open('random_numbers.json', 'w') as f:
        json.dump(random_numbers, f)
    print("Results saved to 'random_numbers.json'.")

if __name__ == "__main__":
    main()
