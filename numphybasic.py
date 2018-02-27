#This is very simple example Illustration 

#import statements 

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Constants

#Generate item Sizes between(1000,5000)
num_init = 100
np.random.seed(50)
item_size = np.random.randint(low=1000,high=5000,size=num_init)

#Generate House Prices with random noise added

np.random.seed(50)
item_price = item_size * 100.0 + np.random.randint(low=10000,high=50000,size=num_init)

#plot data using Matplot with item size and item price

plt.plot(item_size,item_price,"rx") #bx = blue x
plt.xlabel("Item Size")
plt.ylabel("Item Price")
plt.show()




