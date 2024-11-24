import numpy as np
import pandas as pd

def built_in_package_demo():
    # NumPy: Create an array and perform basic operations
    array = np.array([12, 34, 56, 89, 67])
    print("Numpy Array : ", array)
    print("Squared Array : ", array**2)
    print()
    # Pandas: Create a DataFrame and display its information
    data = {'Name' : ["Alice","Bob","charlie"], 'age':[12, 34, 23], 'score' : [78, 90, 89]}
    df = pd.DataFrame(data)
    print(df)

built_in_package_demo()
print()

# User defind package and mypackage folder contains other packages
from mypackage.userpackage_practical14 import add
print(f"Addition : {add(2, 3)}")

from mypackage.userpackage1_practical14 import rectangle
print(f"Rectangle : {rectangle(4, 6)}")