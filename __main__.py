import os
from dotenv import load_dotenv
from logs import logger
from libs.bot import Bot

load_dotenv ()
VAR = os.getenv ("VAR")

if __name__ == '__main__':
    logger.info("Starting bot...")
    chrome_folder = 'C:\\Users\\herna\\AppData\\Local\\Google\\Chrome\\User Data'
    bot = Bot(
        chrome_folder
    )
    
    # Login validation
    is_logged = bot.login()
    if not is_logged:
        logger.error("Error: Login failed")
        quit()
        
    bot.filter_creators()
    
    print("done")