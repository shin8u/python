class Quad:
    def __init__(self):
        self.points = [[-3, -3], [-3, 3], [3, 3], [3, -3]]

    def move(self, x, y):
        for point in self.points:
            point[0] += x
            point[1] += y

    def show_position(self):
        return self.points


class Pentagon:
    def __init__(self):
        self.points = [[4, 1], [2, 0], [5, 5], [6, 4], [5, 1]]

    def move(self, x, y):
        for point in self.points:
            point[0] += x
            point[1] += y
        return 0

    def show_position(self):
        return self.points


def is_intersect(q, p):
    temp = False

    x1 = q.points[0][0]
    y1 = q.points[0][1]
    y2 = q.points[1][1]
    x2 = q.points[3][0]

    for pPoint in p.points:
        if x1 <= pPoint[0] <= x2 \
        and y1 <= pPoint[1] <= y2:
            return True

    x1 = p.points[0][0]
    y1 = p.points[0][1]
    x2 = p.points[1][0]
    y2 = p.points[1][1]
    x3 = p.points[2][0]
    y3 = p.points[2][1]
    x4 = p.points[3][0]
    y4 = p.points[3][1]
    x5 = p.points[4][0]
    y5 = p.points[4][1]

    for qp in q.points:
        if (x2 - x1) * (qp[1] - y1) - (y2 - y1) * (qp[0] - x1) >= 0 \
        and (x1 - x5) * (qp[1] - y5) - (y1 - y5) * (qp[0] - x5) >= 0 \
        and (x5 - x4) * (qp[1] - y4) - (y5 - y4) * (qp[0] - x4) >= 0 \
        and (x4 - x3) * (qp[1] - y3) - (y4 - y3) * (qp[0] - x3) >= 0 \
        and (x3 - x2) * (qp[1] - y2) - (y3 - y2) * (qp[0] - x2) >= 0:
            return True

    return False


if __name__ == '__main__':
    q1 = Quad()
    p1 = Pentagon()

    print(q1.show_position())
    print(p1.show_position())

    print(is_intersect(q1, p1))

    q1.move(9, 7)
    p1.move(9, 7)

    print(q1.show_position())
    print(p1.show_position())
