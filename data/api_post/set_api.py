from metric.main_metric import *
from api.data import *
from menu.main_menu import *
from search.scan import *
import os
import time
from datetime import date

from fastapi import FastAPI

app = FastAPI()

# --- post metode --- #

@api
