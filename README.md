# quantum-programming-platform
This repository consist of codes and data used in the journal article "Advantages of Two Quantum Programming Platforms Advantage in Quantum Computing and Quantum Chemistry".

Installation of Qiskit and PennyLane are necessary for their usage.
Other libraries required in the usage examples will be stated in this document.

# Generation of Figure 1 & 2
The Figure 1 & 2 visualizing the statevector in Qiskit with LaTeX parameter and without parameter. It can be generated 
using statevector.ipynb. This code emplement in jupyter, with Qiskit version: 0.44.1. 

# Generation of Figure 5 & 6
The Figure 5a & 6a visualizing the quantum circuits of Qiskit ZZFeatureMap and ansatz layer used in machine learning can be generated using qiskit_circuit_visualization.py. The Figure 5b & 6b counterparts in PennyLane can be generated using pennylane_circuit_visualization.ipynb.

# Usage Example: Half Adder
1. For Half Adder implementation on qisit, additional libraries are required: qiskit-aer. Usage example is in half_adder_qiskit.ipynb. This code is implement in jupyter, with qiskit version: 0.44.1.
2. Half Adder implementation on Pennylane, Usage example is in half_adder_pennylane.ipynb. This code is implement in jupyter, with Pennylane version 0.32.0.

# Usage Example: Machine Learning
For Qiskit implementation, additional libraries are required: qiskit_algorithms, qiskit_machine_learning, sklearn For PennyLane implementation, the iris dataset is imported from a text file named iris_data.txt.

The codes to build machine learning model in usage examples for Qiskit and PennyLane are qiskit_ML.py and pennylane_ML.py, respectively.
