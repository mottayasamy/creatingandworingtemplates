from django.shortcuts import render

def index(request):
    context = {
        'result': '',
        'filtered_names': []
    }

    # Odd or Even Checker
    if request.method == 'POST' and 'check_odd_even' in request.POST:
        try:
            number = int(request.POST.get('number'))
            if number % 2 == 0:
                context['result'] = f'{number} is an even number'
            else:
                context['result'] = f'{number} is an odd number'
        except ValueError:
            context['result'] = 'Please enter a valid number'

    # Name Filter
    names_list = [ 'Alice', 'Andrew', 'Amelia', 'Aaron', 'Benjamin', 'Bella', 'Brian', 'Brittany', 'Christopher']
    if request.method == 'POST' and 'search_name' in request.POST:
        character = request.POST.get('character').lower()
        if character:  # Check if the character input is not empty
            context['filtered_names'] = [name for name in names_list if name.lower().startswith(character)]

    return render(request, 'webapp/index.html', context)
