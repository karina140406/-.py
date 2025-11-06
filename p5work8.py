card = "5468350018455833"
card_num = len(card)-4
result = "*" * card_num + card[card_num:]
print(result)