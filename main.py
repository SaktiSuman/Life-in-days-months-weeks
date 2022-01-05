age = input("What is your current age?")

age = int(age)
w = int(90 * 52 - age * 52)
m = int(90 * 12 - age * 12)
d = int(90 * 365 - age * 365)
print(f"You have {d} days, {w} weeks, and {m} months left.")