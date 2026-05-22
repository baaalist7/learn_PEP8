class userData:
    def __init__(self, name, age):
        self.user_name = name
        self.age = age

    def printInfo(self):
        print(f"user:{self.user_name}, age: {self.age}")


def process_data(dataList):
    result = []
    for d in dataList:
        if d.age > 18:
            result.append(d.user_Name.upper())
    return result