def save_to_sqlite(file_name, id, content):
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(
        """
            CREATE TABLE IF NOT EXISTS user_info(
	        USER_ID int,
	        USER_CON text
        )
        """
        )
        sql = "INSERT INTO user_info(USER_ID, USER_CON) VALUES (%d, %s)" % (id, content)
        db_con.execute(sql)