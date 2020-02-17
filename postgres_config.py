# Connection setttings for postgresql12 server

#Username/pw/database/address

postgres_address = 'localhost'
postgres_port = '5432'
postgres_username = 'postgres'
postgres_password = '78f47f33fac44e478456f537e1e20ee4'
postgres_dbname = 'this_is_jeopardy'

pg_engine_params = f'postgresql://{postgres_username}:{postgres_password}@{postgres_address}:{postgres_port}/{postgres_dbname}'