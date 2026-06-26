from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

if __name__ == "__main__":
  logging.info("the execution has started")
  
  try:
    a = 1/0
  except Exception as e:
    logging.info("Custome Exception")
    raise CustomException(e)