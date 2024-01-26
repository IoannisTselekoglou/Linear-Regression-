# Linear Regression 

## Table of Contents

- [Introduction](#introduction)
- [Examples](#examples)
- [Conclusion](#testing)
- [Dependencies](#testing)
- [License](#license)

## Introduction

This Python project implements Linear Regression algorithms from scratch. The primary goal is to have a comprehensible implementation of these fundamental machine learning algorithms.

### Linear Regression

Linear Regression is a supervised learning algorithm designed for predicting continuous target values based on input features. Its objective is to identify the best-fit straight line that minimizes the sum of squared errors between predicted and actual values.

## Examples

To illustrate the usage of the implemented algorithms, let us run the following Python script and visualize the output:

- [linear.py](/linear.py): Demonstrates Linear Regression applied to a random dataset.

![image](/assets/Regression_Visulaization.png)

## Conclusion

When visualizing the graphs, we can observe the distance between the actual datapoints and the linear lines.

![image](/assets/Residiual_Visulaization.png)


Comparing the mean squared error values, we can see that the algorithm for calculating the best fit is significantly better than, for example, the random line.

- MSE (Best Fit): 18.8928
- MSE (Random Line): 28.1110



## Dependencies

```bash pip install matplotlib
$ pip install -U matplotlib
$ pip install numpy
$ pip install -U scikit-learn
```

## License
- [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
- [NumPy](https://numpy.org): A open-source library for numerical computing in Python.
- [Matplotlib](https://matplotlib.org): A open-source plotting library for Python. License.

