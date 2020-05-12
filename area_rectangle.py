"""
Find the area of a rectangle when provided with one diagonal and one side of the rectangle.
 If the input diagonal is less than or equal to the length of the side, return "Not a rectangle". 
 If the resultant area has decimals round it to two places.
"""
#My Solution
def area(d, l): 
    if( d <= l):
        area_rect = "Not a rectangle"
        return area_rect
    else:
        area_rect = l * ((d**2 - l**2) ** 0.5)
        area_rect = round(area_rect,2)
        return area_rect



#Recommended Solution
