class pattern:

    @staticmethod
    def Question1(data):
        count = 0
        for i in data['player']:
            print(i['country'])
            if (i['country'] != "India"):
                count +=1

        # assertFlag = ()
        print(count)
        if (count == 4):
            print("True")
            return True
        else:
            print("False")
            return False

    @staticmethod
    def Question2(data):
        wicketkeeper = False
        for i in data['player']:
            if (i['role'] == "Wicket-keeper"):
                wicketkeeper = True

        if (wicketkeeper):
            print("True")
            return True
        else:
            print("False")
            return False






sam = pattern()

data = {"name": "Royal Challengers Bangalore", "location": "Bangalore",
            "player": [{"name": "Faf Du Plessis", "country": "South Africa", "role": "Batsman", "price-in-crores": "7"},
                       {"name": "Virat Kohli", "country": "India", "role": "Batsman", "price-in-crores": "15"},
                       {"name": "Glenn Maxwell", "country": "Australia", "role": "Batsman", "price-in-crores": "11"},
                       {"name": "Mohammad Siraj", "country": "India", "role": "Bowler", "price-in-crores": "7"},
                       {"name": "Harshal Patel", "country": "India", "role": "Bowler", "price-in-crores": "10.75"},
                       {"name": "Wanindu Hasaranga", "country": "Srilanka", "role": "Bowler",
                        "price-in-crores": "10.75"},
                       {"name": "Dinesh Karthik", "country": "India", "role": "Wicket-keeper",
                        "price-in-crores": "5.5"},
                       {"name": "Shahbaz Ahmed", "country": "India", "role": "All-Rounder", "price-in-crores": "2.4"},
                       {"name": "Rajat Patidar", "country": "India", "role": "Batsman", "price-in-crores": "0.20"},
                       {"name": "Josh Hazlewood", "country": "Australia", "role": "Bowler", "price-in-crores": "7.75"},
                       {"name": "Mahipal Lomror", "country": "India", "role": "Bowler", "price-in-crores": "7.75"}]}

print("First question", sam.Question1(data))
print("2nd  question", sam.Question2(data))

