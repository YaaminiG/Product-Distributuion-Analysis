import pandas as pd
df = pd.read_csv(Historical Product Demand.csv")
import matplotlib.pyplot as plt
import seaborn as sns



distinct_count = df['Product_Code'].nunique()
print(f"Number of distinct product codes: {distinct_count}")

distinct_codes = df['Product_Code'].unique()
print("Distinct product codes:", distinct_codes)

print(df.info())

df=pd.DataFrame(df)
print(df.isnull().any().sum(), ' / ', len(df.columns))
print(df.isnull().any(axis=1).sum(),'/', len(df))

df.dropna(axis=0, inplace=True) #Remove all the rows with null values
df.reset_index(drop=True)
df.sort_values('Date')[1:20]

df['Date'] = pd.to_datetime(df['Date'])




# Filter for the specific product code
product_code = "Product_0031"

filtered_data = df[df['Product_Code'] == product_code]

# Resample by year-end and sum the Order_Demand
monthly_order_demand = filtered_data.groupby(pd.Grouper(key='Date', freq='W'))['Order_Demand'].sum().reset_index()
monthly_order_demand.set_index('Date', inplace=True)

# Check the grouped data
print(monthly_order_demand)

monthly_order_demand

# Replace zeros in the Order_Demand column with the mean value
mean_value = 17942  # Provided mean value
monthly_order_demand['Order_Demand'] = monthly_order_demand['Order_Demand'].replace(0, mean_value)
# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(monthly_order_demand.index, monthly_order_demand['Order_Demand'], marker='o', linestyle='-')


# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Total Order Demand')
plt.title(f'Monthly Total Order Demand from 2012 to 2016 for {product_code}')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
import pandas as pd
import matplotlib.pyplot as plt 
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.ar_model import AutoReg
import pandas as pd

# Define the series from your dataset
series = monthly_order_demand['Order_Demand']

# Split the data into training (70%) and testing (30%) sets
train_size = int(len(series) * 0.7)
historic = series.iloc[:train_size]  # In-sample / training data
test = series.iloc[train_size:]      # Out-of-sample / testing data

# Initialize variables for the cross-validation loop
historic_list = historic.to_list()   # Convert training set to a list to allow appending
predictions = []

# Cross-validation loop: one-step-ahead prediction for each point in the test set
for i in range(len(test)):
    # Fit an AR(1) model on the current historic data
    model_fit = AutoReg(historic_list, lags=1).fit()
    
    # Predict the next value (one-step-ahead prediction)
    pred = model_fit.predict(start=len(historic_list), end=len(historic_list), dynamic=False)
    predictions.append(pred[0])  # Store prediction
    
    # Append the actual observed test value to historic data for the next iteration
    historic_list.append(test.iloc[i])

# Convert predictions to a Pandas Series with the same index as the test set
cross_val_predictions = pd.Series(predictions, index=test.index)

# Plotting the results
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(series.index, series, label='Observed', marker='o', linestyle='-', color='blue')
plt.plot(test.index, cross_val_predictions, label='Cross-Validation Predictions', marker='o', linestyle='--', color='red')
plt.xlabel('Date')
plt.ylabel('Total Order Demand')
plt.title('Cross-Validation')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
from sklearn import metrics 
cross_val_predictions = pd.Series(predictions, index=test.index)

# Define y_true and y_pred for evaluation
y_true = test
y_pred = cross_val_predictions

# Calculate and print error metrics
print("Mean Absolute Error (MAE):", metrics.mean_absolute_error(y_true, y_pred))
print("Mean Squared Error (MSE):", metrics.mean_squared_error(y_true, y_pred))
print("Root Mean Squared Error (RMSE):", metrics.mean_squared_error(y_true, y_pred, squared=False))
print("Mean Absolute Percentage Error (MAPE):", metrics.mean_absolute_percentage_error(y_true, y_pred))

from statsmodels.tsa.ar_model import AutoReg, ar_select_order 
historic = series
 #prediction for the next 52 weeks (1 year)
n_pred = 52
date_pred = pd.date_range("2017-01-08", periods=n_pred, freq="W-SUN")
sel = ar_select_order(historic, 13, glob = True, seasonal = True,
old_names=False)
sel.ar_lags
model_fit = sel.model.fit()
pred = model_fit.predict(start=len(historic), end=len(historic) +n_pred- 1, dynamic=False)
predictions = pd.Series(pred.values, index=date_pred)
 # plot results
plt.plot(series, label='Observed')
plt.plot(cross_val_predictions, color='magenta', label='Cross Validation')
plt.plot(predictions, color='red', label='Predicted')

plt.legend(fontsize = 15)
plt.show()
