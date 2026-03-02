# BMI mapping >25 overweight etc. O(1)
def solve(bmi: float) -> str:
    if bmi < 18.5: return "Under"
    if bmi < 25: return "Norm"
    return "Over"\n