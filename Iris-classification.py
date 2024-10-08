import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('iris.data.csv')
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

def classify_iris():
    try:
        sepal_length = float(entry_sepal_length.get())
        sepal_width = float(entry_sepal_width.get())
        petal_length = float(entry_petal_length.get())
        petal_width = float(entry_petal_width.get())

        user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = knn.predict(user_input)
        species = le.inverse_transform(prediction)[0]

        messagebox.showinfo("Result", f'The predicted species is: {species}')
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numerical values")

root = tk.Tk()
root.title("Iris Flower Classification")

tk.Label(root, text="Sepal Length (cm):").grid(row=0, column=0)
entry_sepal_length = tk.Entry(root)
entry_sepal_length.grid(row=0, column=1)

tk.Label(root, text="Sepal Width (cm):").grid(row=1, column=0)
entry_sepal_width = tk.Entry(root)
entry_sepal_width.grid(row=1, column=1)

tk.Label(root, text="Petal Length (cm):").grid(row=2, column=0)
entry_petal_length = tk.Entry(root)
entry_petal_length.grid(row=2, column=1)

tk.Label(root, text="Petal Width (cm):").grid(row=3, column=0)
entry_petal_width = tk.Entry(root)
entry_petal_width.grid(row=3, column=1)

classify_button = tk.Button(root, text="Classify", command=classify_iris)
classify_button.grid(row=4, columnspan=2)

root.mainloop()
