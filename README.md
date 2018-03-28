# (AD1062) Machine Learning Fundamentals

**(AD1062) Machine Learning Fundamentals** is an Trend Micro ETP training course started from Mar. 2018. The github repository stores the sample code demonstrated during the class and homework materials.

For more information, please refer to: https://sites.google.com/view/tu-ad1062-mlfundamentals/

## Pre-requirement
### Anaconda
The sample code **demo01.ipynb**, **demo02.ipynb** are developed and tested with following components:
* Python >= 3.6
* scikit-Learn >= 0.19.1
* numpy >= 1.12.1
* matplotlib >= 2.1.1
* graphviz >= 2.38.0

To simplify the installation, it is recommended to get the latest [Anaconda](https://www.anaconda.com/download/) (Python 3.6 version) directly.

### Graphviz (for Decision Tree visualization)
The additional requirement of **demo03.ipynb**:
* python-graphviz >= 0.8.2
With anaconda installation, please execute the following command in the Anaconda Prompt:
    ```
    conda install python-graphviz
    ```

### Tensorflow and Keras (for Deep Learning applications)
The additional requirement of The sample code in the subsequent classes requires **Tensorflow** and **Keras**:
* tensorflow >= 1.4.0
* keras >= 2.1.2
    ```
    conda install -c conda-forge tensorflow
    conda install -c conda-forge keras
    ```
After the installation, please edit the `keras.json` with the pure text editor, and make sure the value of the `backend` should be set to `tensorflow` (default: `theano`). You can find your `keras.json` in the following locations:
* Windows: `%USERPROFILE%\.keras\keras.json`.
For example: `C:\Users\your_name\.keras\keras.json`
* Mac OS and Linux: `~/.keras/keras.json`

## Sample Code Brief
* **demo01.ipynb**
    * Load the built-in MNIST and IRIS dataset
    * Vector and matrix visualization and operations
    * Training set, validation set, and testing set separation
* **demo02.ipynb**: Linear Classifiers
    * Perceptron
    * Support Vector Machine (SVM) - Linear scenario
* **demo03.ipynb**
    * Multi-Layer Perceptron
    * Support Vector Machine (SVM) - Non-Linear scenario
    * Decision Tree Classifier
    * Gradient Boosting

