class DestinationAgent:
    def suggest_destination(self, mood):
        if mood == "relax":
            return "Bali"
        elif mood == "adventure":
            return "Swiss Alps"
        else:
            return "Istanbul"