with open("C:/питон/input.txt", 'r') as f:
    lines = f.read().splitlines()
answer = ""
nums_str = lines[0]
oper = lines[1]
sis = int(lines[2])
nums = [int(n, sis) for n in nums_str.split()]
if oper == '+':
    result = sum(nums)
elif oper == '-':
    result = nums[0]
    for n in nums[1:]:
        result -= n
elif oper == '*':
    result = 1
    for n in nums:
        result *= n
while result > 0:
    answer = str(result%sis) + answer
    result = result//sis
with open("C:/питон/output.txt", 'w') as d:
    d.write(answer)
d.close()
f.close()