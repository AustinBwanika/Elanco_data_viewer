from .api_data import ApiData

class DataManipulator(ApiData):
    def __init__(self):
        super().__init__()
        self.money = []
        self.maps = super().costs_map()
        self.dates = super().dates_map()
        self.location = super().location_map()


    def highest_cost_(self):
        highest_cost = max(self.maps, key=lambda x: x["Cost"])
        return highest_cost

    def lowest_cost(self):
        lowest_cost = min(self.maps, key=lambda x: x["Cost"])
        return lowest_cost

    def total_cost(self):
        total = 0
        for item in self.maps:
            total += item["Cost"]

        return total

    def earliest_date(self):
        date = min(self.dates_map(), key= lambda x: x["Date"])

        return date["Date"]

    def latest_date(self):
        date = max(self.dates_map(), key= lambda x: x["Date"])
        return date["Date"]

    def location_statistics(self, locations, resource_group=None):
        location_data = self.location
        location = location_data.get(locations.lower())

        if location and resource_group:

            return location.get(resource_group.lower(), 0)
        else:

            return location or {}





