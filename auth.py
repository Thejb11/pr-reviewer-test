def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "'"
    password_hash = md5(password)
    return query
