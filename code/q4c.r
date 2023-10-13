# Set the parameters
n <- 1000 # number of observations
theta <- 0.3 # value of theta
sigma <- 1 # standard deviation of white noise
# Generate a Gaussian white noise
Z <- rnorm(n, mean = 0, sd = sigma)
# Initialize the moving average process
X <- rep(0, n)
# Define the moving average process
for (t in 2:n) {
    X[t] <- Z[t] + theta * Z[t - 1]
}
# Define a function to calculate the empirical autocorrelation
autocorr <- function(x, h) {
    # x is the input series, h is the lag
    n <- length(x) # length of the series
    x_mean <- mean(x) # mean of the series
    num <- sum((x[(h + 1):n] - x_mean) * (x[1:(n - h)] - x_mean)) # numerator
    den <- sum((x - x_mean)^2) # denominator
    return(num / den)
}
# Set the maximum lag to plot
max_lag <- 10
# Plot the empirical autocorrelation 
# function for Gaussian noise process
plot(sapply(0:max_lag, function(h) autocorr(X, h)), type = "h",
main = "Empirical autocorrelation function 
for Gaussian noise process",
xlab = "Lag", ylab = "Autocorrelation")
