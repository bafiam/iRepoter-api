class DatabaseTables():
    """Database class"""

    def table_query(self):
        users = """CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        othernames character varying(50) NOT NULL,
        lastname character varying(50) NOT NULL,
        username character varying(50) NOT NULL,
        email character varying(50) NOT NULL UNIQUE,
        phone_number character varying(13) NOT NULL UNIQUE,
        is_admin BOOLEAN NOT NULL DEFAULT FALSE,
        registered timestamp with time zone DEFAULT \
        ('now'::text):: date NOT NULL,
        password character varying(50) NOT NULL
            )"""

        incidents = """CREATE TABLE IF NOT EXISTS incidents(
        incident_id serial PRIMARY KEY NOT NULL,
        createdon timestamp with time zone DEFAULT\
         ('now'::text):: date NOT NULL,
        createdby numeric NOT NULL,
        type character varying(50) NOT NULL,
        location character varying(100) NOT NULL,
        status character varying(20),
        comment character varying(2000) NOT NULL,
        images character varying(20),
        video character varying(20)
            )"""

        self.query = [users, incidents]
        return self.query

    def drop_table_query(self):
        """Resource for teardown when am testing"""
        drop_users = """DROP TABLE IF EXISTS users"""

        drop_incidents = """DROP TABLE IF EXISTS category CASCADE"""

        self.query = [drop_users, drop_incidents]

        return self.query
