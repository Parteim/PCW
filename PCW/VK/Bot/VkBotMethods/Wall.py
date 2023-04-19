from PCW.VK.Bot.VkBot import VkBot


class Wall(VkBot):
    def get_posts(self, group, count_of_posts=81):
        posts = []
        offset = 0
        count = 100
        if count_of_posts <= 100:
            response = super().get(
                'wall.get', domain=group,
                count=count_of_posts,
                offset=offset,
            )
            posts.extend(response.json()['response']['items'])
        else:
            while count_of_posts > 0:
                response = super().get(
                    'wall.get',
                    domain=group,
                    count=count,
                    offset=offset,

                )
                posts.extend(response.json()['response']['items'])

                count_of_posts -= 100

                if count_of_posts > 100:
                    offset += 100
                else:
                    count = count_of_posts
                    offset += count_of_posts

        return posts


