import numpy as np
from PIL import Image

data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255,255,0]
data[0:4] = [255,0,0]
print(data)

img = Image.fromarray(data,'RGB')
img.save('canvas.png')