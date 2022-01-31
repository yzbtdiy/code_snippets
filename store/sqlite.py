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

	
//使用当前日期作为数据库名称
def save_to_sqlite(file_name, question_id, qq_number, user_content):
    tab_name = str(datetime.date.today().__format__("%Y%m%d"))
    create_tab = (
        "CREATE TABLE IF NOT EXISTS '%s'(QUES_ID int, QQ_NUM int, USER_CON text)"
        % (tab_name)
    )
    add_data = (
        "INSERT INTO '%s'(QUES_ID, QQ_NUM, USER_CON) VALUES (%s ,%d, '%s')"
        % (
            tab_name,
            question_id,
            qq_number,
            user_content,
        )
    )
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(create_tab)
        db_con.execute(add_data)
