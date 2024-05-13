# %% imports and prep 
import math

def camera_b_distance(f, g):
    return (f*g)/(g-f)

# %% Exercise 1

a = 10
b = 3
print(math.degrees(math.atan2(b, a)))
# %% Exercise 2

print(f"0.1 meters: {camera_b_distance(0.015, 0.1)}")
print(f"1 meter: {camera_b_distance(0.015, 1)}")
print(f"5 meter: {camera_b_distance(0.015, 5)}")
print(f"15 meter: {camera_b_distance(0.015, 15)}")

# %% Exercise 3
# everything is in mm

thomas_height = 1800
object_dist = 5000
focal_length = 5
ccd_height = 4.8
ccd_width = 6.4
ccd_diagonal = 8.0
ccd_res_x = 640
ccd_res_y = 480


# 1
# Gauss lens equation
# distance from lens when taking picture of thomas
b = camera_b_distance(focal_length, object_dist)
print(f"1. ccd should be {b} mm from lens")

# 2
# b/B = g/G
# size of thomas on ccd in mm
thomas_on_ccd = ((thomas_height/object_dist)*b)
print(f"2. thomas is {thomas_on_ccd} mm tall on ccd")

# 3
# resolution relative to physical ccd size
ccd_pixel_in_mm = ccd_width / ccd_res_x
print(f"3. a pixel on ccd is {ccd_pixel_in_mm}x{ccd_pixel_in_mm} mm")

# 4
# Height of thomas on ccd
# height on ccd divide by pixels size in mm on ccd
thomas_pixel_height = thomas_on_ccd / ccd_pixel_in_mm
print(f"4. thomas is {thomas_pixel_height} pixels tall on ccd")

# 5
# angle between side of sensor to middle from lens intersection times 2

horizontal_fov = math.degrees(math.atan2((ccd_width / 2),focal_length))*2
print(f"5. horizontal fov is: {horizontal_fov} degrees")

# 6
# angle between top of sensor to middle from lens intersection times 2

vertical_fov = math.degrees(math.atan2((ccd_height / 2),focal_length))*2
print(f"6. vertical fov is: {vertical_fov} degrees")