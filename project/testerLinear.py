# Import classes
from LinearModels import *
from diagnosticPlot import *
from DataSet import *
import statsmodels.api as sm
import numpy as np

# Import dataset from csvData class
data = csvDataSet("real_estate.csv", scaled=True)
data.add_constant()
x_array = data.x
y_array = data.y


###### Define and fit model parameters
#### Regression 1: "y ~ b0 + b1*x2 + b2*x3 + b3*x4"
reg_1 = LinearRegression(x_array, y_array)
reg_1.linearMethod("y ~ b0 + b1*x2 + b2*x3 + b3*x4")
reg_1.optimize()

# Compare with statsmodels
x_ols_1       = np.transpose(x_array)
x_ols_1       = np.delete(x_ols_1, [1,5,6], 1)
results_ols_1 = sm.OLS(y_array, x_ols_1).fit()

# Print statmodels OLS Parameters and R2
print("Expected params:", np.round(results_ols_1.params,4), "\nExpected R2:", np.round(results_ols_1.rsquared,4))

# Print LinearRegression summary
print(reg_1.summary())

# Plot Regression 1
dp1 = diagnosticPlot(reg_1)
dp1.plot(reg_1.y, reg_1.predict(reg_1.params))




#### Regression 2: "y ~ b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5"
reg_2 = LinearRegression(x_array, y_array)
reg_2.linearMethod("y ~ b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5")
reg_2.optimize()

# Compare with statsmodels
x_ols_2       = np.transpose(x_array)
x_ols_2       = np.delete(x_ols_2, 6, 1)
results_ols_2 = sm.OLS(y_array, x_ols_2).fit()

# Print statmodels OLS Parameters and R2
print("Expected params:", np.round(results_ols_2.params,4), "\nExpected R2:", np.round(results_ols_2.rsquared,4))

# Print LinearRegression summary
print(reg_2.summary())

# Plot Regression 2
dp2 = diagnosticPlot(reg_2)
dp2.plot(reg_2.y, reg_2.predict(reg_2.params))



#### Regression 3: "y ~ b1*x1"
reg_3 = LinearRegression(x_array, y_array)
reg_3.linearMethod("y ~ b1*x1")
reg_3.optimize()

# Compare with statsmodels
x_ols_3       = np.transpose(x_array)
x_ols_3       = np.delete(x_ols_3, [0, 2,3,4,5,6], 1)
results_ols_3 = sm.OLS(y_array, x_ols_3).fit()
results_ols_3.summary()

# Print statmodels OLS Parameters and R2
print("Expected params:", np.round(results_ols_3.params,4), "\nExpected R2:", np.round(results_ols_3.rsquared,4))

# Print LinearRegression summary
print(reg_3.summary())

# Plot Regression 3
dp3 = diagnosticPlot(reg_3)
dp3.plot(reg_3.y, reg_3.predict(reg_3.params))


