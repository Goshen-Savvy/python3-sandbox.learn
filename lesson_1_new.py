#Checks if a value exist in a list
class Find:
    def search(data):
        data = [4, 5, 10]
        num = int(input('Enter number '))
        for n in data:
            if num == 5:
                print("lucky number")
                break
            else:
                print("Try again")
                break

f = Find()
f.search()