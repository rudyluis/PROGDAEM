# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

df = pd.read_csv("/kaggle/input/supermarket-sales/supermarket_sales - Sheet1.csv")
df.head()

df.info()

import matplotlib.pyplot as plt
import seaborn as sns
import warnings 

warnings.filterwarnings("ignore")

fig, axes = plt.subplots(2, 3, figsize=(16, 12))

cols = df[["Branch", "City", "Customer type", "Gender", "Product line", "Payment"]]

for i, column in enumerate(cols):
    row = i // 3
    col = i % 3
    sns.histplot(x=cols[column], ax=axes[row, col])
    axes[row, col].set_xticklabels(axes[row, col].get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()




max_prices = df.groupby("Product line")["Unit price"].max().reset_index()
min_prices = df.groupby("Product line")["Unit price"].min().reset_index()

product_min_max = pd.concat([max_prices, min_prices["Unit price"]], axis=1, join='inner')
product_min_max.columns =["Product line","Max Price","Min Price"]

product_min_max

total_sales = df.groupby("Product line")["Total"].sum().reset_index()
sns.barplot(x=total_sales["Product line"],y=total_sales["Total"])
plt.xticks(rotation=45)

total_quan = df.groupby("Product line")["Quantity"].sum().reset_index()
sns.barplot(x=total_quan["Product line"],y=total_quan["Quantity"])
plt.xticks(rotation=45)

max_cost =  df.loc[df.groupby(["Product line"])["cogs"].idxmax()]
min_cost = df.loc[df.groupby(["Product line"])["cogs"].idxmin()]

max_cost = max_cost.rename(columns={"cogs":"Max Cost"})
min_cost = min_cost.rename(columns={"cogs":"Min Cost"})

mean_cost= df.groupby(["Product line"])["cogs"].mean()/df.groupby(["Product line"])["Quantity"].mean()
mean_cost = pd.DataFrame(mean_cost,columns=["Mean Cost"])

min_max_cost = max_cost.merge(min_cost["Min Cost"],on=max_cost["Product line"],how="left")
min_max_cost = min_max_cost[["Product line","Max Cost","Quantity","Min Cost"]]
min_max_cost["Max Cost"] =min_max_cost["Max Cost"]/min_max_cost["Quantity"]

min_max_cost = min_max_cost.merge(mean_cost["Mean Cost"],on=mean_cost.index,how="left")

min_max_cost.drop(["Quantity","key_0"],axis=1,inplace=True)
min_max_cost

total_cost = df.groupby("Product line")["cogs"].sum().reset_index()
sns.barplot(x=total_cost["Product line"],y=total_cost["cogs"])
plt.xticks(rotation=45)

ratings = df.groupby("Product line")["Rating"].agg(["max","min","mean"])
ratings.rename(columns={"max":"Max Rating","min": "Min Rating","mean" : "Mean Rating"},inplace=True)
ratings

sns.histplot(x=df["Payment"],hue=df["Customer type"],multiple="dodge")

round(df["gross margin percentage"].describe().astype("float64"),6)

income = df.groupby("Product line")["gross income"].agg(["sum","max","min","mean"]).reset_index()
income

sns.barplot(x=income["Product line"],y=income["sum"])
plt.xticks(rotation=45)

print(f"Dataset is in Dates between :{df['Date'].min()} and {df['Date'].max()}")

df.head()

df_filtered = df.copy()
df_filtered = df_filtered.drop(["Invoice ID","Quantity","gross margin percentage","cogs","Time"],axis=1)

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)

ohe_cols = ["Branch","City","Payment","Product line","Gender"]

encoded = encoder.fit_transform(df_filtered[ohe_cols])

encoded = pd.DataFrame(encoded,columns=encoder.get_feature_names_out(ohe_cols))


df_filtered = pd.concat([df_filtered.drop(ohe_cols,axis=1),encoded],axis=1)

from sklearn.preprocessing import LabelEncoder

encoder_ = LabelEncoder()

df_filtered["Customer type"] = encoder_.fit_transform(df["Customer type"])


import datetime as dt

df_filtered["Date"] = pd.to_datetime(df_filtered["Date"])

df_filtered["Year"] = df_filtered["Date"].dt.year.astype("int64")
df_filtered["Month"] = df_filtered["Date"].dt.month.astype("int64")
df_filtered["Day"] = df_filtered["Date"].dt.day.astype("int64")
df_filtered.drop("Date",axis=1,inplace=True)

df_filtered.info()

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

x = df_filtered.drop("Total",axis=1)
y = df_filtered["Total"]

x_scaler = StandardScaler()
y_scaler = StandardScaler()

x_scaled = x_scaler.fit_transform(x)

y_scaler.fit(np.array(y).reshape(-1,1))
y_scaled = y_scaler.transform(np.array(y).reshape(-1,1))

x_train,x_test,y_train,y_test = train_test_split(x_scaled,y_scaled,test_size=0.3,random_state=42)


from catboost import CatBoostRegressor

catboost = CatBoostRegressor(iterations=1000, depth=6, learning_rate=0.05, loss_function='RMSE', random_seed=42,verbose=0)

catboost.fit(x_train,y_train)

y_pred_cat  = catboost.predict(x_test)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

print(f"MSE : {mean_squared_error(y_test,y_pred_cat)}")
print(f"R2 Score : {r2_score(y_test,y_pred_cat)}")

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(catboost, x_scaled, y_scaled, cv=5, scoring='neg_mean_squared_error')
print(f"Cross Val Score : {cv_scores * -1}")
print(f"Cross Val Score Mean: {cv_scores.mean() * -1}")
print(f"Cross Val Score Std: {cv_scores.std()}")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits

train_sizes, train_scores, test_scores = learning_curve(
    CatBoostRegressor(), x_scaled, y_scaled, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10)
)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training")
plt.ylabel("Score")
plt.grid()

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1, color="r")

plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")


plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1, color="g")

plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

plt.legend(loc="best")
plt.show()


residuals = y_test - y_pred_cat

plt.scatter(x=y_pred_cat, y=y_pred_cat)
plt.hlines(y=0, xmin=min(y_pred_cat), xmax=max(y_pred_cat), colors='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.1)

lasso.fit(x_train,y_train)


y_pred_lasso = lasso.predict(x_test)

print(f"MSE : {mean_squared_error(y_test,y_pred_lasso)}")
print(f"R2 Score : {r2_score(y_test,y_pred_lasso)}")

cv_scores = cross_val_score(lasso, x_scaled, y_scaled, cv=5, scoring='neg_mean_squared_error')
print(f"Cross Val Score : {cv_scores * -1}")
print(f"Cross Val Score Mean: {cv_scores.mean() * -1}")
print(f"Cross Val Score Std: {cv_scores.std()}")

train_sizes, train_scores, test_scores = learning_curve(
    Lasso(), x_scaled, y_scaled, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10)
)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training")
plt.ylabel("Score")
plt.grid()

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1, color="r")

plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")


plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1, color="g")

plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

plt.legend(loc="best")
plt.show()

residuals = y_test.flatten() - y_pred_lasso

plt.scatter(x=y_pred_lasso, y=residuals)
plt.hlines(y=0, xmin=min(y_pred_lasso), xmax=max(y_pred_lasso), colors='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(x_train,y_train)


y_pred_ridge = ridge.predict(x_test)


print(f"MSE : {mean_squared_error(y_test,y_pred_ridge)}")
print(f"R2 Score : {r2_score(y_test,y_pred_ridge)}")

cv_scores = cross_val_score(ridge, x_scaled, y_scaled, cv=5, scoring='neg_mean_squared_error')
print(f"Cross Val Score : {cv_scores * -1}")
print(f"Cross Val Score Mean: {cv_scores.mean() * -1}")
print(f"Cross Val Score Std: {cv_scores.std()}")

train_sizes, train_scores, test_scores = learning_curve(
    Ridge(), x_scaled, y_scaled, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10)
)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training")
plt.ylabel("Score")
plt.grid()

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1, color="r")

plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")


plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1, color="g")

plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

plt.legend(loc="best")
plt.show()

residuals = y_test - y_pred_ridge

plt.scatter(x=y_pred_ridge, y=residuals)
plt.hlines(y=0, xmin=min(y_pred_ridge), xmax=max(y_pred_ridge), colors='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

from sklearn.linear_model import ElasticNet
elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_net.fit(x_train, y_train)




y_pred_enet = elastic_net.predict(x_test)

print(f"MSE : {mean_squared_error(y_test,y_pred_enet)}")
print(f"R2 Score : {r2_score(y_test,y_pred_enet)}")

cv_scores = cross_val_score(elastic_net, x_scaled, y_scaled, cv=5, scoring='neg_mean_squared_error')
print(f"Cross Val Score : {cv_scores * -1}")
print(f"Cross Val Score Mean: {cv_scores.mean() * -1}")
print(f"Cross Val Score Std: {cv_scores.std()}")

train_sizes, train_scores, test_scores = learning_curve(
    Ridge(), x_scaled, y_scaled, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10)
)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure()
plt.title("Learning Curve")
plt.xlabel("Training")
plt.ylabel("Score")
plt.grid()

plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1, color="r")

plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")


plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1, color="g")

plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")

plt.legend(loc="best")
plt.show()

residuals = y_test.flatten() - y_pred_enet

plt.scatter(x=y_pred_enet, y=residuals)
plt.hlines(y=0, xmin=min(y_pred_enet), xmax=max(y_pred_enet), colors='red')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()