from LinearModels import *

##
#  This module defines the diagnosticPlot class which returns a plot based on the function input
#
class diagnosticPlot():
    
    ## Initializes the class where the linear model input is recognized as a linear regression or logistic regression
    #  @param linearmodel fitted linear model (linear reg. or logistic reg.)
    #  @return returns instance variable "LinearRegression" if model type is LinearRegression
    #  else if model type is LogisticRegression it returns instance variable "LogisticRegression"
    #
    def __init__(self, linearmodel):
        self._linearmodel = linearmodel
        
        if isinstance(linearmodel, LinearRegression) == True:
            self._method = "LinearRegression"
            print("Object is an instance of Linear Regression")
            
        elif isinstance(linearmodel, LogisticRegression) == True:
            self._method = "LogisticRegression"
            print("Object is an instance of Logistic Regression")
    
    ## Method which plots either a scatter plot (y against mu) for Linear Regression or a ROC Curve for Logistic regressions
    #  @param y numpy array of dependent variable y
    #  @param mu numpy array of predicted mu variables (y_hat)
    #  @returns scatterplot if model is LinearRegression or ROC Curve plot if model is LogisticRegression
    #
    def plot(self, y, mu):
        import matplotlib.pyplot as plt
        from sklearn import metrics
        
        if self._method == "LinearRegression":
            plt.scatter(y, mu)
            plt.title(f"Specified model: {self._linearmodel.model()}")
            plt.xlabel("y")
            plt.ylabel("mu (y_hat)")
        
        elif self._method == "LogisticRegression":
            fpr, tpr, thresholds = metrics.roc_curve(y, mu)
            roc_auc = metrics.auc(fpr, tpr)
            display = metrics.RocCurveDisplay(fpr = fpr, tpr = tpr, roc_auc = roc_auc, estimator_name ='ROC curve')
            display.plot()
            plt.show()    