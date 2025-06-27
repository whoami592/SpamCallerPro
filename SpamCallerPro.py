#!/usr/bin/python3
"""
SpamCallerPro - A Python script to simulate spam calls
"""

import random
import time
import sys

def spam_caller():
    """Simulate spam calls"""
    
    # List of common scam numbers
    scam_numbers = [
        "1-800-555-1234",
        "1-800-555-5678",
        "1-800-555-9012",
        "1-800-555-3456",
        "1-800-555-7890"
    ]
    
    # List of common scam messages
    scam_messages = [
        "Your account has been compromised!",
        "You have won a prize!",
        "Your payment has failed!",
        "Your credit card has expired!",
        "Your package is delayed!"
    ]
    
    # Simulate spam calls
    for _ in range(10):  # Make 10 spam calls
        # Randomly select a scam number and message
        number = random.choice(scam_numbers)
        message = random.choice(scam_messages)
        
        # Print the simulated call
        print(f"Calling {number}...")
        time.sleep(1)  # Simulate call duration
        
        # Print the scam message
        print(f"{message}")
        time.sleep(1)  # Wait before next call
        
    print("Spam call simulation completed!")

if __name__ == "__main__":
    spam_caller()