from agent.destination_agent import DestinationAgent
from agent.booking_agent import BookingAgent
from agent.explore_agent import ExploreAgent

class AgentRunner:
    def plan_trip(self, mood):
        dest_agent = DestinationAgent()
        book_agent = BookingAgent()
        explore_agent = ExploreAgent()

        destination = dest_agent.suggest_destination(mood)
        booking = book_agent.book_trip(destination)
        attractions = explore_agent.suggest_attractions(destination)
        food = explore_agent.suggest_food(destination)

        return {
            "destination": destination,
            "flights": booking["flights"],
            "hotels": booking["hotels"],
            "attractions": attractions,
            "food": food
        }