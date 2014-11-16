from DotaBragger.user import User
from requests_oauthlib import OAuth1

class Twitter(User):
    def __init__(self, *a, **kw):
        super(Twitter, self).__init__(*a, **kw)

        self.session.auth = OAuth1(
            '',
            '',
            '',
            '',
            signature_type='auth_header')

    def update_status(self, status):
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        data = {
            'status': status
        }
        response = self.post(url, data=data)