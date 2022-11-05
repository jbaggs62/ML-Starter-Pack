# Importing libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import mean_squared_error, r2_score  
  
X, Y = load_diabetes(return_X_y=True)  
X = X[:,8].reshape(-1,1)  
  
#train and train split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 0.4, random_state = 10 )  

linReg = LinearRegression()  

# Training 
linReg.fit( X_train, Y_train )  

#Predictions 
Y_pred = linReg.predict( X_test )  
print("Value of the coefficients: \n", linReg.coef_)  
  
# Get MSE
print(f"MSE: {mean_squared_error( Y_test, Y_pred)}")  
  
# Get R-Squared
print(f"R-Square: {r2_score( Y_test, Y_pred )}")  
  
# Plotting the output  
plt.scatter(X_test, Y_test, color = "black", label = "original data")  
plt.plot(X_test, Y_pred, color = "blue", linewidth=3, label = "regression line")  
plt.xlabel("Independent Varaiables")  
plt.ylabel("Dependent Variables")  
plt.title("Simple Linear Regression")  
plt.savefig("Linear_Regression.png")
