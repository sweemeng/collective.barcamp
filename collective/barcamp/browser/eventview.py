from Products.Five.browser import BrowserView

class BarcampEventView(BrowserView):
    pass

class BarcampSessionView(BrowserView):
    pass


class BarcampAttendanceView(BrowserView):
    def get_attendee(self):
        return self.context.registrations.items()


class BarcampFNBView(BrowserView):
    def get_attendee(self):
        return self.context.registrations.items()


class BarcampHotelView(BrowserView):
    def get_attendee(self):
        return self.context.registrations.items()


class BarcampTourView(BrowserView):
    def get_attendee(self):
        return self.context.registrations.items()

