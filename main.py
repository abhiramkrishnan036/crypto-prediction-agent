from utils.logger import setup_logger
from utils.result_saver import save_results

import logging

from agents.search_agent import SearchAgent
from agents.data_fetch_agent import DataFetchAgent
from agents.prediction_agent import PredictionAgent
from agents.risk_agent import RiskAgent
from agents.feedback_agent import FeedbackAgent


def main():

    # -----------------------------------
    # Initialize Logger
    # -----------------------------------
    setup_logger()
    logging.info("Application started")

    print("Crypto Prediction Agent Started")

    try:

        # -----------------------------------
        # Search Agent
        # -----------------------------------
        search_agent = SearchAgent()
        prices = search_agent.get_crypto_prices()

        logging.info("Fetched crypto prices")

        print("Current Crypto Prices:")
        print(prices)

        # -----------------------------------
        # Data Fetch Agent
        # -----------------------------------
        data_agent = DataFetchAgent()
        historical_data = data_agent.get_historical_data()

        logging.info("Fetched historical data")

        print("Number of historical records:")
        print(len(historical_data))

        # -----------------------------------
        # Prediction Agent
        # -----------------------------------
        prediction_agent = PredictionAgent()
        prediction = prediction_agent.predict_next_move(historical_data)

        logging.info(f"Prediction generated: {prediction}")

        print("Prediction for next move:")
        print(prediction)

        # -----------------------------------
        # Risk Management Agent
        # -----------------------------------
        risk_agent = RiskAgent()

        probability = 0.6
        odds = 2

        risk = risk_agent.calculate_risk(probability, odds)

        logging.info(f"Risk calculated: {risk}")

        print("Recommended risk fraction:")
        print(risk)

        # -----------------------------------
        # Feedback Agent
        # -----------------------------------
        feedback_agent = FeedbackAgent()

        result, actual = feedback_agent.evaluate_prediction(prediction)

        logging.info(f"Actual result: {actual}")
        logging.info(f"Prediction accuracy: {result}")

        print("Actual result:")
        print(actual)

        print("Prediction accuracy:")
        print(result)

        # -----------------------------------
        # Save Results to File
        # -----------------------------------
        save_results(prediction, actual, result)

        logging.info("Results saved to file")

    except Exception as error:

        logging.error(f"An error occurred: {error}")
        print("Error occurred:", error)


if __name__ == "__main__":
    main()