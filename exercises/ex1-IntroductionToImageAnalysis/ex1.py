from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom
# %% 
# Directory containing data and images
in_dir = "data/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)

print(f"image resolution: {im_org.shape[0]} by {im_org.shape[1]}")

print(f"image is stored in {im_org.dtype}")

picMin = np.amin(im_org)
picMax = np.amax(im_org)

print(f"min pixel value found: {picMin}")
print(f"max pixel value found: {picMax}")

# io.imshow(im_org, vmin = picMin, vmax = picMax)
# h = plt.hist(im_org.ravel(), bins = picMax - picMin)
# plt.title('Metacarpal image')
# io.show()
print(f"The pixel value at (110, 90) is {im_org[110, 90]}")

# %% 
in_dir = "data/"

im_name = "metacarpals.png"

im_org = io.imread(in_dir + im_name)

mask = im_org > 150
im_org[mask] = 255
io.imshow(im_org)
io.show()

# %%
in_dir = "data/"

im_name = "ardeche.jpg"

im_org = io.imread(in_dir + im_name)

green = [0, 255, 0]
im_org[:im_org.shape[0] // 2] = green

io.imshow(im_org)
io.show()

# %%
in_dir = "data/"
im_name = "ardeche.jpg"
im_org = io.imread(in_dir + im_name)

print(f"dimensions are {im_org.shape[1]} by {im_org.shape[0]}")
im_rescaled = rescale(im_org, 0.25, anti_aliasing = True, channel_axis = 2)
# Calculating a scaling factor allows for maintaining the 
# aspect ratio with a desired width/height
scaling_factor = 400 / im_org.shape[1]

im_resized = resize(im_org, (int(im_org.shape[0] * scaling_factor), int(im_org.shape[1] * scaling_factor)), anti_aliasing = True)

print(f"im_rescaled is now type {im_rescaled.dtype}")
print(f"pixel value of (100, 100): {im_org[100, 100]}")
print(f"pixel value of (100, 100): {im_rescaled[100, 100]}")
print(f"rescaled floats after multiplying by 256: {im_rescaled[100, 100]}")

im_gray = color.rgb2gray(im_org)
im_byte = img_as_ubyte(im_gray)

io.imshow(im_gray)
io.show()

# %%
in_dir = "data/"
im_name = "ardeche.jpg"
im_org = io.imread(in_dir + im_name)

im_gray = color.rgb2gray(im_org)
im_byte = img_as_ubyte(im_gray)

h = plt.hist(im_byte.ravel(), bins = 256)
plt.title('ardeche.jpg pixel values')
io.show()

# %%
in_dir = "data/"
im_name = "skull.jpg"
im_org = io.imread(in_dir + im_name)

im_resized = resize(im_org, (im_org.shape[0] // 8, im_org.shape[1] // 8), anti_aliasing=True)
im_gray = color.rgb2gray(im_resized)
im_byte = img_as_ubyte(im_gray)
print(f"dtype of im_byte: {im_byte.dtype}")

h = plt.hist(im_byte.ravel(), bins = 256)
print(f"left edge of 2: {h[1][180]}")
print(f"right edge of 2: {h[1][181]}")
plt.title('skull.jpg gray values')
io.show()

# %%
in_dir = "data/"
im_name = "DTUSign1.jpg"
im_org = io.imread(in_dir + im_name)

# Only the intensity of the Red channel is being shown
r_comp = im_org[:, :, 0]
io.imshow(im_org)
io.show()
io.imshow(r_comp, cmap = "nipy_spectral")
plt.title('DTU sign image (Red)')
io.show()

# %%
in_dir = "data/"
im_name = "DTUSign1.jpg"
im_org = io.imread(in_dir + im_name)

im_org[500:1000, 800:1500, :] = [0, 0, 255]
io.imshow(im_org)
io.show()
io.imsave(fname = "test.png", arr=im_org)

# %%
in_dir = "data/"
im_name = "metacarpals.png"
im_org = io.imread(in_dir + im_name)
print(f"type of metacarpals is: {im_org.dtype}")
im_rgb = color.gray2rgb(im_org)

# pixel mask where bones are targeted to be colored blue

mask = im_org > 125
im_rgb[mask] = [0, 0, 255]


io.imshow(im_rgb)
io.show()

# %%
in_dir = "data/"
im_name = "metacarpals.png"
im_org = io.imread(in_dir + im_name)

p = profile_line(im_org, (342, 77), (320, 160))
plt.plot(p)
plt.ylabel('Intensity')
plt.xlabel('Distance along line')
plt.show()
io.imshow(im_org)
io.show()

# %%
in_dir = "data/"
im_name = "1-442.dcm"
ds = dicom.dcmread(in_dir + im_name)
im = ds.pixel_array
print(f"{im.dtype}")
print(f"{im.shape[0]}")
io.imshow(im, vmin=-200, vmax=400, cmap="jet")
io.show()