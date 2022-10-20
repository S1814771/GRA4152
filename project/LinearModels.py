
##
#  This module defines the LM (Linear Models) superclass which works as a base for regression models
#

class LM():
    _intercept = "b0"
    ## Initializes with dependent variable(endogenous) y and independent(exogenous) variables x 
    #  @param x numpy array of independent/covariates x specified by user
    #  @param y numpy array of dependent variable y specified by user
    #
    def __init__(self, x, y):
        self._model = ""
        self._x = x
        self._y = y
    
    ## Construct a string which recognizes the dependent variables based on a string format.
    #  @param linmodel user specified string for regression model, e.g. "y ~ b0 + b1*x1"
    #
    def linearMethod(self, linmodel):
        self._model = linmodel      
        
        # Splits string based on "x" and retrieve covariates corresponding to string
        model_stripped    = linmodel.split("x")[1:]
        for i in range(len(model_stripped)):
            model_stripped[i-1] = int(model_stripped[i-1].split(" ")[0])
        
        if LM._intercept in self._model:
            model_stripped.insert(0, 0)
        
        # Update covariates according to specified model
        self._x = self._x[model_stripped, :] 
        
        # Saves length of parameters for use in optimize method
        self._len_params = len(model_stripped)
    
    ## Accessor method. User can retrieve x
    #  @return numpy array of dependent variables x
    #  @property is decorator
    @property        
    def x(self):
        return self._x
    
    ## Accessor method. User can retrieve y
    #  @return numpy array of independent variable y
    #  @property is decorator
    @property
    def y(self):
        return self._y
    
    ## Accessor method. User can retrieve beta parameters
    #  @return numpy array of beta parameters
    #  @property is decorator
    @property
    def params(self):
        return self._params
    
    ## String representation of specified model
    #  @return model specified in LM in string representation
    def model(self):
        return self._model
    
    ## Abstract class. Method for calculating model performance/accuracy
    #  @raise return to be specified in subclasses. Model specific
    def diagnosis(self):
        raise NotImplementedError
    
    ## Abstract class. Method for modelling the deviance
    #  @raise return to be specified in subclasses. Model specific
    def fit(self):
        raise NotImplementedError
    
    ## Abstract class. Method for modelling estimate for mu (y_hat)
    #  @raise return to be specified in subclasses. Model specific  
    def predict(self):
        raise NotImplementedError
    
    ## Numerical minimization using spicy package
    #  @param init_val initial values for beta parameters (default set to 1)
    #  @return returns minimized beta parameters
    def optimize(self, init_val = 1):                                      
        from scipy.optimize import minimize 
        import numpy as np
        
        init_params  = np.repeat(init_val , self._len_params)              
        results      = minimize(self.fit, init_params) 
        self._params = results['x']
    
    ## Prints out string with fitted parameters
    #  @return if model is not specified, it prints: "I am a LinearModel"
    #  @return if model is specified but not fitted it prints: specified model with 0s in all parameters
    #  @return if model is specified and fitted it prints: specified model with fitted parameters
    def __repr__(self):
        if self._model == "":
            return str("I am a LinearModel")
        elif hasattr(self, "params") == False and self._model != "":
            string_stripped    = self._model.split("b")[1:]
            "".join(string_stripped)
            for i in range(len(string_stripped)):
                string_stripped[i] = string_stripped[i].replace(string_stripped[i][0], "0")
            string = "".join(string_stripped)
            string = "".join(("y ~ ", string))
            return string
        else:
            import numpy as np
            string_stripped    = self._model.split("b")[1:]
            "".join(string_stripped)
            for i in range(len(string_stripped)):
                string_stripped[i] = string_stripped[i].replace(string_stripped[i][0], str(np.round(self._params[i], decimals = 4)))
            string = "".join(string_stripped)
            string = "".join(("y ~ ", string))
            return string
    
    ## Prints out the model specified in LM, the fitted parameters, and the model accuracy
    #
    def summary(self):
        import numpy as np
        print("                            LINEAR MODEL                                ")
        print("========================================================================")
        print("Model Specified:   ", self._model)
        print("Fitted Parameters: ", np.round(self._params,4))
        print("Model Accuracy:    ", np.round(self.diagnosis(),4))
        print("========================================================================")

## 
#  This module defines the LinearRegression subclass that models linear regressions
#
class LinearRegression(LM):
    
    ## Initializes with dependent variable(endogenous) y and independent(exogenous) variables x. 
    #  Inherits from superclass LM
    #  @param x numpy array of independent/covariates x specified by user
    #  @param y numpy array of dependent variable y specified by user
    def __init__(self, x, y):
        super().__init__(x,y)
    
    ## Method for modelling estimate for mu (y_hat)
    #  @param params are beta parameters
    #  @return returns the modelled mu (y_hat)         
    def predict(self, params):
        import numpy as np
        mu  = np.dot(np.transpose(self.x), params)      
        return mu 
    
    ## Method for modelling the deviance
    #  @param params are beta parameters
    #  @return returns the model deviance
    def fit(self, params):
        import numpy as np
        mu  = self.predict(params)
        dev = (self.y - mu)**2
        return np.sum(dev)
    
    ## Method for calculating model performance/accuracy
    #  @return returns R-Squared               
    def diagnosis(self):
        import numpy as np
        D0 = np.sum((self.y - np.mean(self.y))**2)
        D  = self.fit(self.params)
        R2 = 1 - D/D0
        return R2

##
#  This module defines the LogisticRegression subclass that models logistic regressions
#
class LogisticRegression(LM):
    
    ## Initializes with dependent variable(endogenous) y and independent(exogenous) variables x. 
    #  Inherits from superclass LM
    #  @param x numpy array of independent/covariates x specified by user
    #  @param y numpy array of dependent variable y specified by user
    def __init__(self, x, y):
        super().__init__(x,y)
    
    ## Method for modelling estimate for mu (y_hat)
    #  @param params are beta parameters
    #  @return returns the modelled mu (y_hat)
    def predict(self, params, x):
        import numpy as np
        mu = np.exp(np.dot(np.transpose(x), params)) / ( 1 + np.exp(np.dot(np.transpose(x), params))) # added x and replaced self.x with x
        return mu
    
    ## Method for modelling the deviance
    #  @param params are beta parameters
    #  @return returns the model deviance  
    def fit(self, params):
        import numpy as np
        dev = np.log( 1 + np.exp(np.dot(np.transpose(self.x), params))) - self.y * np.dot(np.transpose(self.x), params)
        return np.sum(dev)
    
    ## Method for calculating model performance/accuracy
    #  @return returns the Area Under the ROC Curve (auc)
    def diagnosis(self):
        from sklearn.metrics import roc_auc_score
        auc = roc_auc_score(self.y, self.predict(self.params, self.x))
        return auc


