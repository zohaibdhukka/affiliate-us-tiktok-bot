import os
from dotenv import load_dotenv
from logs import logger
from libs.bot import Bot

load_dotenv()
CHROME_FOLDER = os.getenv("CHROME_FOLDER")
CATEGORY = os.getenv("CATEGORY")
FOLLOWERS = os.getenv("FOLLOWERS")
CONTENT_TYPE = os.getenv("CONTENT_TYPE")
CREATOR_AGENCY = os.getenv("CREATOR_AGENCY")

if __name__ == '__main__':
    logger.info("Starting bot...")
    bot = Bot(
        CHROME_FOLDER
    )
    
    # Login validation
    is_logged = bot.login()
    if not is_logged:
        logger.error("Error: Login failed")
        quit()
        
    bot.filter_creators(
        CATEGORY,
        FOLLOWERS,
        CONTENT_TYPE,
        CREATOR_AGENCY
    )
    
    print("done")