"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
"""

#My solution:

def likes(names):
    
    if len(names) == 0:
        x = 'no one likes this'
    elif len(names) == 1:
        x = str(names[0]) + ' likes this'
    elif len(names) == 2:
        x = str(names[0])+' and '+ str(names[1])+ ' like this'
    elif len(names) == 3:
        x = (',').join(str(x) for x in names[:2])+' and '+ names[2]+ ' like this'
    elif len(names) > 3: 
        x = (',').join(str(x) for x in names[:2]) + ' and ' + str(len(names)-2) + ' others like this' 
    print(x)

likes(['John', 'Peter', 'Tom', 'Tim'])



#Recommended Solution:
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)