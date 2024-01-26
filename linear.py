import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

def generate_linear_dataset(var):
    x = np.arange(var)
    delta = np.random.uniform(-10, 10, size=(var,))
    y = 4 + x * 3 + delta
    return x, y

def least_squares_fit(x, y):
    x_mean, y_mean = np.mean(x), np.mean(y)
    slope_xy = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    start_value = y_mean - slope_xy * x_mean
    return slope_xy, start_value

def linear_function(x, slope, start_value):
    return start_value + slope * x

def calculate_best_fit(x, slope, start_value):
    return linear_function(x, slope, start_value)

def calculate_random_line(x):
    return np.random.uniform(-10, 10) * x + np.random.uniform(-10, 10)

def visualize_linear_function(x, y, slope, start_value, title, save_path):
    best_fit = calculate_best_fit(x, slope, start_value)
    random_line = calculate_random_line(x)

    plt.scatter(x, y)
    plt.plot(x, best_fit, label='Best Fit Line', color='r')
    plt.plot(x, random_line, label='Random Line', linestyle='--', color='g')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.savefig(save_path, dpi=50)
    plt.show()
    plt.close()

def calculate_residuals(y_true, y_pred):
    return y_true - y_pred

def calculate_mse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)

def visualize_residuals(x, y_true, y_best_fit, y_random_line):
    residuals_best_fit = calculate_residuals(y_true, y_best_fit)
    residuals_random_line = calculate_residuals(y_true, y_random_line)

    plt.scatter(x, y_true, label='True Values')
    plt.plot(x, y_best_fit, label='Best Fit Line', color='r')
    plt.plot(x, y_random_line, label='Random Line', linestyle='--', color='g')
    
    for xi, yt, ybf, yrl in zip(x, y_true, y_best_fit, y_random_line):
        plt.vlines(xi, yt, ybf, colors='gray', linestyles='dashed', alpha=0.5)
        plt.vlines(xi, yt, yrl, colors='gray', linestyles='dotted', alpha=0.5)

    plt.title('Visualizing Residuals')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()
    plt.close()

def main():
    var = 20
    x, y = generate_linear_dataset(var)
    slope, start_value = least_squares_fit(x, y)

    title = "Linear Regression Visualization for Linear Dataset"
    save_path = "assets/Visualization_Linear_Dataset.png"
    visualize_linear_function(x, y, slope, start_value, title, save_path)

    best_fit = calculate_best_fit(x, slope, start_value)
    random_line = calculate_random_line(x)

    visualize_residuals(x, y, best_fit, random_line)

    mse_best_fit = calculate_mse(y, best_fit)
    mse_random_line = calculate_mse(y, random_line)

    print(f'MSE (Best Fit): {mse_best_fit:.4f}')
    print(f'MSE (Random Line): {mse_random_line:.4f}')

if __name__ == "__main__":
    main()

