from sqlite3 import connect

user = input('Nazwa użytkownika: ')
passwd = input('Hasło: ')

with connect('access.db') as conn:
    c = conn.cursor()
    # sql = "SELECT user FROM users WHERE user='%s' AND passwd='%s'" % (user, passwd)
    # print(sql)
    # c.execute(sql)
    c.execute("SELECT user FROM users WHERE user=? AND passwd=?", (user, passwd))
    u = c.fetchone()
    if not u:
        print('Niepoprawny login!')
    else:
        print('Zalogowano jako: ', u[0])
