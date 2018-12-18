import requests

class NBA:
    """
    Handles the NBA API
    """

    def __init__(self):
        self.base_url = 'http://data.nba.net/10s/prod/v1/today.json'
        self.players_url = 'http://data.nba.net/10s/prod/v1/{}/players.json'

    def get_api_links(self):
        """
        Gets the list of available API links
        :return: JSON object
        """
        try:
            r = requests.get(self.base_url)
            return r.json()
        except Exception as e:
            print(e)

    def get_players_list(self, year):
        """
        Gets the list of players
        :param year: YYYY in string format
        :return:
        """
        try:
            url = self.players_url
            r = requests.get(url.format(year))
            return r.json()
        except Exception as e:
            print(e)

    def find_player_by_name(self, last_name, first_name=None):
        """
        Searches a player from the player list by name
        :param last_name: player's last name
        :param first_name: player's first name, optional
        :return:
        """
        # get the player list
        raw_list = self.get_players_list('2018')
        player_list = raw_list['league']['standard']
        print(player_list)



if __name__ == '__main__':
    nba = NBA()
    print(nba.find_player_by_name(last_name='James'))