import pandas as pd
import numpy as np

print("/nHello You")

print(pd.DataFrame.__doc__)

# created a simple DataFrame to test functionality
df = pd.DataFrame(np.array([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9]]),
                            columns=['a', 'b', 'c'])

# stored DataFrame in a local csv file
df.to_csv("outputs/empty.csv", index=False)

