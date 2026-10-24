score = 82
documents = True
attendance = 90
fee = True
probability = 0.81

print("case: pass_all")
print("input: score =", score, "documents =", documents, "attendance =", attendance, "fee =", fee, "probability =", probability)
print("expected: Review")

if score >= 70 and documents and attendance >= 75 and fee:
    print("actual: Review")
else:
    print("actual: Hold")

if probability >= 0.70:
    print("threshold: Review")
else:
    print("threshold: Hold")

print("reason: All conditions satisfied")
print("")

score = 85
documents = True
attendance = 60
fee = True
probability = 0.85

print("case: fail_attendance")
print("input: score =", score, "documents =", documents, "attendance =", attendance, "fee =", fee, "probability =", probability)
print("expected: Hold")

if score >= 70 and documents and attendance >= 75 and fee:
    print("actual: Review")
else:
    print("actual: Hold")

if probability >= 0.70:
    print("threshold: Review")
else:
    print("threshold: Hold")

print("reason: Attendance below 75 (new condition 1 fails)")
print("")

score = 88
documents = True
attendance = 92
fee = False
probability = 0.88

print("case: fail_fee")
print("input: score =", score, "documents =", documents, "attendance =", attendance, "fee =", fee, "probability =", probability)
print("expected: Hold")

if score >= 70 and documents and attendance >= 75 and fee:
    print("actual: Review")
else:
    print("actual: Hold")

if probability >= 0.70:
    print("threshold: Review")
else:
    print("threshold: Hold")

print("reason: Fee not cleared (new condition 2 fails)")
print("")

score = 70
documents = True
attendance = 80
fee = True
probability = 0.70

print("case: boundary_score")
print("input: score =", score, "documents =", documents, "attendance =", attendance, "fee =", fee, "probability =", probability)
print("expected: Review")

if score >= 70 and documents and attendance >= 75 and fee:
    print("actual: Review")
else:
    print("actual: Hold")

if probability >= 0.70:
    print("threshold: Review")
else:
    print("threshold: Hold")

print("reason: Score exactly 70, boundary case passes")
