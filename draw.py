import math
import sys 
import pygame
from pygame import gfxdraw
from pygame import Color

def prime_number_set(max_value):
    """This function computes the set of prime numbers that are smaller
    than or equal to max_value.

    """
    int_list = range(2, max_value + 1)
    primes = set(int_list)

    for n in int_list:
        if n in primes:
            i = 2 * n
            while i <= max_value:
                if i in primes:
                    primes.remove(i)
                i += n
    return primes

def compute_number_to_circle_point(x, y, point_number, radius):
    """This function compute a dictonary which associates to each number
    its coordinates on the circle.

    """
    angle = (2 * math.pi) / point_number
    return {i : (int(x + radius * math.sin(i * angle)), \
                 int(y + radius * math.cos(i * angle))) for i in range(point_number)}

def compute_lines(points, prime_numbers):
    """For each point x of the circle, this function computes (x *
    multiplier) mod len(points) and add the coordinates of the source
    and of the destination of the segment to the result list.

    """
    n = len(points)
    res = []
    for source in points:
        for prime in [p for p in prime_numbers if source < p < 2 * source and p < n]:
            destination = prime % point_number
            res.append((points[source], points[destination]))
    return res

def draw_lines(window, x, y, radius, lines):
    """This function uses gfxdraw to draw the initial circle in white and
    the previously computed lines in red.

    """
    gfxdraw.circle(window, x, y, radius, Color(255, 255, 255,255))
    for p1, p2 in lines:
        gfxdraw.line(window, p1[0], p1[1], p2[0], p2[1], Color(255, 0, 0,255))

if __name__ == '__main__':
    # number of points on the circle.
    point_number = int(sys.argv[1])
    # radius of the circle.
    radius = int(sys.argv[2])
    # multiplication table that we draw.
    pygame.init()

    prime_numbers = list(prime_number_set(2 * point_number))
    prime_numbers.sort()

    # The size of the window is (2 * radius + 40, 2 * radius + 40) so
    # the center of the screen is (radius + 20, radius + 20)
    window = pygame.display.set_mode((2 * radius + 40, 2 * radius + 40))
    x_center = y_center = radius + 20

    # We compute the coordinates of the points on the circle, the
    # lines between the points and then we draw these lines.
    points = compute_number_to_circle_point(x_center, y_center,
                                            point_number, radius)
    lines = compute_lines(points, prime_numbers)
    draw_lines(window, x_center, y_center, radius, lines)
    pygame.display.flip()

    # We save the picture.
    pygame.image.save(window, 'render.png')

    # The window stays open until it is closed manually by the user.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

