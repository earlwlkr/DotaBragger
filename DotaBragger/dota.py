from DotaBragger.user import User


class DotaHandler(User):
	"""
	Handles Dota API data.
	API Doc: http://dev.dota2.com/showthread.php?t=58317
	"""
	steam_api_key 		= ''

	url_get_heroes 			= 'https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/'
	url_get_match_history 	= 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/'
	url_get_match_details 	= 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/'

	def __init__(self):
		super(DotaHandler, self).__init__()
		self.heroes = self.get_heroes_list()

	def get_heroes_list(self):
		params = {'key': self.steam_api_key}
		response = self.get(self.url_get_heroes, params=params)
		raw_list = response.json()['result']['heroes']
		return {hero['id']: hero['name'] for hero in raw_list}

	def normalize_hero_name(self, response_name):
		name = response_name.replace('npc_dota_hero_', '')
		return name.replace('of', ' of ').replace('_', ' ').title()

	def get_hero_name(self, hero_id):
		return self.normalize_hero_name(self.heroes[hero_id])

	def get_latest_matches_brief(self, account_id, num_matches=1):
		params = {
			'key': 					self.steam_api_key,
			'account_id': 			account_id,
			'matches_requested': 	num_matches
		}

		response = self.get(self.url_get_match_history, params=params)
		if num_matches == 1:
			return response.json()['result']['matches'][0]
		return response.json()['result']['matches']

	def get_match_details(self, match_id):
		params = {
			'key': 		self.steam_api_key,
			'match_id': match_id
		}

		response = self.get(self.url_get_match_details, params=params)
		return response.json()['result']['players']

	def get_match_player_data(self, match_id, account_id):
		match = self.get_match_details(match_id)
		for player in players:
			if player['account_id'] == account_id:
				return player
		return None

	def get_latest_match_player_data(self, account_id):
		latest_match = self.get_latest_matches_brief(account_id)
		players = self.get_match_details(latest_match['match_id'])

		for player in players:
			if player['account_id'] == account_id:
				return player

	def print_player_data(self, player):
		print '* Hero: ' + self.get_hero_name(player['hero_id'])
		print '* K/D/A: {}/{}/{}'.format(player['kills'], 
										 player['deaths'], 
										 player['assists'])
		print '* Gold: ' + str(player['gold'])
		print '* Last hits/Denies: {}/{}'.format(player['last_hits'], 
												 player['denies'])
		print '* Hero damage: ' + str(player['hero_damage'])

