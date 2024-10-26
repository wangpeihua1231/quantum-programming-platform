from qiskit.circuit.library import RealAmplitudes, ZZFeatureMap
from qiskit.primitives import Sampler
from qiskit_algorithms.optimizers import COBYLA
from qiskit_machine_learning.algorithms.classifiers import VQC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
iris_data = load_iris()

features = iris_data.data
labels = iris_data.target


# Split the dataset

random_seed = 123
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, train_size=0.8, random_state=random_seed
)


# Construct the variational quantum circuits

num_features = features.shape[1]

feature_map = ZZFeatureMap(feature_dimension=num_features, reps=1)
ansatz = RealAmplitudes(num_qubits=num_features, reps=3)


# Build and train the machine learning model

sampler = Sampler()
optimizer = COBYLA(maxiter=100)

vqc = VQC(
    sampler=sampler,
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=optimizer,
)

vqc.fit(train_features, train_labels)


# Evaluate the model

train_score = vqc.score(train_features, train_labels)
test_score = vqc.score(test_features, test_labels)

print(f"Quantum VQC on the training dataset: {train_score:.2f}")
print(f"Quantum VQC on the test dataset:     {test_score:.2f}")
