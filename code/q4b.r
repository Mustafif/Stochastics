# Set the parameters
n <- 1000 # number of observations
theta <- 0.3 # value of theta
df <- 4 # degrees of freedom for t-student distribution

# Generate a t-student white noise
Z <- rt(n, df = df)

# Initialize the moving average process
X <- rep(0, n)

# Define the moving average process
for (t in 2:n) {
  X[t] <- Z[t] + theta * Z[t - 1]
}

# Plot the simulated values
plot(X,
  type = "l",
  main = "Moving average process with t-student noise",
  xlab = "Time", ylab = "Value"
)
