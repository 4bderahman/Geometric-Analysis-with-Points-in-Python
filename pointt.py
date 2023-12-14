import math

class Point:
    nb = 0

    def __init__(self, abs, ord):
        self._abs = abs
        self._ord = ord
        Point.nb += 1

    @property
    def abs(self):
        return self._abs

    @abs.setter
    def abs(self, new_abs):
        self._abs = new_abs

    @property
    def ord(self):
        return self._ord

    @ord.setter
    def ord(self, new_ord):
        self._ord = new_ord

    def __str__(self):
        return f"({self._abs}, {self._ord})"

    def __eq__(self, other):
        return self._abs == other._abs and self._ord == other._ord

    def calculerdistance(self, p):
        return ((self._abs - p._abs) ** 2 + (self._ord - p._ord) ** 2) ** 0.5

    def calculermilieu(self, p):
        x_milieu = (self._abs + p._abs) / 2
        y_milieu = (self._ord + p._ord) / 2
        return Point(x_milieu, y_milieu)

class TroisPoints:
    def __init__(self, point1, point2, point3):
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3

    @property
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, new_point1):
        self._point1 = new_point1

    @property
    def point2(self):
        return self._point2

    @point2.setter
    def point2(self, new_point2):
        self._point2 = new_point2

    @property
    def point3(self):
        return self._point3

    @point3.setter
    def point3(self, new_point3):
        self._point3 = new_point3

    def sontalignes(self):
        d1 = self._point1.calculerdistance(self._point2)
        d2 = self._point2.calculerdistance(self._point3)
        d3 = self._point3.calculerdistance(self._point1)
        return math.isclose(d1 + d2, d3, abs_tol=1e-9) or math.isclose(d2 + d3, d1, abs_tol=1e-9) or math.isclose(d3 + d1, d2, abs_tol=1e-9)

    def estisocèle(self):
        d1 = self._point1.calculerdistance(self._point2)
        d2 = self._point2.calculerdistance(self._point3)
        d3 = self._point3.calculerdistance(self._point1)
        return d1 == d2 or d2 == d3 or d3 == d1


# Create some Point instances
point1 = Point(0, 0)
point2 = Point(4, 0)
point3 = Point(2, 3)

# Create an instance of TroisPoints with these points
trois_points = TroisPoints(point1, point2, point3)

# Test for alignment
print(f"Les points sont-ils alignés? {trois_points.sontalignes()}")

# Test for isosceles triangle
print(f"Les points forment-ils un triangle isocèle? {trois_points.estisocèle()}")

# Test for acute-angled triangle


# Additional tests can be added as needed to verify all functionalities
