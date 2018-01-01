from datetime import datetime as dt


class CustomDateBuilder:
    def suffix(self, d):
        return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

    def custom_strftime(self, format, t):
        return t.strftime(format).replace('{S}', str(t.day) + self.suffix(t.day))

    def build_date(self):
        return self.custom_strftime('{S} %B %Y', dt.now())
