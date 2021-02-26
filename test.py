from OTXv2 import OTXv2
import IndicatorTypes
import os, json, requests, psycopg2, time
from psycopg2 import pool
from datetime import datetime
from pytz import timezone
from tqdm import tqdm
from config import config
from termcolor import cprint

otx = OTXv2('d208825926256517b037657addb90894cf4b663c8ba9651a67d44493334a94a4')
dbs = otx.getall(limit=1, max_page=1)

print(dbs)
