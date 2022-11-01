import pandas as pd
import sqlite3, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, text, inspect
from IPython.display import Markdown, display

engine=create_engine('sqlite:///FIFA23_Player.db',echo=True)
meta=MetaData()
df_Fifa23_Player = pd.read_csv('data/FIFA 23 Player.csv')

df_Fifa23_Player.to_sql("FIFA23_Player", engine)
