import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

try:
    logging.debug("Taking input from user")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    logging.debug("Calculating division")
    result = a / b

    print("Result =", result)
    logging.info("Division completed successfully")

except ValueError:
    print("Please enter numbers only.")
    logging.error("Invalid input entered by user", exc_info=True)

except ZeroDivisionError:
    print("Cannot divide by zero.")
    logging.error("Division by zero occurred", exc_info=True)

except Exception as e:
    print("An unexpected error occurred.")
    logging.exception("Unexpected error")

finally:
    logging.info("Program execution completed")