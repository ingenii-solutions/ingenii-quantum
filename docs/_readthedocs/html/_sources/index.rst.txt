Welcome to Ingenii Quantum's Documentation!
===========================================

Ingenii Quantum is a Python package for quantum and quantum-inspired machine learning.

Quantum Convolutional Layer (2D and 3D)
---------------------------------------

It is designed to reduce the complexity of the classical 2D/3D CNN while maintaining its prediction performance. 
The hybrid CNN replaces a convolutional layer with a quantum convolutional layer. Each classical convolutional filter 
is replaced by a quantum circuit, which acts as a quantum filter. Each quantum circuit is divided into two blocks: 
the data encoding, which maps the input data into a quantum circuit, and the quantum transformation, where quantum operations 
are applied to retrieve information from the encoded data. The package contains an implementation for 2D data (images) 
and for 3D data (volumes).

Quantum Fully-Connected Layer
------------------------------

It is designed to construct hybrid quantum-classical neural networks, where the quantum layer is a fully-connected layer. 
The quantum layer is a parameterized quantum circuit composed of three parts: a data encoding that maps the classical data 
into a quantum circuit, a parameterized quantum circuit that performs quantum operations with trainable parameters, 
and measurements that produce the output of the layer. Multiple quantum architectures are provided, extracted from 
previous studies of hybrid neural networks.

**Update:** To improve efficiency of the training, the codes have been rewritten using Pennylane instead of Qiskit. 
You can still run the algorithm on Qiskit devices by providing the suitable backend name.

Quantum Fusion Model
---------------------

It is designed to efficiently integrate the extracted features from two classical neural network models to produce enhanced predictions. 
The proposed model strategically integrates 3D-CNNs and SG-CNNs to leverage their respective strengths in processing diverse 
facets of the training data. The simulation results demonstrate the superior performance of the quantum fusion model 
relative to state-of-the-art classical models.

Quantum Hadamard Edge Detection (2D and 3D)
-------------------------------------------
Performs edge detection for 2D data (images) and 3D data (volumes) using quantum operations.

Quantum-Inspired Image Filter
-----------------------------

This quantum-inspired filter is especially useful for highlighting regions with varying contrast and identifying regions of interest. 
This transformation adjusts pixel intensity based on its local contrast and overall neighborhood contribution, enhancing segmentation 
by emphasizing boundaries and transitions in the image.

Quantum State Visualizations
----------------------------

To understand the behavior and transformations of quantum circuits, visualizations play a key role. 
This library offers multiple state and circuit visualizations:

- **State Space**: Represents the evolution of quantum states at different stages of the circuit. 
  Each computational state is shown as a colored ball where the size indicates the probability of the corresponding basis state 
  and the color represents the phase.
- **Phase Disks**: Condensed representations of the state space visualization. Each qubit has a phase disk, 
  where the fullness represents the probability and the color indicates the phase.
- **Bloch Sphere**: A geometric representation of one-qubit systems. The state of a qubit is depicted as a point on the sphere, 
  visually demonstrating how the qubit's state evolves under quantum operations.
- **Q-Sphere**: Generalizes the Bloch sphere for multiple-qubit systems. Each computational basis state appears as a point on the sphere, 
  where the radius represents probability, the color indicates the phase, and the latitude represents the number of 0s and 1s in the state.

Quantum Neural Network Statistics
---------------------------------

Provides metrics to evaluate the balance between performance and complexity in quantum neural networks. Two key metrics are:

- **Entangling Capacity**: Measures the circuit's ability to generate entanglement among qubits. This property is crucial for 
  quantum computing, as entanglement is required for tasks that classical computers cannot efficiently solve.
- **Expressibility**: Refers to the ability of a quantum circuit to generate a wide variety of quantum states from the input data. 
  High expressibility ensures that the circuit can approximate any target quantum state, which is crucial for quantum neural networks.

Tensor Network Decomposition
----------------------------

One of the most effective tensor decompositions for compressing convolutional layers is the Tucker decomposition. 
This method breaks down the original four-dimensional weight tensor of a convolutional layer into multiple smaller tensors. 
This approach is particularly relevant in medical imaging, where small datasets and complex models are common. 
Tucker decomposition compresses over-parameterized layers, preserving essential information for accurate predictions while reducing 
the number of parameters, making the model faster and more efficient.

Quantum Optimization for Image Segmentation
-------------------------------------------

Provides the graph mapping for image segmentation and the formulation as a QUBO problem. 
Many quantum and quantum-inspired algorithms, such as quantum annealing and QAOA, can then be used to find the optimal segmentation mask.

Installation
==========

To install Ingenii Quantum, run:
   
.. code-block:: bash

    pip install ingenii-quantum

User Guide
==========

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   source/installation


API Reference
==========

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   source/modules

