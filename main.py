import pandas as pd
import numpy as np

print("/nHello World")

print(pd.DataFrame.__doc__)

df = pd.DataFrame(np.array([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9]]),
                            columns=['a', 'b', 'c'])

df.to_csv("outputs/empty.csv", index=False)

