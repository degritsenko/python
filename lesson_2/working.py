goods = []
while input("add producr: "):
    number = int(input("Enter product number: ")):
    features = {}
    while input("Would you like add product parameters? : "):
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))