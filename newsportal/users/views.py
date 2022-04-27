from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProfileForm


@login_required
def profile(request):
    '''Показать профиль '''
    user = request.user
    return render(request, 'users/profile.html', {'users': user})


@login_required
def change_profile(request):
    '' 'обновить личную информацию' ''
    if request.method == 'POST':
        # параметр экземпляра означает инициализировать форму экземпляром модели, чтобы вы могли обновить данные через форму
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Добавьте сообщение, и форма будет перенаправлена на страницу личной информации, если проверка формы прошла успешно
            messages.add_message(request, messages.SUCCESS, 'Личная информация обновлена успешно!')
            return redirect('users:profile')
    else:
        # Вернуть пустую форму, если это не POST запрос
        form = ProfileForm(instance=request.user)

    return render(request, 'users/change_profile.html', context={'form': form})
