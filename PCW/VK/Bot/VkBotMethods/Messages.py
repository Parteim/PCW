from requests import get as r_get

from PCW.VK.Bot.VkBot import VkBot


class Messages(VkBot):
    def __init__(self, bot):
        super(Messages, self).__init__(bot)

    def get_long_poll_server(self):
        response = super().get(
            'messages.getLongPollServer',
            need_pts=0,
            group_id=216089448,
            lp_version=3,
        )

        return response.json()

    def connect_long_poll_server(self):
        date_of_session = self.get_long_poll_server()['response']

        print(date_of_session)

        server = date_of_session['server']
        key = date_of_session['key']
        ts = date_of_session['ts']

        response = r_get(f'https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=3')

        return response.json()
