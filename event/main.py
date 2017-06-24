from zope.event import notify, subscribers


def on_event(evt):
    print 'Event:', evt


subscribers.append(on_event)

notify('Hello!')
# Output: Event: Hello!


class Point(object):
    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y
        notify(('moved', self))

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


class Line(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        subscribers.append(self.on_event)

    def on_event(self, evt):
        if evt[0] == 'moved':
            self.on_move(evt[1])

    def on_move(self, point):
        if (point == self.a) or (point == self.b):
            print 'moving', self

    def __str__(self):
        return '%s -- %s' % (self.a, self.b)


A = Point(0, 0)
B = Point(1, 0)
C = Point(0, 1)

AB = Line(A, B)
BC = Line(B, C)
CA = Line(C, A)

A.move(-1, -1)
