import newrelic.agent  # isort:skip


# Built-in
import os


if os.getenv("ENVIRONMENT") != "TEST":
    newrelic.agent.initialize("newrelic.ini")

# External
import fastf1
from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app = FastAPI(
    title="Slick Telemetry API",
    description="Slick Telemetry backend written in python with fastf1. 🏎",
    version=__version__,
    contact={
        "name": "Slick Telemetry",
        "url": "https://github.com/Slick-Telemetry",
        "email": "contact@slicktelemetry.com",
    },
    license_info={
        "name": "GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    redoc_url=None,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # HTTPSRedirectMiddleware # TODO use for production and staging
)
