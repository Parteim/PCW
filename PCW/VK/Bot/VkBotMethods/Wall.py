from PCW.VK.Bot.VkBot import VkBot


class Wall(VkBot):

    def get_posts(self, group, count_of_posts=100):
        posts = []
        offset = 0
        count = 100

        response = super().get(
            'wall.get',
            domain=group,
            count=count,
            offset=offset,

        )
        posts.extend(response.json()['response']['items'])
        print(posts)


Wall().get_posts('fujiwaraclan')
