# i)
#######################################################################
# Install the moments package if not already installed
if (!requireNamespace("moments", quietly = TRUE)) {
  install.packages("moments")
}

# Load the moments package
library(moments)


# Read the CSV file
data <- read.csv("AAPL.csv")

# Extract daily returns and prices
daily_returns_str <- data$Change
daily_returns <- as.numeric(sub("%", "", daily_returns_str))
prices <- data$Price

# Create a data frame
df <- data.frame(DailyReturns = daily_returns, Prices = prices)

# Create a boxplot
plot(df,
  main = "AAPL Historical Data",
  xlab = "Daily Returns (%)",
  ylab = "Prices ($)",
  pch = 16, # Set the point character (16 for solid circles)
  col = "blue" # Set point color
)

# ii)
######################################################################

# First four moments for prices series
prices_mean <- mean(prices)
cat("Mean of prices:", prices_mean, "\n")

prices_std <- sd(prices)
cat("Standard deviation of prices:", prices_std, "\n")

prices_skew <- skewness(prices)
cat("Skewness of prices:", prices_skew, "\n")

prices_kurt <- kurtosis(prices)
cat("Kurtosis of prices:", prices_kurt, "\n")

cat("\n")

# First four moments for daily returns
dr_mean <- mean(daily_returns)
cat("Mean of daily returns:", dr_mean, "\n")

dr_std <- sd(daily_returns)
cat("Standard deviation of daily returns:", dr_std, "\n")

dr_skew <- skewness(daily_returns)
cat("Skewness of daily returns:", dr_skew, "\n")

dr_kurt <- kurtosis(daily_returns)
cat("Kurtosis of daily returns:", dr_kurt, "\n")

# iii)
######################################################################
# emperical pdf from kernel density estimate
kde <- density(daily_returns)
# plot the empirical PDF
plot(kde,
  main = "Empirical PDF vs. Gaussian PDF",
  xlab = "Returns",
  ylab = "Density",
  col = "red"
)

# compute Gaussian PDF
x <- seq(min(daily_returns), max(daily_returns))
gaussian_pdf <- dnorm(x, mean = dr_mean, sd = dr_std)
lines(x, gaussian_pdf, col = "blue", lty = 2)
legend("topright", legend = c("Empirical PDF", "Gaussian PDF"), col = c("red", "blue"), lty = c(1, 2))
