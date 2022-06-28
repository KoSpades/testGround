import duckdb
con = duckdb.connect("DuckDB/test.db")

print(con.execute("SELECT * FROM new_tbl").fetchall())

