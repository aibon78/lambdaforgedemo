import random
import json
from dataclasses import dataclass

@dataclass
class Input:
    pass

@dataclass
class Output:
    message: str


def lambda_handler(event, context):
    
    user_choice = event["queryStringParameters"]["user_choice"]
    
    computer_choice =random.choice(["rock","scissors","paper"])
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
    return {
        "statusCode": 200,
        "body": json.dumps({"message": result}),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }
    




