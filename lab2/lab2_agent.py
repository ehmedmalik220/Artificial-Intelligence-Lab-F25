

class RoomAgent:
    def decide(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"

class SmartAgent(RoomAgent):
    def __init__(self):
        self.last = None

    def run(self, temp, occupied):
        mode = self.decide(temp, occupied)
        send = mode != self.last
        self.last = mode
        return mode, send

print("Reflex:")
agent = RoomAgent()
for temp, occupied in [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]:
    print((temp, occupied), "->", agent.decide(temp, occupied))

print("\nStateful:")
smart = SmartAgent()
for temp, occupied in [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False), (29, False)]:
    mode, send = smart.run(temp, occupied)
    print((temp, occupied), "->", mode, "| send:", send)

print("\nNoisy around 26:")
noisy = SmartAgent()
for temp, occupied in [(25, True), (27, True), (25, True), (27, True)]:
    mode, send = noisy.run(temp, occupied)
    print((temp, occupied), "->", mode, "| send:", send)

