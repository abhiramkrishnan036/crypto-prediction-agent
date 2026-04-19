class FeedbackAgent:

    def evaluate_prediction(self, prediction):

        print("Evaluating prediction result...")

        # Simulated actual result
        actual_result = "UP"

        if prediction == actual_result:
            result = "CORRECT"
        else:
            result = "WRONG"

        return result, actual_result