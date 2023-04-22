
def img_filter(img_list):
    filtered_img_list = []

    for post in img_list:
        for attachment in post['attachments']:
            if attachment['type'] == 'photo':
                for img in attachment['photo']['sizes']:
                    if img['type'] == 'z':
                        filtered_img_list.append(img['url'])

    return filtered_img_list


