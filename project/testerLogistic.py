# Import classes
from LinearModels import *
from diagnosticPlot import *
from DataSet import *
import numpy as np
import statsmodels.api as sm

# Load dataset spector
spector = sm.datasets.spector.load_pandas()

# Feed into DataSet class
data = DataSet(spector.exog.values, spector.endog.values, scaled=False)
data.add_constant()

# Test and train sets
data.train_test(train_set = 0.7, seed = 12345)
x_te = data.x_te
x_tr = data.x_tr
y_te = data.y_te
y_tr = data.y_tr


###### Define and fit model parameters
#### Regression 1: "y ~ b0 + b1*x1"
reg_1 = LogisticRegression(x_tr, y_tr)
reg_1.linearMethod("y ~ b0 + b1*x1")
reg_1.optimize()

# Compare with statsmodels
x_log_1       = np.transpose(x_tr)
x_log_1       = np.delete(x_log_1, [2,3], 1)
results_log_1 = sm.Logit(y_tr, x_log_1).fit()

# Print statmodels Logit Parameters
print("Expected params:", np.round(results_log_1.params,4))

# Print LogitRegression summary
print(reg_1.summary())

# Plot Regression 1 with y test and predicted mu on test set
dp_1 = diagnosticPlot(reg_1)
dp_1.plot(y_te, reg_1.predict(reg_1.params, x_te[(0,1),:]))





#### Regression 2: "y ~ b0 + b1*x1 +b2*x2"
reg_2 = LogisticRegression(x_tr, y_tr)
reg_2.linearMethod("y ~ b0 + b1*x1 + b2*x2")
reg_2.optimize()

# Compare with statsmodels
x_log_2       = np.transpose(x_tr)
x_log_2       = np.delete(x_log_2, 3, 1)
results_log_2 = sm.Logit(y_tr, x_log_2).fit()

# Print statmodels Logit Parameters
print("Expected params:", np.round(results_log_2.params,4))

# Print LogisticRegression summary
print(reg_2.summary())

# Plot Regression 2
dp_2 = diagnosticPlot(reg_2)
dp_2.plot(y_te, reg_2.predict(reg_2.params, x_te[:3,:]))




#### Regression 3: "y ~ b0 + b1*x1 +b2*x2 + b3*x3"
reg_3 = LogisticRegression(x_tr, y_tr)
reg_3.linearMethod("y ~ b0 + b1*x1 + b2*x2 + b3*x3")
reg_3.optimize()

# Compare with statsmodels
x_log_3       = np.transpose(x_tr)
#x_log_3       = np.delete(x_log_2, 3, 1)
results_log_3 = sm.Logit(y_tr, x_log_3).fit()

# Print statmodels Logit Parameters
print("Expected params:", np.round(results_log_3.params,4))

# Print LogisticRegression summary
print(reg_3.summary())

# Plot Regression 3
dp_3 = diagnosticPlot(reg_3)
dp_3.plot(y_te, reg_3.predict(reg_3.params, x_te))


