# Set the parameters
n <- 1000 # number of observations
theta <- 0.3 # value of theta (k/10) k = 3
sigma <- 1 # standard deviation of white noise

# Generate a Gaussian white noise
Z <- rnorm(n, mean = 0, sd = sigma)

# Initialize the moving average process
X <- rep(0, n)

# Define the moving average process
for (t in 2:n) {
    X[t] <- Z[t] + theta * Z[t - 1]
}

# Plot the simulated values
plot(X, type = "l",
main = "Moving average process with Gaussian noise",
xlab = "Time", ylab = "Value")
