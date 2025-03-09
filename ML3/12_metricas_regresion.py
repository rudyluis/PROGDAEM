from sklearn.metrics import max_error
## Error absoluto máximo (M)
y_verdadero = [1, 2, 3, 4, 5]
y_predicho = [1, 2, 3, 4, -5]
print(max_error(y_verdadero, y_predicho))



from sklearn.metrics import mean_absolute_error
##Error absoluto medio (mean absolute error - MAE)
y_verdadero = [1, 2, 3, 4, 5]
y_predicho = [1, 2, 3, 4, -5]
print(mean_absolute_error(y_verdadero, y_predicho))

from sklearn.metrics import mean_squared_error

##Error cuadrático medio (mean squared error - MSE)

y_verdadero = [1, 2, 3, 4, 5]
y_predicho = [1, 2, 3, 4, -5]
print(mean_squared_error(y_verdadero, y_predicho))
      

##Raíz cuadrada del error cuadrático medio (RMSE)
from sklearn.metrics import root_mean_squared_error

y_verdadero = [1, 2, 3, 4, 5]
y_predicho = [1, 2, 3, 4, -5]
print(root_mean_squared_error(y_verdadero, y_predicho))

##R^2 (Coeficiente de determinación)
from sklearn.metrics import r2_score

y_verdadero = [1, 2, 3, 4, 5]
y_predicho = [1, 2, 3, 4, 2]
print(r2_score(y_verdadero, y_predicho))
