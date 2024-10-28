# quantum-programming-platform
This repository consist of codes and data used in the journal article "Advantages of Two Quantum Programming Platforms Advantage in Quantum Computing and Quantum Chemistry".

Installation of Qiskit and PennyLane are necessary for their usage.
Other libraries required in the usage examples will be stated in this document.

# Generation of Figure 1 & 2
The Figure 1 & 2 visualizing the statevector in Qiskit with LaTeX parameter and without parameter. It can be generated 
using statevector.ipynb. This code emplement in jupyter, with qiskit version: 0.44.1. 

# Generation of Figure 5 & 6
The Figure 5 & 6 visualizing the quantum circuits of Qiskit ZZFeatureMap and ansatz layer used in machine learning can be generated using qiskit_circuit_visualization.py.

# Usage Example: Half Adder
For Half Adder implementation, additional libraries are required: qiskit-aer. Usage example is in half_adder.ipynb. This code is emplement in jupyter, with qiskit version: 0.44.1.

# Usage Example: Machine Learning
For Qiskit implementation, additional libraries are required: qiskit_algorithms, qiskit_machine_learning, sklearn
For PennyLane implementation, the iris dataset is imported from a text file named iris_data.txt.

The codes to build machine learning model in usage examples for Qiskit and PennyLane are qiskit_ML.py and pennylane_ML.py, respectively.
