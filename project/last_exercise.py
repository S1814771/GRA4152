#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:37:51 2022

The code below is written to provide a description to the code for part 4.1 from mid-term exam
There are some adjustments in the code for the mid-term task needed to make the argparse code work properly and in accordance with the current assignment task
"""
import argparse, textwrap

# Since it is explicitly specified that we should describe the LogisticRegression class, I wirte in intro what the code from the mid-tern task 4.1 does in description
# and describe the LogisticRegression in details using epilog
parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter,
                                 description = textwrap.dedent('''\
                                                               The code running a tester of LogisticRegression class
                                                               --------------------------------------------------------------------
                                                               The tester invokes the LogisticRegression class
                                                               LogisticRegression class runs logistisc regression on feeded x and y
                                                               The class uses log optimization to fit the model
                                                               ROC curve is used as model performance measure
                                                               '''),
                                epilog = textwrap.dedent('''\
--------------------------------------------------------------------
The class has several methods like fit(), optimize(), diagnosis(), etc.
The tester runs the logistic regression on three given models:
     y ~ b0 + b1*x1
     y ~ b0 + b1*x1 +b2*x2
     y ~ b0 + b1*x1 +b2*x2 + b3*x3
And compare the results with an in-built regression tools
'''))

### Add arguments for seed value, share of training data, list of covariates to feed in model, and argument to make plot
parser.add_argument("-s", "--seed", default = 12345, type = int, help = "Argument is used to set the seed") # Default value is 12345, corresponding to mid-term task

# Given that in my code for the mid-term I have 70%/30% as default for train/test split I use the "required" parameter to push user to specify the share for training set
parser.add_argument("-tr", "--train", type = float, required = True, help = "The argument to split dataset into training and test set. The argument must be specified")

# In the mid-term code we work with three models, therefore, the combination of corresponding covariates for each scenario are (1) x1; (2) x1, x2; and (3) x1, x2, x3
# Therefore, the covariates the user can choose only one this combinations
parser.add_argument("-c", "--covariates", type = str, required = True, choices = ["x1", "x1, x2", "x1, x2, x3"], help = "Argument to specify the covariates to be included in the model. In accordance with mid-term taks we cank choose between 'x1', 'x1, x2', and 'x1, x2, x3' covariates in the model")

# This argument makes plot if bool specified similar approach as to the code from the lecture 10
parser.add_argument("-mp", "--make_plot", action = "store_true", help = "The user need to call the argument to plot")                                    

# call args
args = parser.parse_args()

### Incorporate argparse to the code from the mid-term
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
data.train_test(train_set = args.train, seed = args.seed)
x_te = data.x_te
x_tr = data.x_tr
y_te = data.y_te
y_tr = data.y_tr


###### Define and fit model parameters
if args.covariates == "x1":
    model = "y ~ b0 + b1*x1"
if args.covariates == "x1, x2":
    model = "y ~ b0 + b1*x1 + b2*x2"
if args.covariates == "x1, x2, x3":
    model = "y ~ b0 + b1*x1 + b2*x2 + b3*x3"
    
reg = LogisticRegression(x_tr, y_tr)
reg.linearMethod(model)
reg.optimize()


# Print LogitRegression summary
print(reg.summary())

# Plot Regression with y test and predicted mu on test set if argument called
if args.make_plot == True:
    if model == "y ~ b0 + b1*x1":
        dp = diagnosticPlot(reg)
        dp.plot(y_te, reg.predict(reg.params, x_te[(0,1),:]))
    if model == "y ~ b0 + b1*x1 + b2*x2":
        dp = diagnosticPlot(reg)
        dp.plot(y_te, reg.predict(reg.params, x_te[:3,:]))
    if model == "y ~ b0 + b1*x1 + b2*x2 + b3*x3":
        dp = diagnosticPlot(reg)
        dp.plot(y_te, reg.predict(reg.params, x_te))