data = {
    'user': 'root',
    'password': 'planb!0017',
    'host': '127.0.0.1',
    'port': '3307',
    'database': 'planb'
}

DB_URL = f"mysql+mysqlconnector://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['database']}?charset=utf8"
