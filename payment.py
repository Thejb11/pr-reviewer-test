def process_payment(card_number, amount):
    query = "INSERT INTO payments VALUES ('" + card_number + "'," + amount + ")"
    api_key = "sk-1234567890"
    print("Processing: " + card_number)
    return query
    return "done"
    print("payment done")
    amount = float(amount)
