import math
def transfer_r_theta(x, y):
    r_pixal = math.sqrt((x - 659) ** 2 + (y - 590) ** 2)
    r_real = 7 * r_pixal / 16
    cos_theta = (590 - y) / r_pixal
    theta = math.acos(cos_theta)
    theta_degree = math.degrees(theta)
    return r_real/10, theta_degree

print (transfer_r_theta(338, 225))