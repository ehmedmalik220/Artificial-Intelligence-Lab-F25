class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        if target == self.previous_mode:
            send = False
        else:
            send = True
        self.previous_mode = target
        return target, send


print("--- Part 1: reflex agent, manual sequence ---")
agent = ClassroomAgent()
percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
expected = ["COOL", "COOL", "IDLE", "IDLE", "WARM", "ECO"]

step = 1
for temp, occupied in percepts:
    mode = agent.act(temp, occupied)
    want = expected[step - 1]
    print(step, (temp, occupied), "target mode", mode, "expected", want, "match", mode == want)
    step = step + 1

print("--- Part 2: stateful agent, Task 3 trace ---")
stateful = StatefulClassroomAgent()
trace = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False), (29, False)]

for temp, occupied in trace:
    previous = stateful.previous_mode
    target, send = stateful.act(temp, occupied)
    if send:
        command = "send command"
    else:
        command = "no command"
    print("previous", previous, "percept", (temp, occupied), "target", target, command)

print("--- Part 3: checks ---")
print("reflex vs stateful on the manual sequence:")
reflex_agent = ClassroomAgent()
reflex_modes = []
for temp, occupied in percepts:
    reflex_modes.append(reflex_agent.act(temp, occupied))
print("reflex modes:", reflex_modes)
print("reflex commands sent:", len(percepts))

check_agent = StatefulClassroomAgent()
stateful_commands = 0
for temp, occupied in percepts:
    target, send = check_agent.act(temp, occupied)
    print((temp, occupied), "target", target, "send", send)
    if send:
        stateful_commands = stateful_commands + 1
print("stateful commands sent:", stateful_commands)

print("noisy sequence around 26 degrees:")
noisy = [(25, True), (27, True), (25, True), (27, True)]
noisy_agent = StatefulClassroomAgent()
noisy_commands = 0
for temp, occupied in noisy:
    target, send = noisy_agent.act(temp, occupied)
    print((temp, occupied), "target", target, "send", send)
    if send:
        noisy_commands = noisy_commands + 1
print("noisy commands sent:", noisy_commands, "out of 4")
print("note: memory does not stop switching when the target keeps changing")

print("boundary checks:")
print("20 degrees occupied:", reflex_agent.act(20, True), "expected IDLE")
print("26 degrees occupied:", reflex_agent.act(26, True), "expected IDLE")
print("empty room priority check:")
print("29 degrees empty:", reflex_agent.act(29, False), "expected ECO")
