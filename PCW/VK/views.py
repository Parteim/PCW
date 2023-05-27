from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .Bot.VkBotMethods.Wall import Wall
from .Bot.VkBot import VkBotInstance
from .Bot.Domain.ImgFilter import posts_img_filter

from .models import VkBotModel, VkCommunity

from .forms import VkBotCreationForm, VkCommunityForm


def index(request):

    return render(request, 'main/index.html')


@login_required
def get_posts(request):
    bot = VkBotInstance(
        access_token=''
    )

    posts = Wall(bot).get_posts('land_of_art')

    f_posts = posts_img_filter(posts)

    return render(request, 'main/get_posts.html', {'posts': f_posts})


@login_required
def create_vk_bot(request):
    if request.method == 'POST':
        form = VkBotCreationForm(request.POST, )
        if form.is_valid():
            print(request.POST)
            VkBotModel.objects.create(
                name=request.POST['name'],
                access_token=request.POST['access_token'],
                user=request.user,
            )
            bot_name = name = request.POST['name']
            messages.success(request, f'bot "{bot_name}" created')
            return redirect('bot-list')

    form = VkBotCreationForm
    return render(request, 'vk/create_vk_bot.html', {'form': form})


@login_required
def get_bot_list(request):
    vk_bot_list = VkBotModel.objects.filter(user=request.user)

    return render(request, 'main/bot_list.html', {'bot_list': vk_bot_list})


@login_required
def bot_settings(request):
    return redirect('home')


@login_required
def vk_bot_instance(request, pk):
    bot = VkBotModel.objects.get(pk=pk)
    group_list = VkCommunity.objects.filter(parser=bot)

    data = {
        'bot': bot,
        'group_list': group_list,
    }

    return render(request, 'vk/vk_bot_instance.html', data)


@login_required
def add_group_to_parse_list(request, bot_id):
    if request.method == 'POST':
        form = VkCommunityForm(request.POST)
        if form.is_valid():
            bot = VkBotModel.objects.get(pk=bot_id)
            VkCommunity.objects.create(
                name=request.POST['name'],
                domain=request.POST['domain'],
                owner_id=request.POST['owner_id'],
                parser=bot,
            )
            return redirect('vk-bot-instance', bot_id)
    data = {
        'form': VkCommunityForm
    }
    return render(request, 'vk/add_group.html', data)
