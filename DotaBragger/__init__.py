from DotaBragger.dota import DotaHandler
from DotaBragger.twitter import Twitter

def main():
	unformatted = 'Just played one Dota match as {} with K/D/A: {}/{}/{}'
	handler = DotaHandler()
	account_id 	= 165019503
	player = handler.get_latest_match_player_data(account_id)
	status = unformatted.format(handler.get_hero_name(player['hero_id']),
								player['kills'], 
								player['deaths'], 
								player['assists'])
	print status

	
	twitter = Twitter()
	twitter.update_status(status) 