# Ingenii Quantum

Version: 0.1.0

Package of tools to integrate quantum and quantum-inspired algorithms to your machine learning algorithms. This package contains the following quantum algorithms:

## Quantum convolutional layer (2D and 3D):
It is designed to reduce the complexity of the classical 2D/3D CNN, while maintaining its prediction performance. The hybrid CNN replaces a convolutional layer with a quantum convolutional layer. That is, each classical convolutional filter is replaced by a quantum circuit, which acts as a quantum filter. Each quantum circuit is divided into two blocks: the data encoding, which maps the input data into a quantum circuit, and the quantum transformation, where quantum operations are applied to retrieve information from the encoded data. Tha package contains an implementation for 2D data (images) and for 3D data (volumes).

## Quantum fully-connected layer
It is designed to construct hybrid quantum-classical neural networks, where the quantum layer is a fully-connected layer. The quantum layer is a parametrized quantum circuit, composed of three parts: a data encoding which maps the classical data into a quantum circuit, a parametrized quantum circuit, which performs quantum operations with parameters, and measurements, which produce the output of the layer. Multiple quantum architectures are provided, which have been extracted from previous studies of hybrid neural networks. **Update:** To improve efficiency of the training, the codes have been rewritten using Pennylane instead of Qiskit. You can still run the algorithm in Qiskit devices by providing the suitable backend name.  

## Quantum fusion model
It is designed to efficiently integrate the extracted features from two classical neural network models to produce enhanced predictions. The proposed model strategically integrates 3D-CNNs and SG-CNNs to leverage their respective strengths in processing diverse facets of the training data. 
The simulation results presented here will demonstrate the superior performance of the quantum fusion model relative to state-of-the-art classical models.

## Quantum Hadamard Edge Detection (2D and 3D):
Performs edge detection for 2D data (images) and 3D data (volumes), using quantum operations. 

## Quantum-inspired image filter
This quantum-inspired filter is especially useful to highlight regions with varying contrast and identify regions of interest. This transformation essentially adjusts the pixel intensity of the image based on its local contrast and overall neighborhood contribution, which enhances segmentation by emphasizing the boundaries and transitions in the image.

### Quantum state visualizations
To understand the behavior and transformations of quantum circuits, visualizations play a key role. They provide intuitive insights into how quantum gates modify qubit states throughout the circuit. This library offers multiple state and circuit visualizations:

+ **State Space**: This visualization represents the evolution of quantum states at different stages of the circuit. It helps understand how quantum gates alter the coefficients of the quantum states. Each computational state is shown as a colored ball where the size indicates the probability of the corresponding basis state and the color represents the phase of the state.
+ **Phase Disks**: Phase disks are condensed representations of the state space visualization. At each stage of the computation, you will have one phase disk for each qubit, where the fullness represents the probability of the qubit and the color indicates the phase of the qubit.
+ **Bloch Sphere**: The Bloch sphere is a geometric representation of one-qubit systems. The state of a qubit is depicted as a point on the sphere. Quantum gates perform rotations on this sphere, visually demonstrating how the qubit's state evolves.
+ **Q-Sphere**: The Q-sphere generalizes the Bloch sphere for multiple-qubit systems. Each computational basis state appears as a point on the sphere, where the radius represents the probability of the basis state, the color indicates the phase and the latitude indicates the number of 0s and 1s of the basis state.

### Quantum neural network statistics
Provides metrics to evaluate the balance between performance and complexity in quantum neural networks. Two key metrics are:

+ **Entangling capacity**: circuit's ability to generate entanglement among qubits. This property is crucial for quantum computing, as quantum circuits need to generate a sufficient level of entanglement to perform tasks that classical computers cannot efficiently solve. For systems with more than two qubits, there are various non-equivalent measures of entanglement.
+ **Expressibility**: refers to the ability of a quantum circuit to generate a wide variety of quantum states from the input data. It is a measure of the "richness" of the set of states that the circuit can produce. High expressibility ensures that the circuit can approximate any target quantum state, which is crucial for the success of quantum neural networks. Expressibility is often assessed by comparing the distribution of quantum states produced by the circuit to the uniform distribution over all possible states. 

### Tensor network decomposition
One of the most effective tensor decompositions for compressing convolutional layers is the Tucker decomposition. This method breaks down the original four-dimensional weight tensor of a convolutional layer into multiple smaller tensors. This method is particularly relevant in medical imaging, where small datasets and complex models are common. Large pre-trained models may lead to overfitting or slow performance. Tucker decomposition compresses over-parameterized layers, preserving essential information for accurate predictions but with far fewer parameters, making the model faster and more efficient.

### Quantum optimization for image segmentation
Provides the graph mapping for image segmentation and the formulation as a QUBO problem. Many quantum and quantum-inspired algorithms can then be used to find the optimal segmentation mask, such as quantum annealing and QAOA. 