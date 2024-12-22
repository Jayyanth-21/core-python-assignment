class Feedback:
    def __init__(self, ratings):
        self.ratings = ratings

    def calcPositivefeed(self):
        if not self.ratings:
            print("No ratings available.")
            return

        positive_feedback_count = sum(1 for rating in self.ratings if rating == 4 or rating == 5 or rating >=3.5)
        positive_percentage = (positive_feedback_count / len(self.ratings)) * 100

        print(f"Positive Feedback: {positive_percentage:.2f}%")

ratings = [5, 4.2, 3.9, 5, 2.1, 4.5, 1.6, 5, 3.7, 3.1, 4.4, 1.8, 2.5, 3.7]

fs = Feedback(ratings)
fs.calcPositivefeed()