from math import floor
def nb_year(p0, percent, aug, p):
    years = 0 
    while p0 < p and p0 != p:
            p0 = floor(p0) + floor((p0 * (percent / 100)) + aug)
            years += 1     
    return years
