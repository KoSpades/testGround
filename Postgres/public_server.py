import psycopg2
import psycopg2.extras


def main():
    conn_string = "host='hh-pgsql-public.ebi.ac.uk' dbname='pfmegrnargs' user='reader' password='NWDMCE5xdipIjRrp'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # retrieve a list of RNAcentral databases
    query = "SELECT * FROM rnc_database"

    cursor.execute(query)
    res = []
    for row in cursor:
        res.append(row)
    print(res)


if __name__ == "__main__":
    main()
