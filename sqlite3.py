import sqlite3

from sqlalchemy import create_engine
engine = create_engine("sqlite:///testDb.db")

query = engine.execute("""SELECT * FROM Taha;""")

con = sqlite3.connect("/Users/TCAKIR/testDb.db")

cur = con.cursor()

cur.execute("""SELECT * FROM Reality""")


"""
CREATE TABLE Taha (
	column_1 data_type PRIMARY KEY,
   	column_2 data_type NOT NULL,
	column_3 data_type DEFAULT 0,
	table_constraints
) ;
"""