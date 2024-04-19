# External
import fastf1
from dotenv import dotenv_values
from fastapi.security import HTTPBearer
from fastf1.ergast import Ergast


__version__ = "0.6.0"


# Load environment variables from .env file
config = dotenv_values(".env")
# FastF1 configuration
fastf1.set_log_level("WARNING")
fastf1.Cache.set_disabled()
# Ergast configuration
ergast = Ergast(result_type="raw", auto_cast=True)
# Cors Middleware
origins = [config["FRONTEND_URL"], "http://127.0.0.1:3000"]
# Others
favicon_path = "favicon.ico"
# Security
security = HTTPBearer()
