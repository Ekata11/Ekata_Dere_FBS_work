
dev_any_digit=[x for x in range(1,1001)if any(x%d==0 for d in range(2,10))]
print(dev_any_digit)