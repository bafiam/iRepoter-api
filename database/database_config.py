class DatabaseTables():
    """Database class"""

    def table_query(self):
        users = """CREATE TABLE IF NOT EXISTS users
        (
        id serial primary key not null,
        firstname char varying(50),
        othernames char varying(50),
        lastname char varying(50),
        username char varying(50) not null ,
        email char varying(50) not null,
        phone_number character varying(13) unique ,
        is_admin boolean  default false,
        registered timestamp ,
        password char varying(50777) not null 
            )"""

        incidents = """CREATE TABLE IF NOT EXISTS incidents(
        incident_id serial primary key not null ,
        createdon timestamp not null ,
        createdby numeric not null ,
        type char varying(50) not null ,
        location char varying(100) NOT NULL,
        status char varying(20),
        comment char varying(2000) NOT NULL,
        images char varying(20),
        video char varying(20)
            )"""
        print("Table created successfully")
        self.query = [users, incidents]
        return self.query

    def drop_table_query(self):
        """Resource for teardown when am testing"""
        drop_users = """DROP TABLE IF EXISTS users"""

        drop_incidents = """DROP TABLE IF EXISTS category CASCADE"""

        self.query = [drop_users, drop_incidents]

        return self.query
