class Student:
    def __init__(self):
        self.std_data = {}

    def inpStd(self):
        try:
            n = int(input("Enter the number of students: "))
            for i in range(1, n + 1):
                name = input(f"Enter the name of student {i}: ")
                scores = input(f"Enter scores for {name} (comma-separated): ")
                scores = list(map(float, scores.split(',')))
                self.std_data[name] = scores
                print(f"Scores for {name} have been recorded.")
        except ValueError:
            print("Invalid input.... Please enter numbers only for scores and count")

    def calcAvg(self):
        # Create a new dictionary to store student scores and averages
        self.std_avg = {}
        if not self.std_data:
            print("No student data available to calculate averages")
            return
        for name, scores in self.std_data.items():
            average = sum(scores) / len(scores) if scores else 0
            self.std_avg[name] = {"Scores": scores, "Average": average}

    def topPerformer(self):
        if not self.std_data:
            print("No student data available to identify the top performer.")
            return
        top_student = None
        top_average = 0
        for name, details in self.std_avg.items():
            average = details["Average"]
            if average > top_average:
                top_average = average
                top_student = name
        if top_student:
            print(f"\nTop Performer: {top_student} with an average score of {top_average:.2f}")
        else:
            print("\nNo valid student data to identify the top performer")

    def data(self):
        self.inpStd()
        self.calcAvg()
        self.topPerformer()
        print("\nFinal Student Data with Scores and Averages:")
        print(self.std_avg)

obj = Student()
obj.data()
