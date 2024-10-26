# Figure 5 Three-qubit ZZ feature map visualized in Qiskit.

from qiskit.circuit.library import ZZFeatureMap

feature_map = ZZFeatureMap(feature_dimension=3, reps=1)
feature_map.decompose().draw(output="mpl", fold=20)

# Figure 6 Three-qubit ansatz layer visualized in Qiskit.

from qiskit.circuit.library import RealAmplitudes

ansatz = RealAmplitudes(num_qubits=3, reps=3)
ansatz.decompose().draw(output="mpl", fold=20)
