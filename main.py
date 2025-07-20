from agent_runner import AgentRunner

if __name__ == "__main__":
    mood = input("What's your travel mood? (relax/adventure/romantic): ")
    runner = AgentRunner()
    plan = runner.plan_trip(mood)

    print("\n📍 Destination:", plan["destination"])
    print("✈️ Flights:", plan["flights"])
    print("🏨 Hotels:", plan["hotels"])
    print("🎢 Attractions:", plan["attractions"])
    print("🍽️ Food Recommendations:", plan["food"])