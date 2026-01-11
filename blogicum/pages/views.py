from django.shortcuts import render


def about(request):
    context = {
        'active_page': 'about'
    }
    return render(request, 'pages/about.html', context)


def rules(request):
    context = {
        'active_page': 'rules'
    }
    return render(request, 'pages/rules.html', context)
