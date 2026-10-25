
def check(marks, docs, attend, fee_paid):
    if marks >= 70 and docs and attend >= 75 and fee_paid:
        return "Review"
    return "Hold"

tests = [
    ("pass_all", 82, True, 90, True, "Review"),
    ("fail_attendance", 85, True, 60, True, "Hold"),
    ("fail_fee", 88, True, 92, False, "Hold"),
    ("boundary_score", 70, True, 80, True, "Review"),
]

for name, marks, docs, attend, fee_paid, want in tests:
    got = check(marks, docs, attend, fee_paid)
    print(name, "->", got, "(expected:", want + ")")

