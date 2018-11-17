total_price = int(input("合計金額を教えてね(円):"))
print(total_price)

amount = int(input("人数をおしえてね(人):"))
print(amount)

print("一人あたり:" + str(total_price // amount) + "円,端数:" + str(total_price % amount) + "円")
