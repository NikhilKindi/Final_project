import train


def test_triangle_0():
    assert train.triangle(0, 0, 0) == 'Equilateral triangle'
    assert train.triangle(1, 0, 0) == 'Isosceles triangle'
    assert train.triangle(2, 0, 1) == 'Scalene triangle'
