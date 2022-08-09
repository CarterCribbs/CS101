"""
Created on 9/16/21

@author: cartercribbs
"""

import random


def totem_random():
    '''
    A function that will print three random
    heads using helper function head_random()
    '''
    head_random()
    head_random()
    head_random()


def head_random():
    '''
    Helper function that randomizes the totem
    pole's hair, eyes and mouth
    '''
    hairfunc = part_hair_mohawk
    eyefunc = part_eyes_square
    mouthfunc = part_mouth_surprised
    x = random.randint(1, 4)
    if x==1:
        mouthfunc = part_mouth_smile
        hairfunc = part_hair_wavy
    elif x==2:
        eyefunc = part_eye_shadesfancy
        hairfunc = part_hair_mohawk
    elif x==3:
        eyefunc = part_eyes_eyebrows
    else:
        mouthfunc = part_mouth_frown
    head_with_three(hairfunc, eyefunc, mouthfunc)


def head_with_three(hairfunc, eyefunc, mouthfunc):
    '''
    This is a function that is called in head_random
    that prints some head parts that won't change
    and others that will be randomized
    '''
    print(hairfunc())
    print(eyefunc())
    print(part_nose_right())
    print(mouthfunc())
    print(part_chin_straight())




def totem_selfie():
    '''
    Prints a totem pole with selfie band
    By calling the selfie() helper function
    '''
    selfie(part_hair_mohawk, part_eyes_square, part_mouth_smile)
    selfie(part_hair_wavy, part_eye_shadesfancy, part_mouth_surprised)
    selfie(part_hair_sparse, part_eyes_eyebrows, part_mouth_frown)

def selfie(hairfunc, eyefunc, mouthfunc):
    '''
    selfie function that prints a head with
    functions for the hair, eyes and mouth
    '''
    print(hairfunc())
    print(selfie_band())
    print(eyefunc())
    print(part_nose_right())
    print(mouthfunc())
    print(part_chin_beard())



def selfie_band():
    '''
    prints a three line part that
    inclues my net id
    '''
    p1 = r"123456789012345678"
    p  = r" +--------------+ " + "\n"
    p += r" |cdc86    cdc86| " + "\n"
    p += r" +--------------+ "
    return p


def head_with_mouth(mouthfunc):
    """
    Prints a head with square eyes and a pointed chin
    but with a mouth specified by mouthfunc
    """
    print(part_hair_mohawk())
    print(part_eyes_square())
    print(part_nose_triangle())
    print(mouthfunc())
    print(part_chin_pointed())


def head_with_eyes(eyefunc):
    """
    Prints a head with a smiling mouth, beard chin
    and wavy hair but with eyes specified by eyefunc
    """
    print(part_hair_wavy())
    print(eyefunc())
    print(part_nose_right())
    print(part_mouth_smile())
    print(part_chin_beard())


def head_with_hair_and_chin(hairfunc, chinfunc):
    """
    Prints a head with a frowning mouth and shades
    but with hair and chin specified by hairfunc and chinfunc
    """
    print(hairfunc())
    print(part_eye_shadesfancy())
    print(part_nose_left())
    print(part_mouth_frown())
    print(chinfunc())


def totem_fixed():
    '''
    print the same totem pole with three heads,
    one cool, one angry and one crazy
    '''
    cool_head()
    angry_head()
    crazy_head()




def part_hair_mohawk():
    """
    returns a string that is one line mohawk hair
    all head parts in this program are 18 characters long
    """
    a1 = r"123456789012345678"
    a  = r" ////////\\\\\\\\ "
    return a

def part_hair_sparse():
    """
    returns a string that is one line of sparse hair
    """
    b1 = r"123456789012345678"
    b  = r"   | | | | | | |  "
    return b

def part_hair_wavy():
    """
    returns a string that is three lines of wavy hair
    """
    c1 = r"123456789012345678"
    c  = r"   / / / / / / /  " + "\n"
    c += r"   \ \ \ \ \ \ \  " + "\n"
    c += r"   / / / / / / /  "
    return c

def part_mouth_surprised():
    """
    returns an open mouth that looks surprised and is three lines tall
    """
    d1 = r"123456789012345678"
    d  = r" |   ________   | " + "\n"
    d += r" |  |        |  | " + "\n"
    d += r" |  |________|  | "
    return d

def part_mouth_smile():
    """
    returns a mouth that is smiling and is two lines tall
    """
    e1 = r"123456789012345678"
    e  = r" |  \        /  | " + "\n"
    e += r" |   \______/   | "
    return e

def part_mouth_frown():
    """
    returns a mouth that is frowning and is two lines tall
    """
    f1 = r"123456789012345678"
    f  = r" |   _._.._._   | " + "\n"
    f += r" |  /        \  | "
    return f

def part_eyes_square():
    """
    returns eyes that are square shaped and three lines tall
    """
    g1 = r"123456789012345678"
    g  = r"  ____      ____  " + "\n"
    g += r" [ o  ]    [  o ] " + "\n"
    g += r" [____]    [____] "
    return g

def part_eye_shadesfancy():
    """
    returns eyes with fancy sunglasses that is four lines tall
    """
    h1 = r"123456789012345678"
    h =  r"  _______________ " + "\n"
    h += r" |  _._    _._  | " + "\n"
    h += r" | |   |__|   | | " + "\n"
    h += r" | |_._|  |_._| | "
    return h

def part_eyes_eyebrows():
    """
    returns eyes that have eyebrows and is four lines tall
    """
    i1 = r"123456789012345678"
    i  = r"  ____       ____ " + "\n"
    i += r"  ____\     /____ " + "\n"
    i += r" /  0 \    /  0 \ " + "\n"
    i += r" \____/    \____/ "
    return i

def part_nose_left():
    """
    returns a nose that faces left and is two lines tall
    """
    j1 = r"123456789012345678"
    j  = r" |      /       | " + "\n"
    j += r" |     {__      | "
    return j

def part_nose_right():
    """
    returns a nose that faces right and is two lines tall
    """
    k1 = r"123456789012345678"
    k  = r" |       \      | " + "\n"
    k += r" |      __}     | "
    return k

def part_nose_triangle():
    """
    returns a nose in the shape of a triangle and is two lines tall
    """
    l1 = r"123456789012345678"
    l  = r" |      /\      | " + "\n"
    l += r" |     {__}     | "
    return l

def part_chin_straight():
    """
    returns a chin that is straight and is one line tall
    """
    m1 = r"123456789012345678"
    m =  r" |______________| "
    return m

def part_chin_pointed():
    """
    returns a chin that curves inward and is two lines tall
    """
    n1 = r"123456789012345678"
    n  = r" |. . . . . . . | " + "\n"
    n += r"  \____________/  "
    return n

def part_chin_beard():
    """
       returns a chin that has a beard and is two lines tall
    """
    o1 = r"123456789012345678"
    o  = r" |::::::::::::::| " + "\n"
    o += r" |______________| "
    return o

def angry_head():
    """"
    Prints a head that looks angry with sparse hair
    and a frowning mouth
    """
    print(part_hair_sparse())
    print(part_eyes_eyebrows())
    print(part_nose_right())
    print(part_mouth_frown())
    print(part_chin_pointed())

def cool_head():
    """
    prints a head that looks cool with a mohawk
    for hair and sunglasses where eyes are
    """
    print(part_hair_mohawk())
    print(part_eye_shadesfancy())
    print(part_nose_triangle())
    print(part_mouth_smile())
    print(part_chin_straight())

def crazy_head():
    """
    print a head that looks crazy with long
    wavy hair, funny eyes and a surprised mouth
    """
    print(part_hair_wavy())
    print(part_eyes_square())
    print(part_nose_left())
    print(part_mouth_surprised())
    print(part_chin_beard())

def friendly_head():
    """"
    prints a friendly looking head with a smiling
    mouth, a mohawk and a beard
    """
    print(part_hair_mohawk())
    print(part_eyes_square())
    print(part_nose_right())
    print(part_mouth_smile())
    print(part_chin_beard())



if __name__ == '__main__':


    print("\nfixed totem\n")

    totem_fixed()

    print("\nself totem\n")

    totem_selfie()

    print("\nrandom totem\n")

    totem_random()




