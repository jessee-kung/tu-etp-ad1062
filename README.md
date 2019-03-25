# (AD1062) Machine Learning Fundamentals

**(AD1062) Machine Learning Fundamentals** is an Trend Micro ETP training course. The github repository stores the sample code demonstrated during the class and homework materials.

For more information, please refer to: https://sites.google.com/view/tu-ad1062-mlfundamentals/

----
## Installation
All jupyter notebook sample code are developed based on Python 3, Scikit-Learn and Tensorflow with Keras front-end. To execute the sample code, please follow the steps listed below:
1. Install Python 3.7
(For more details, see: [Appendix 1](#appendix-1\.-install-python-3\.7-and-related-dependencies))
2. Clone the git repository:
    ```
    $ git clone https://github.com/jessee-kung/tu-etp-ad1062.git
    ```
3. Install all dependencies:
    - You can do it by:
        ```
        $ pip3 install sklearn jupyter matplotlib tensorflow keras keras-rl graphviz opencv-python
        ```
    - Or navigate to the folder of git repository, then install the dependencies by `requirement.txt` as below :
        ```
        $ cd tu-etp-ad1062
        $ pip3 install -r requirement.txt 
        ```

Done!

----
## Usage
Launch jupyter notebook for execution of sample code and playground:
```
$ jupyter notebook
```

Here's the summary of each `*.ipynb`: 
* **demo01.ipynb**: Ch1. Overview
    * Load the Keras built-in MNIST dataset
    * Vector and matrix visualization and operations
    * Training set, validation set, and testing set separation
* **demo02.ipynb**: Ch2. Linear Classifiers
    * Perceptron
    * Support Vector Machine (SVM) - Linear scenario
* **demo03.ipynb**: Ch3. Non-Linear Classifiers
    * Multi-Layer Perceptron
    * Support Vector Machine (SVM) - Non-Linear scenario
    * Decision Tree Classifier
    * Gradient Boosting
* ...
* **demo08.ipynb**: Ch8. Dimension Reduction
    * Dimension reduction of PCA, LDA, and t-SNE

----
## Frequently Asked Questions:
### 1. May I use Python 2.7?
Not recommended. Sample code are tested with Python 3.x only.

### 2. May I use Anaconda or WinPython?
You can also use Anaconda or WinPython based on Python 3, too. But it is not required, due to these integrated packages provides more components which may not used in this course (and occupies more disk space). You also have to install Keras and Tensorflow later after you install the Anaconda or WinPython.

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
### Install Python 3.7 and Related Dependencies
#### Windows
Get the installation package from: https://www.python.org/downloads/release/python-372/

#### macOS
(TBD)

#### Linux
Please manually install Python 3.7 by steps listed as follows, with elevated user privileges (e.g., `sudo` with each command or `su - root` first):
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