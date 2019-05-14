# (AD1062) Machine Learning Fundamentals

**(AD1062) Machine Learning Fundamentals** is an Trend Micro ETP training course. The github repository stores the sample code demonstrated during the class and homework materials.

For more information, please refer to: https://sites.google.com/view/tu-ad1062-mlfundamentals/

## Table of contents
- [Installation](#installation)
    - [Option 1. Setup the Environment Manually](#option-1-setup-the-environment-manually)
    - [Option 2. Setup the Environment by Docker](#option-2-setup-the-environment-by-docker)
- [Usage](#usage)
- [Frequently Asked Questions](#frequently-asked-questions)
    - [May I use Python 2.7?](#1-may-i-use-python-27)
    - [May I use Anaconda or WinPython?](#2-may-i-use-anaconda-or-winpython)
    - [Keeps showing "No module named 'theano'" error?](#3-keeps-showing-no-module-named-theano-error)
- [Appendix](#appendix)
    - [How to Install Python 3.7 and Related Dependencies Manually?](#how-to-install-python-37-and-related-dependencies-manually)
        - [Windows](#windows)
        - [macOS](#macos)
        - [Linux](#linux)
----
## Installation
All jupyter notebook sample code are developed based on Python 3, Scikit-Learn and Tensorflow with Keras front-end. To execute the sample code, please select **one** of methods listed below:

### Option 1. Setup the Environment Manually
Please follow the steps listed below:
1. Install Python 3.7
(For more details, see: [Appendix：How to Install Python 3.7 and Related Dependencies Manually?](#how-to-install-python-37-and-related-dependencies-manually))
2. Clone the git repository:
    ```
    $ git clone https://github.com/jessee-kung/tu-etp-ad1062.git
    ```
3. **(Optional)** Create a virtual environment under the repository folder and activate it if you want to have an isolated environment:
    ```
    $ mkdir .venv
    $ python3 -m venv /your/path/to/tu-etp-ad1062/.venv
    $ source .venv/bin/activate
    ```
4. Install all dependencies:
    - You can do it by:
        ```
        $ pip3 install sklearn jupyter matplotlib tensorflow keras keras-rl lightgbm graphviz opencv-python pillow pandas
        ```
    - Or navigate to the folder of git repository, then install the dependencies by `requirements.txt` as below :
        ```
        $ cd tu-etp-ad1062
        $ pip3 install -r requirements.txt 
        ```

Done!

### Option 2. Setup the Environment by Docker
If you already have Docker installed on your machine, then you can simply build an image from the `Dockefile`, and bind mount the project folder into the container as the Jupyter notebook working directory.  There is also a prepared Makefile for simplifing the steps with 4 pre-defined targets:
1. Build Docker image. By default the image will be named `tu-etp-ad1062:pynb`
    ```
    $ make build
    ```
2. Start server. The server will listen on port `8888`. Once the server is started, there should be a message showing you the secret token for your notebook.
    ```
    $ make start
    ```
3. Stop server.
    ```
    $ make stop
    ```
4. Clean Docker image. If you want to rebuild the Docker image or you have finished the course, then you are free to remove the image.
    ```
    $ make clean
    ```

> #### Acknowledgements:
> Thanks to [Chuck Lin](https://github.com/chucklin) for the Dockerfile!

----
## Usage
Launch jupyter notebook for execution of sample code and playground:
```
$ jupyter notebook
```

If the environment is installed by Docker, simply launch jupyter notebook as follows:
```
$ make start
```

Here's the summary of each `*.ipynb`: 
* **demo_01.ipynb**: Ch1. Overview
    * Load the Keras built-in MNIST dataset
    * Vector and matrix visualization and operations
    * Training set, validation set, and testing set separation
* **demo_02.ipynb**: Ch2. Linear Classifiers
    * Perceptron
    * Support Vector Machine (SVM) - Linear scenario
* **demo_03.ipynb**: Ch3. Non-Linear Classifiers
    * Multi-Layer Perceptron
    * Support Vector Machine (SVM) - Non-Linear scenario
    * Decision Tree Classifier
    * Gradient Boosting
* **demo_04.ipynb**: Ch4. Convolutional Neural Network
    * Convolutional Neural Network on Images
        * Use CNN For MNIST classification
        * Bases observation
    * Convolutional Neural Network on Texts
        * Use CNN For IMDB movie comment dataset classification
    * Pre-trained models
        * Use InceptionV3 for wild-image classifications
* **demo_05.ipynb**: Ch5. Sequential Learning
    * Text data pre-processing steps:
        * Tokenization
        * Top-K words encoding (Based on occurrences)
        * Word2Vec convert with GloVe
    * Classification with LSTM
* **demo_06.ipynb**: Ch6. Generative Adversarial Network
    * TBD
* **demo_07.ipynb**: Ch7. Dimension Reduction
    * Dimension reduction of PCA, LDA, and t-SNE

----
## Frequently Asked Questions
### 1. May I use Python 2.7?
Not recommended. Sample code are tested with Python 3.x only.

### 2. May I use Anaconda or WinPython?
You can also use Anaconda or WinPython based on Python 3, too. But it is not required, due to these integrated packages provides more components which may not be used in this course (and occupies more disk space). You also have to install Keras and Tensorflow later once you have your Anaconda or WinPython installed.

### 3. Keeps showing "No module named 'theano'" error?
If you already have an earlier version of Keras installed, make sure the value of `backend` attribute should be `tensorflow`:
```
{
   "image_data_format": "channels_last",
   "epsilon": 1e-07,
   "floatx": "float32",
   "backend": "tensorflow"
}
```
You can find your `keras.json` in the following locations:
* Windows: `%USERPROFILE%\.keras\keras.json`.
* Mac OS and Linux: `~/.keras/keras.json`

----
## Appendix
### How to Install Python 3.7 and Related Dependencies Manually?
#### Windows
Get the installation package directly from the Python official website:
https://www.python.org/downloads/release/python-372/

#### macOS
1. Install Xcode and Homebrew first:
    ```
    $ xcode-select --install
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
2. Install Python 3:
    ```
    $ brew install python3
    ```
3. Make sure your Python 3.7 is worked:
    ```
    $ python3 --version
    ```

#### Linux
If your Linux distributions provides no official Python 3 packages in its package management system (i.e., `apt`, `yum`, `dnf`, `pkg` ., etc.), you can manually install Python 3.7 by steps listed as follows, with elevated user privileges (e.g., `sudo` with each command or `su - root` first):
1. Make sure that all dependencies of building Python is satisfied, including `gcc`, `bzip2-devel`, `openssl-devel` and `libffi-devel`. You can installed by the commands listed below if your Linux distribution matches one of them:
    - On Ubuntu, or Debian:
        ```
        $ apt-get install build-essential autoconf libtool pkg-config zlibc zlib1g-dev libssl-dev libxslt1-dev libxslt-dev libffi-dev libxml2-dev
        ```
    - On CentOS, Scientific Linux, or Red Hat Enterprise Linux:
        ```
        $ yum install gcc bzip2-devel zlib-devel openssl-devel libffi-devel libxslt-devel libxml2-devel 
        ```
2. Get the latest Python 3.7 package:
    ```
    $ wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
    ```
3. Configure and install as follows:
    ```
    $ ./configure --enable-optimizations
    $ make altinstall
    ```
4. To ensure that the newly installed Python 3.x doesn't conflict with the OS built-in Python 2.7, it is recommended to create symbolic links and access Python 3.x by using `python3` and `pip3`:
    ```
    $ ln -s /usr/local/bin/python3.7 /usr/sbin/python3
    $ ln -s /usr/local/bin/pip3.7 /usr/sbin/pip3
    ```
5. Make sure your Python 3.7 is worked:
    ```
    python3 --version
    ```