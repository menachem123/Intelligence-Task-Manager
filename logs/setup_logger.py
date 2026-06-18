import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s | %(levelname)s | %(message)s ", filename="logs/app.log")
logger = logging.getLogger(__name__)