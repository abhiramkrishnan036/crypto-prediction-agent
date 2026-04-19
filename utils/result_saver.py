def save_results(prediction, actual, accuracy):

    with open("results.txt", "a") as file:

        file.write("Prediction: " + prediction + "\n")
        file.write("Actual: " + actual + "\n")
        file.write("Accuracy: " + accuracy + "\n")
        file.write("----------------------\n")