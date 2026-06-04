import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("expense.csv")

print("Expense Data:")
print(data)

total=data["Amount"].sum()

print("\nTotal Expense:")
print(total)

category_total=data.groupby("Category")["Amount"].sum()

print("\nCategory-wise Expense:")
print(category_total)


#pie chart
category_total.plot(
    kind="pie",
    autopct="%1.2f%%"
)
plt.title("Expense Distribution")
plt.ylabel("")
plt.show()