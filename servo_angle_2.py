import math

def servo_angles(x):
    ab = x - 7.7
    ac = math.sqrt(ab ** 2 + 6.7 ** 2)
    cos_acb = (ac ** 2 + 6.7 ** 2 - ab ** 2) / (2 * ac * 6.7)
    acb = math.acos(cos_acb)
    cos_cab = (ac ** 2 + ab ** 2 - 6.7 ** 2) / (2 * ac * ab)
    cab = math.acos(cos_cab)
    eac = math.pi/2 - cab
    ec = math.sqrt(9 ** 2 + ac ** 2 - 2 * 9 * ac * math.cos(eac))
    cos_eca = (ec ** 2 + ac ** 2 - 9 ** 2) / (2 * ec * ac)
    eca = math.acos(cos_eca)
    cos_edc = (9.8 ** 2 + 9.8 ** 2 - ec ** 2) / (2 * 9.8 * 9.8)
    edc = math.acos(cos_edc)
    dce = math.pi/2 - (edc / 2)
    cos_aec = (9 ** 2 + ec ** 2 - ac ** 2) / (2 * 9 * ec)
    aec = math.acos(cos_aec)
    dea = aec + dce
    dcb = dce + eca + acb

    s1 = math.degrees(dcb) - 90
    s2 = math.degrees(edc) - 40
    s3 = math.degrees(dea)
    
    return s1, s2, s3