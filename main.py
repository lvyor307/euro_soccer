from database.data_provider import ClubsDataProvider, PlayersDataProvider


if __name__ == '__main__':
    database_uri = "postgresql+psycopg2://lvyor307:Aa123456@localhost:5432/FIFA_DB"
    players = PlayersDataProvider()
    players.web_scrap(332)
    players.drop_duplicates()
    players.push_to_db(table_name='players', database_uri=database_uri)
    clubs = ClubsDataProvider()
    clubs.web_scrap(12)
    clubs.drop_duplicates()
    clubs.push_to_db(table_name='clubs', database_uri=database_uri)
