def dupeChecker(list):
    seen = set()
    for num in list:
        if num in seen:
            return True
        seen.add(num)
    return False

print(dupeChecker([1,2,3,1]))
print(dupeChecker([1,2,3,4]))