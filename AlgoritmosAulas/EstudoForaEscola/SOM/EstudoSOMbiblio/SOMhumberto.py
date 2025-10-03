import numpy as np
import matplotlib.pyplot as plt

def generate_inputs(n=100):

    mean = [-5, -2]
    cov = [[.1, 0], [0, .1]]  # diagonal covariance
    c1 = np.random.multivariate_normal(mean, cov, size=n//3)

    mean = [-2, 3]
    cov = [[.1, 0], [0, .1]]  # diagonal covariance
    c2 = np.random.multivariate_normal(mean, cov, size=n//3)

    mean = [3, 1]
    cov = [[.1, 0], [0, .1]]  # diagonal covariance
    c3 = np.random.multivariate_normal(mean, cov, size=(n//3+n%3))

    inputs = np.concatenate((c1, c2, c3))

    np.random.shuffle(inputs)

    # normalization
    return inputs

class SOM:
    def __init__(self, M, N, dim=2, sigma_0=5, learning_rate_0=0.1, tau=1000):
        """Initialize the SOM with a 2D grid of neurons."""
        self.M = M  # Rows in the grid
        self.N = N  # Columns in the grid
        self.dim = dim  # Input dimension (2 for 2D inputs)
        self.weights = np.random.rand(M, N, dim)  # Random weights in [0,1]
        self.sigma_0 = sigma_0  # Initial neighborhood radius
        self.learning_rate_0 = learning_rate_0  # Initial learning rate
        self.tau = tau  # Decay time constant

    def find_bmu(self, x):
        """Find the Best Matching Unit for input vector x."""
        diff = self.weights - x  # Broadcasting: (M, N, 2) - (2,) -> (M, N, 2)
        dist = np.sum(diff**2, axis=2)  # Squared Euclidean distance
        bmu_idx = np.unravel_index(np.argmin(dist), (self.M, self.N))  # (i,j) coordinates
        return bmu_idx

    def train_step(self, x, t):
        """Perform one training step for input x at iteration t."""
        bmu_idx = self.find_bmu(x)
        # Compute decaying parameters
        sigma = self.sigma_0 * np.exp(-t / self.tau)
        learning_rate = self.learning_rate_0 * np.exp(-t / self.tau)
        # Compute neighborhood function for all neurons
        rows, cols = np.ogrid[0:self.M, 0:self.N]
        dist_sq = (rows - bmu_idx[0])**2 + (cols - bmu_idx[1])**2
        h = np.exp(-dist_sq / (2 * sigma**2))  # Shape: (M, N)
        # Update weights
        diff = x - self.weights  # Shape: (M, N, 2)
        update = learning_rate * h[:, :, np.newaxis] * diff  # Broadcasting h to (M, N, 1)
        self.weights += update

    def train(self, data, T):
        """Train the SOM for T iterations using the input data."""
        for t in range(T):
            x = data[np.random.randint(0, len(data))]  # Random sample
            self.train_step(x, t)

# Generate random 2D data
np.random.seed(0)
data = generate_inputs(n=1000)

# Initialize and train the SOM
som = SOM(M=10, N=10, dim=2, sigma_0=5, learning_rate_0=0.1, tau=1000)
som.train(data, T=10000)

# Visualization
weights = som.weights
plt.scatter(data[:, 0], data[:, 1], c='gray', alpha=0.5, label='Data')
# Plot SOM grid
for i in range(som.M):
    for j in range(som.N):
        if i < som.M - 1:  # Connect to the neuron below
            plt.plot([weights[i, j, 0], weights[i+1, j, 0]],
                     [weights[i, j, 1], weights[i+1, j, 1]], 'r-')
        if j < som.N - 1:  # Connect to the neuron to the right
            plt.plot([weights[i, j, 0], weights[i, j+1, 0]],
                     [weights[i, j, 1], weights[i, j+1, 1]], 'r-')
plt.scatter(weights[:, :, 0].flatten(), weights[:, :, 1].flatten(), c='red', label='SOM Neurons')
plt.legend()
plt.title('SOM with 2D Inputs')
plt.show()