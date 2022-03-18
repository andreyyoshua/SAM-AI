class Bbox:
    def __init__(self, x1, y1, x2, y2, label):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.label = label
        self.box = [self.x1, self.y1, self.x2, self.y2]
        self.width = abs(self.x2 - self.x1 + 1)
        self.height = abs(self.y2 - self.y1 + 1)

    @property
    def area(self):
        """
        Calculates the surface area. useful for IOU!
        """
        return self.width * self.height

    def intersect(self, bbox):
        x1 = max(self.x1, bbox.x1)
        y1 = max(self.y1, bbox.y1)
        x2 = min(self.x2, bbox.x2)
        y2 = min(self.y2, bbox.y2)
        if x2 < x1 or y2 < y1:
            return 0.0

        return (x2 - x1 + 1) * (y2 - y1 + 1)

    def intersecting_over_50_percent(self, bbox):
        intersection = self.intersect(bbox)

        percentage = intersection / float(self.area)
        return percentage >= 0.5