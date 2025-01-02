#!/usr/bin/env python
import sys
from crew import ZillowscraperCrew
import agentops
from agentops.enums import EndState
import os

session = agentops.init(api_key=os.getenv('AGENTOPS_API_KEY'), default_tags=['crewai', 'agentstack'])


def run():
    """
    Run the crew.
    """
    inputs = {
        "url": "https://www.zillow.com/apartments/austin-tx/the-hamilton/5XhsyY/"  # Replace with the Zillow URL you want to scrape
    }
    ZillowscraperCrew().crew().kickoff(inputs=inputs)
    session.end_session(EndState.SUCCESS)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
    }
    try:
        ZillowscraperCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ZillowscraperCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
    }
    try:
        ZillowscraperCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


if __name__ == '__main__':
    run()