# quantum-programming-platform
This repository consist of codes and data used in the journal article "Advantages of Two Quantum Programming Platforms in Quantum Computing and Quantum Chemistry".

Installation of Qiskit and PennyLane are necessary for their usage.
In this tutorial, the codes are implenmented using Qiskit version 1.4.1 and PennyLane version 0.41.0.
Other libraries required in the usage examples will be stated in this document.

# Generation of Figure 1 & 2
The Figure 1 & 2 visualizing the statevector in Qiskit with LaTeX parameter and without parameter. It can be generated using statevector_qiskit.ipynb. This code emplement in jupyter, with additional library required: qiskit_aer (version 0.16.0). The pennylane part can be generated using statevector_pennylane.py.

# Generation of Figure 5 
The Figure 5a visualizing the quantum circuits of Qiskit ZZFeatureMap can be generated using qiskit_circuit_visualization.ipynb, with additional library pylatexenc (version 2.10) for visualization. The Figure 5b counterparts in PennyLane can be generated using pennylane_circuit_visualization.ipynb.

# Usage Example: Half Adder
1. For Half Adder implementation on qisit, with additional library qiskit-aer (version 0.16.0). Usage example is in half_adder_qiskit.ipynb. This code is implement in jupyter.
2. Half Adder implementation on Pennylane, Usage example is in half_adder_pennylane.ipynb, with additional library pylatexenc (version 2.10) for visualization. This code is implement in jupyter, with additional plugin in pennylane: pennylane-qiskit (version 0.41.0).

# Usage Example: Machine Learning
The AqSolDB dataset is imported from the csv file named curated_solubility_dataset.csv.
The codes to build machine learning model in usage examples for Qiskit and PennyLane are qiskit_ML.ipynb and pennylane_ML.ipynb, respectively.

Sklearn and Pandas libraries are required in this usage example.
Numpy library is available as the dependent library when installing Qiskit and PennyLane.
Matplotlib library is required for visualization.

For Qiskit implementation, additional library qiskit_machine_learning (version 0.8.2) is required. 
