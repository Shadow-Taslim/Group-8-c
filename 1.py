import math

def double_slit_maxima(wavelength_nm, angle_deg, slit_distance_um):
    
    MIN_WAVELENGTH = 380
    MAX_WAVELENGTH = 750

    
    if wavelength_nm < MIN_WAVELENGTH or wavelength_nm > MAX_WAVELENGTH:
        return "Out of the range. Please enter a valid number."

    
    wavelength_m = wavelength_nm * 1e-9
    
    slit_distance_m = slit_distance_um * 1e-6

    
    angle_rad = math.radians(angle_deg)

    
    m = (slit_distance_m * math.sin(angle_rad)) / wavelength_m
    order = round(m)

    return f"{order}-th order maxima"


try:
    wavelength_nm = float(input("Enter the wavelength (in nm): "))
    angle_deg = float(input("Enter the angle (in degrees): "))
    slit_distance_um = float(input("Enter the distance between slits (in micrometers): "))

    result = double_slit_maxima(wavelength_nm, angle_deg, slit_distance_um)
    print(result)
except ValueError:
    print("Invalid input. Please enter a numerical values.")