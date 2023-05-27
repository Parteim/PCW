def img_filter(img_list):
    filtered_img_list = []

    for post in img_list:
        for attachment in post['attachments']:
            if attachment['type'] == 'photo':
                for img in attachment['photo']['sizes']:
                    if img['type'] == 'z':
                        filtered_img_list.append(img['url'])

    return filtered_img_list


def posts_img_filter(posts_list):
    filtered_posts_list = []

    for post in posts_list:
        filtered_posts_list.append([])
        for attachment in post['attachments']:
            if attachment['type'] == 'photo':
                for img in attachment['photo']['sizes']:
                    if img['type'] == 'z':
                        filtered_posts_list[-1].append(img['url'])
    return filtered_posts_list

# bot = VkBotInstance(
#     access_token='4f2c35104f2c35104f2c3510114c3c892044f2c4f2c35102c0950b4e8b4d099257fd1f0'
# )
#
# posts = Wall(bot).get_posts('fujiwaraclan')
#
# print(posts_img_filter(posts))
