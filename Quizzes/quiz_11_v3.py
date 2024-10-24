"""
Solution for implementation of a Circle type. 

Author: Carlos Seminario, Laura Hiatt

Programmer/Collaborator: David Zhang
"""

from math import pi
from math import sqrt

class Circle:
    """ Represents a Circle in two-dimensional space as (r, a, b).
    
    The Circle object represents a circle of radius r in two dimensional space. 
    This class allows the Circle to be manipulated and analyzed through various
    methods.
    
    Attributes:
        r: radius of the circle
        a: The x-coordinate of the center of the circle in space
        b: The y-coordinate of the center of the circle in space
    """
    def __init__(self, r, a = 0.0, b = 0.0): ## Modify this line to implement default parameters!
        
        """ Creates a Circle object.
         
        Using the given coordinates, constructs a Circle object with those
        r, a and b values.
        
        Parameters:
            radius: radius (as a float)
            a: x-coordinate (as a float), a Constructor default parameter
            b: y-coordinate (as a float), a Constructor default parameter
        """        
        ## Do NOT change the names of these instance attributes!!!
        self.radius = float(r)
        self.x_coord = float(a)
        self.y_coord = float(b)
        
    def __str__(self):
        """ Returns a string representation of Circle's characteristics.
        
        The string representation of self Circle object is returned in the
        form "This is a circle of radius x centered at x-y coordinates (x, y)".
        
        Returns:
            The Circle object in a string representation of self Circle's 
            characteristics.
        """
        
        return "This is a circle of radius %.1f centered at x-y coordinates \
(%.1f, %.1f)" % (self.radius, self.x_coord, self.y_coord)
        
    
    def __eq__(self, other):
        """ Returns the equality of two Circle objects.
        
        Determines if two Circle objects are the same based on whether or not
        both circles have the same radius and x and y coordinates.
        
        Parameters:
            other: another Circle object to compare with self Circle
                      
        Returns:
            True if both Circles have same radius and x and y coordinates
            False if both Circles do NOT same radius and x and y coordinates
        """         
        if (self.radius == other.radius and self.x_coord == other.x_coord and
            self.y_coord == other.y_coord):
            return True
        else:
            return False
        
               
    def area(self):
        """ Calculates a Circle object's area.
        
        The Circle object's area is computed using the formula,
        area = pi * r**2
        
        Parameters:
            None.
        
        Returns:
            Circle object's area (as a float)
        """    
        area = pi * (self.radius ** 2)
        return float('%.3f' % area)
        
        
    def circumference(self):
        """ Calculates a Circle object's circumference.
        
        The Circle object's circumference is computed using the formula,
        circumference = 2 * pi * r
        
        Parameters:
            None.
        
        Returns:
            Circle object's circumference (as a float)
        """    
        circum = 2 * pi * self.radius
        return float('%.3f' % circum)
        
    
    def translate(self, dx, dy):
        """ Shifts a Circle object's coordinates.
        
        The Circle object's coordinates are shifted by the specified amounts 
        in the x and y directions.
        
        Parameters:
            dx: the change in x
            dy: the change in y
        
        Returns:
            None.
        """
        self.x_coord += dx
        self.y_coord += dy
        
    def distance(self, other):
        """ Returns the distance between the centers of two Circle objects.
        
        Determines the Euclidean distance between self Circle and other Circle
        using the formula ((x1 − x2)**2 + (y1 − y2)**2)**(1/2) for two points
        (x1, y1) and (x2, y2).
        
        Parameters:
            other: the Circle object from which to determine self Circle's
                   distance.
                      
        Returns:
            The Euclidean distance between the centers of self Circle and 
            other Circle.
        """        
        dist = ((self.x_coord - other.x_coord)**2 + (self.y_coord
                                                     - other.y_coord)**2)**(1/2)
        return dist
        
        
    def quadrant(self):
        """ Returns the quadrant of the x-y plane in which self Circle object
            is centered.
                
        A Circle lies in 
        quadrant 1 if the x and y coordinates are both positive, 
        quadrant 2 if the x coordinate is negative and the y coordinate is positive,
        quadrant 3 if the x and y coordinates are both negatiave, and 
        quadrant 4 if the x coordinate is positive and the y coordinate is negative. 
        If the Circle lies directly on the x and/or y axis, the quadrant is 
        represented as 0.
            
        Returns:
            The quadrant of self Circle object's center as an integer.
        """        
        if self.x_coord > 0 and self.y_coord > 0:
            return 1
        if self.x_coord < 0 and self.y_coord > 0:
            return 2
        if self.x_coord < 0 and self.y_coord < 0:
            return 3
        if self.x_coord > 0 and self.y_coord < 0:
            return 4
        else:
            return 0
    
    def center_collision(self, other):
        """ 
        Determines whether or not the other circle object's center is contained 
        within (has "collided" with) the self circle object and returns a boolean 
        value.

        Parameters:
            other circle object.
        
        Returns: 
        True: When the other circle's center is inside (and not on) the 
              circumference of the self circle.
        False: When the other circle's center is NOT contained inside 
               the self circle.
        
        """
        ##
        ## Feel free to use (or not) these design ideas ..
        ##
        #
        # 1. Determine whether the other center is contained within self circle ..
        
        ## << place your code here >> 
        
        ##else:
            #
            # 2. Given that the other circle's center is not within self circle,
            # the other circle has not collided with self circle.
            ## << place your code here >>
        dist = ((self.x_coord - other.x_coord)**2 + (self.y_coord
                                                     - other.y_coord)**2)**(1/2)
        if dist > self.radius:
            #When the radius of the self circle is smaller than the distance
            #between the two circles, then True
            return False
        else:
            return True
        

    def contained(self, other):
        """ 
        Determines whether or not the other circle object is totally contained 
        within self circle object and returns a boolean value.
        
        Parameters:
            other circle object.
        
        Returns: 
        True: When the other circle is totally contained within self circle.
        False: When the other circle is NOT totally contained within self circle.
        
        """
        ##
        ## Feel free to use (or not) these design ideas ..
        ##
        # 1. Determine whether the other circle is contained within self circle ..
        
        ## << place your code here >>
        ##else:
            #
            # 2. Given that the other circle is not contained within self circle,
            # the other circle is not totally contained in self circle.
            ## << place your code here >>
        dist = ((self.x_coord - other.x_coord)**2 + (self.y_coord
                                                     - other.y_coord)**2)**(1/2)
        if self.radius - other.radius < dist:
            #When the difference between the radius of two circles is smaller
            #than the distance between the two centers, then the other circle
            #is not contained in the self circle
            return False
        else:
            return True
        

    def shares_one_point(self, other):
        """ 
        Determines whether or not the other circle object shares *one* point on the
        circumference with the self circle object and returns a boolean value, i.e.,  
        whether the circles are *touching* each other or not, at only one point. 
        This can occur only when the other circle object is TOTALLY contained 
        within this self circle or when the other circle is outside, but adjacent 
        to, this self circle.        
        
        Note: When the other and self circles are defined identically, this
        method should return False because all points on the circumference are 
        shared.
        
        Parameters:
            other circle object.
            
        Returns:
        True: if the other circle's circumference shares one point with 
              (is touching) self circle's circumference.
        False: if the other circle's circumference does NOT share any point with 
              (is touching) self circle's circumference.
        
        """
        ##
        ## Feel free to use (or not) these design ideas ..
        ##
        # 1. Determine whether the other center is contained within self circle ..
        
        ## << place your code here >>
        
            #
            # 2. Given that the center of other is within self circle, determine
            # whether the other circle is contained within self circle. 
            
            ## << place your code here >>
            
                # 3. Given that the other circle is totally contained within
                # self circle, determine whether the circles have a common point
                # at the circumference, i.e., the circles are "touching".
                
                ## << place your code here >>

            # 4. Given that the other center is not contained in self circle,
            # determine whether the circles have a common point at the 
            # circumference, i.e., the circles are "touching".
            #
            ## << place your code here >>
        dist = ((self.x_coord - other.x_coord)**2 + (self.y_coord
                                                     - other.y_coord)**2)**(1/2)
        if self.radius + other.radius == dist:
            #If the sum of the radius of the two circles is the same as the
            #distance between the two circles, then they share one point.
            return True
        else:
            return False


def main():
    """ Tester function. """
    
    ## Move the triple quotes down as you develop your code 
    ## so you can use these test cases..
    
        
    
    # Instantiate a circle
    c1 = Circle(3)
    print ()
    
    # Test _str_()
    print (c1)
    # should print: 
    # This is a circle of radius 3.0 centered at x-y coordinates (0.0, 0.0)
    print ()
    
    # Test _eq_()
    c1 = Circle (3.5, 3, 4)
    c2 = Circle (3.5, 3, 4)
    c3 = Circle (5.0)
    print (c1 == c2)        # should print .. True
    print (c1 == c3)        # should print .. False
    print ()
    
    # Test area()
    c1 = Circle (3.5, 4.5, 5.5)
    print (c1.area())       # should print .. 38.484
    print ()
    
    # Test circumference()
    c1 = Circle (2.5, 3.5, 4.5)
    print (c1.circumference())  # should print .. 15.708
    print ()    
    
    
    # Test translate()
    c1 = Circle (2.5)
    print (c1) 
    # should print: 
    # This is a circle of radius 2.5 centered at x-y coordinates (0.0, 0.0)    
    c1.translate (2, 5)
    print (c1) 
    # should print: 
    # This is a circle of radius 2.5 centered at x-y coordinates (2.0, 5.0)
    c1.translate(-1, 3)
    print (c1) 
    # should print: 
    # This is a circle of radius 2.5 centered at x-y coordinates (1.0, 8.0)    
    print ()
    
    # Test distance()
    c1 = Circle (3.0, 3, 5)
    c2 = Circle (5.0, 6, 9)
    dist = c1.distance(c2)
    print (dist) # should print: 5.0
    print ()
    
    # Test quadrant()
    c1 = Circle (4.5, 1, 1)
    print (c1.quadrant()) # should print: 1
    c1.translate(-2.0, 0)
    print (c1.quadrant()) # should print: 2
    c1.translate(0, -2.0)
    print (c1.quadrant()) # should print: 3
    c1.translate(2.0, 0)
    print (c1.quadrant()) # should print: 4
    c1.translate(0, 1.0)
    print (c1.quadrant()) # should print: 0    
    print ()
    
    # Test with 6 circles of varying radii and x-y coordinates 
    #c1 = Circle (1, 4, 4)
    #c2 = Circle (1, 2, 2)
    #c3 = Circle (4, 4, 2)
    #c4 = Circle (2, 3, 3)
    #c5 = Circle (1, 2, 0)
    #c6 = Circle (1, 4, -1)    
    
    # Test collisions with two identical circles
    print('Test with two identical circles')
    c1 = Circle (5)
    c2 = Circle (5)
    print (c1.center_collision(c2)) # True
    print (c2.center_collision(c1)) # True
    print (c1.contained(c2))        # True
    print (c2.contained(c1))        # True
    print (c1.shares_one_point(c2)) # False
    print (c2.shares_one_point(c1)) # False
    print()
    
    # Test center-collision
    print('Test collision')
    c1 = Circle (1, 4, 4)
    c2 = Circle (1, 2, 2)
    print (c1.center_collision(c2)) # False (b/c c2 center NOT within c1)
    c3 = Circle (4, 4, 2)
    print (c3.center_collision(c1)) # True (b/c c1 center within c3)
    print ()
    
    # Test contained
    print('Test contained')
    c4 = Circle (2, 3, 3)
    c6 = Circle (1, 4, -1)
    print (c4.contained(c6)) # False (b/c c6 NOT contained within c4)
    c3 = Circle (4, 4, 2)
    print (c3.contained(c6)) # True  (b/c c6 contained within c3)
    print ()  
    
    # Test shares_one_point
    print('Test shares_one_point')
    c1 = Circle (1, 4, 4)
    c2 = Circle (1, 2, 2)
    print (c1.shares_one_point(c2)) # False
    c5 = Circle (1, 2, 0)
    print (c5.shares_one_point(c2)) # True (b/c c5,c2 circumferences are touching) 
    print()   
    
    
if __name__ == "__main__":
    main()