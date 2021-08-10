import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)
console_handler.setFormatter(logging.Formatter('%(name)s : %(message)s'))

logger.info("Eine Info Nachricht")
logger.debug("Eine Debug Nachricht")
