from database.data_provider import ClubsDataProvider, PlayersDataProvider

players = PlayersDataProvider()
players.web_scrap(332)