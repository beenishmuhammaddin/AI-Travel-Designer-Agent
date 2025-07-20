class ExploreAgent:
    def suggest_attractions(self, destination):
        return ["Museum", "Beach", "Local Food Tour"] if destination == "Bali" else ["Mountain Hike", "Skiing"]

    def suggest_food(self, destination):
        return ["Seafood", "Balinese Satay"] if destination == "Bali" else ["Swiss Chocolate", "Cheese Fondue"]