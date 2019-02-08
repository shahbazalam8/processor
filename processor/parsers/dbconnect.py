import pprint
import pandas as pd
import xmldataset
from sqlalchemy.dialects import mysql
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine
import sqlalchemy
# import MySQLdb

class DbConnect():
    # def __init__(self):
    #     df_output = self.df_output
    def dbengine1(self, dataf, dbtype, dbuser, dbpasswd,server):
        dburi = str(dbtype + "://" + dbuser + ":" + dbpasswd + "@" + server + "/mysql")
        print(dburi)
        # engine = create_engine(dburi)
        engine = mysql.connector.connect(dburi)
        with engine.connect() as conn, conn.begin():
            dataf.to_sql('symdev_test', conn, if_exists='append', index=False)