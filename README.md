# Quantum Random Number Generator

This is a web application that generates random numbers using quantum algorithms provided by IBM's Quantum Experience.

## Description

The project demonstrates how to generate random numbers using quantum computing principles and display them on a web interface. The random numbers are fetched from a pre-generated JSON file (`random_numbers.json`) which contains numbers generated by a quantum algorithm.

## How It Works

1. **Quantum Random Number Generation**:
   - The `qrng.py` script uses Qiskit and IBM's Quantum Experience to generate random numbers.
   - A quantum circuit is created and executed on a quantum backend to produce truly random numbers.
   - The results are saved in `random_numbers.json`.

2. **Web Application**:
   - The web application consists of `index.html`, `script.js`, and `style.css`.
   - Users can click a button to fetch and display a random number from `random_numbers.json`.

## Files

- `index.html`: The main HTML file for the web application.
- `script.js`: JavaScript file that handles fetching and displaying random numbers.
- `style.css`: CSS file for styling the web application.
- `random_numbers.json`: JSON file containing pre-generated quantum random numbers.
- `qrng.py`: Python script that generates random numbers using quantum computing.

## Quantum Random Number Generator (QRNG)

### What is a QRNG?

A Quantum Random Number Generator (QRNG) leverages the principles of quantum mechanics to generate random numbers. Unlike classical random number generators, which rely on algorithms and can be ultimately predictable, QRNGs use the inherent randomness of quantum phenomena to produce truly random numbers.

### Why is QRNG Special?

1. **True Randomness**: 
   - Classical algorithms for random number generation are deterministic in nature, meaning they follow a predictable sequence based on an initial seed value. This makes them pseudo-random.
   - QRNGs, on the other hand, exploit quantum phenomena such as superposition and entanglement, which are fundamentally probabilistic. This leads to true randomness, which is essential for applications requiring high security and unpredictability.

2. **Unpredictability**:
   - In classical systems, given the algorithm and the seed, one can predict the entire sequence of random numbers.
   - In a quantum system, the outcome of a quantum measurement is inherently unpredictable. Even if the exact quantum state is known, the result of the measurement cannot be determined in advance.

3. **Applications**:
   - **Cryptography**: True random numbers are crucial for generating secure cryptographic keys.
   - **Simulations**: Randomness is essential for accurate Monte Carlo simulations in various scientific fields.
   - **Gaming**: Ensures fairness and unpredictability in online gaming and gambling.

## Usage

1. **Generating Quantum Random Numbers**:
   - Ensure you have Python and Qiskit installed.
   - Update the `qrng.py` script with your IBM Quantum Experience token.
   - Run the script to generate random numbers and save them to `random_numbers.json`:
     ```sh
     python qrng.py
     ```

2. **Running the Web Application**:
   - Open `index.html` in a web browser.
   - Click the "Generate Random Number" button to display a random number.

## Deployment

The web application is deployed using GitHub Pages. You can access it at:
[https://kl2200030523.github.io/quantum-random-number-generator/](https://kl2200030523.github.io/quantum-random-number-generator/)

## Conclusion

This project demonstrates the integration of quantum computing with a simple web application to generate and display true random numbers. The use of quantum mechanics ensures that the numbers are truly random and unpredictable, making them superior to classical pseudo-random number generators in terms of security and reliability.

## Acknowledgments

- IBM Quantum Experience for providing the quantum computing platform.
- [Qiskit](https://qiskit.org/) for the quantum computing SDK.
