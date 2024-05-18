import math

def calculate_slit_ratio(angle_deg):
    
    angle_rad = math.radians(angle_deg)

    
    sin_theta = math.sin(angle_rad)


    ratio = 1 / sin_theta

    return ratio


angle_deg = 45


slit_to_wavelength_ratio = calculate_slit_ratio(angle_deg)
print(f"The ratio of the slit width to the wavelength is: {slit_to_wavelength_ratio:.2f}")