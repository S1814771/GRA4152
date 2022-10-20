
##
#  This module defines the DataSet class which examines the data and returns the correct format
#
class DataSet():
    ## Initializes with array x and array y.
    #  @param x numpy array of dependent x variables
    #  @param y numpy array of independent y variable
    #  @param transposed user input if data is already transposed (Default set to False)
    #  @param scaled user input if dependent x variables should be scaled or not (Default set to False)
    #  @return returns properly transposed data and scaled if specified
    def __init__(self, x, y, transposed = False ,scaled = False) :          # we don't use transposed as it here now any place
        import numpy as np
        if (not isinstance(x, np.ndarray) or
            not isinstance(y, np.ndarray)) :
            raise TypeError("Wrong format of x and y! Please, pass variables formatted as np.array.")
        
        question_tr = input("Is the input data transposed?: (True/False):")
        
        #
        if question_tr == "True":
            self._transposed = bool(True)
        elif question_tr == "False":
            self._transposed = bool(False)
        else:
            raise TypeError("Please, do answer True or False.")

        #
        if scaled == True:
            from sklearn.preprocessing import MinMaxScaler
            scaler = MinMaxScaler()
            
            if self._transposed == False:
                x = scaler.fit_transform(x)
            else:
                x = np.transpose(scaler.fit_transform(np.transpose(x)))

        #
        if self._transposed == False :
            self._x = np.transpose(x)
            self._y = np.transpose(y)
        elif self._transposed == True :
            self._x = x
            self._y = y
        else:
            raise TypeError("Please do answer True or False to the question.")
               
    ## Mutator method which appends a vector of 1s in the first row of x
    #  @return returns x with a new row of ones.
    def add_constant(self) :
        import numpy as np   
        self._x = np.vstack([np.array(np.repeat(1.0, self._x.shape[1]), dtype = np.float32), self._x])
    
    ## Method which splits the dataset into a train set and test set according to user inputs
    #  @param train_set defines the weight to be given to the train set. Default is set to 0.7 (70%)
    #  @param seed defines the random seed which lets the user replicate results. Default is set to 12345
    def train_test(self, train_set = 0.7, seed = 12345) :
        import numpy as np
        import random
        random.seed(seed)
        
        ## Since random cannot be implied on np.array we create index list that will be used to extract specific observations for training and test
        #
        
        index_tr = random.sample(list(range(self._x.shape[1])) , round(train_set*(self._x.shape[1])))
        index_te = np.where(np.in1d(list(range(self._x.shape[1])), index_tr, invert = True))[0]
        
        ## Split the data into test and train
        #
        self._xtr = self._x[:, index_tr]
        self._ytr = self._y[index_tr]
        self._xte = self._x[:, index_te]
        self._yte = self._y[index_te]
    
    ## Accessor method. Retrieve whole datasample for x array
    #  @return returns x (whole dataset)
    #  @property is decorator
    @property
    def x(self) :
        return self._x
    
    ## Accessor method. Retrieve whole datasample for y array
    #  @return returns y (whole dataset)
    #  @property is decorator
    @property
    def y(self) :
        return self._y
    
    ## Accessor method. Retrieves train sample for x
    #  @return returns x train set as specified to be split in method train_test
    #  @property is decorator
    @property
    def x_tr(self) :
        return self._xtr
    
    ## Accessor method. Retrieves train sample for y
    #  @return returns y train set as specified to be split in method train_test
    #  @property is decorator
    @property
    def y_tr(self) :
        return self._ytr
    
    ## Accessor method. Retrieves test sample for x
    #  @return returns x test set as specified to be split in method train_test
    #  @property is decorator
    @property
    def x_te(self) :
        return self._xte
    
    ## Accessor method. Retrieves test sample for y
    #  @return returns y test set as specified to be split in method train_test
    #  @property is decorator
    @property
    def y_te(self) :
        return self._yte


##
#  This module defines the csvDataSet subclass which lets the user read a csv file and transform it to a numpy array
#    
class csvDataSet(DataSet) :

    ## Initializes with name of csv-file 
    #  @param path name of csv-file in ""
    #  @param transposed if x-array is in transposed format (default is set to False)
    #  @param scaled if x-array should be scaled or not (default is set to False)
    #  @param header if dataset includes header or not
    #  @return dataset in correct format and scaled if specified. x and y variables 
    #  are retrieved with accessor methods in superclass (x, y, x_tr, y_tr, x_te, y_te)
    def __init__(self, path, transposed = False, scaled = False, header = None) :
        self._transposed = transposed
        import csv
        import numpy as np
        rows = []
        file = open(path)
        csvreader = csv.reader(file)
        if header == True:
            header = []
            header = next(csvreader)
        for row in csvreader:
                rows.append(row)
        self._data = np.array(rows, dtype = np.float32)
        file.close()
        
        if self._transposed == True:
            x = self._data[1:,:]
            y = self._data[0,:]
        else:
            x = self._data[:,1:]
            y = self._data[:,0]
        
        super().__init__(x, y, transposed, scaled)
        
        
