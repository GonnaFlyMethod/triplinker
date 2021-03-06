# Django modules.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied

# !Triplinker modules:

# Another apps modules.
from accounts.models.TLAccount_frequest import TLAccount
from feed.models import Post, Notification

# Current app modules.
from .models import Journey, Participant, Activity, Place
from .forms import AddJourneyForm, AddActivityForm
from .helpers.views.get_allowed_journeys import get_allowed_journeys
from .helpers.views.get_average_rating import get_rating


def activity_form_api(request):
    form = AddActivityForm(request.POST)
    print(request.POST)
    if form.is_valid():
        activity = form.save(commit=False)
        activity.journey = Journey.objects.get(id=request.POST['journey_id'])
        activity.save()
        context = {
            'status': True,
        }
        return JsonResponse(context, safe=False)
    return JsonResponse({'status': False}, safe=False)


def journey_form_api(request):
    form = AddJourneyForm(request.POST)
    print(request.POST)
    if form.is_valid():
        journey = form.save(commit=False)
        journey.who_added_the_journey = request.user
        journey.save()
        journey.participants.add(request.user)
        journey.save()
        context = {
            'journey_id': journey.id,
            'status': True,
        }
        user = request.user
        journey_to = request.POST["journey_to"]
        journey_date = request.POST["date_of_start"]
        place_to = Place.objects.get(id=request.POST["place_to"])
        NEW_JOURNEY_POST_TEXT = f'I am starting a new journey to '\
                                f'{journey_to} on {journey_date}.'
        NEW_JOURNEY_NOTIF_TEXT = f'{user} is starting a new journey to '\
                                 f'{journey_to} on {journey_date}.'
        post = Post.objects.create(is_place=True, content=NEW_JOURNEY_POST_TEXT,
                                   author=user, place=place_to, journey=journey,
                                   notification_post=True)
        post.save()
        notification = Notification.objects.create(post=post,
                                                   text=NEW_JOURNEY_NOTIF_TEXT,
                                                   is_journey=True)
        notification.users.set(user.friends.all())
        notification.save()
        return JsonResponse(context, safe=False)
    return JsonResponse({'status': False}, safe=False)


def edit_journey(request, journey_id):

    journey = Journey.objects.get(pk=journey_id)

    if journey.who_added_the_journey != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = AddJourneyForm(request.POST, instance=journey)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journeys:journey-page',
                                        kwargs={'journey_id': journey.id}))

    form = AddJourneyForm(instance=journey)
    return render(request, 'journeys/edit_journey.html', {'form': form})


def edit_activity(request, activity_id):

    activity = Activity.objects.get(pk=activity_id)

    if activity.journey.who_added_the_journey != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = AddActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journeys:journey-page',
                                        kwargs={'journey_id':
                                                activity.journey.id}))

    form = AddActivityForm(instance=activity)
    return render(request, 'journeys/edit_activity.html', {'form': form})


def add_new_journey(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('journeys:journey-list',
                                    kwargs={'user_id': request.user.id}))
    context = {
        'form': AddJourneyForm(),
        'activity_form': AddActivityForm(),
    }
    return render(request, 'journeys/add_journey_form.html', context)


def user_journey_list(request, user_id):
    current_user = request.user
    another_user = get_object_or_404(TLAccount, id=user_id)

    journeys = get_allowed_journeys(current_user, another_user)
    context = {
        'user_acc': another_user,
        'journeys': journeys
    }
    return render(request, 'journeys/user_journeys_list.html', context)


def journey_page(request, journey_id):
    journey = get_object_or_404(Journey, id=journey_id)
    creator_of_journeys_page = journey.who_added_the_journey
    context = {
        'journey': journey,
        'creator_of_journeys_page': creator_of_journeys_page,
    }
    return render(request, 'journeys/journey_page.html', context)


def sort_journeys_by_rating_of_place(request, user_id):
    user = get_object_or_404(TLAccount, id=user_id)
    journeys_raw = Participant.objects.filter(participant=user)

    journeys = []
    for participant_object in journeys_raw:
        journeys.append(participant_object.journey)

    sort = sorted(journeys, key=lambda journey: get_rating(journey),
                  reverse=False)

    context = {
        'user_acc': user,
        'journeys': sort,
    }
    return render(request, 'journeys/user_journeys_list.html', context)


def sort_journeys_by_date(request, user_id):
    user = get_object_or_404(TLAccount, id=user_id)
    journeys_raw = Participant.objects.filter(participant=user)

    journeys = []
    for participant_object in journeys_raw:
        journeys.append(participant_object.journey)

    sort = sorted(journeys, key=lambda journey: journey.date_of_start,
                  reverse=False)
    context = {
        'user_acc': user,
        'journeys': sort,
    }
    return render(request, 'journeys/user_journeys_list.html', context)


def join_journey(request, journey_id):
    journey = Journey.objects.get(pk=journey_id)
    journey.participants.add(request.user)
    journey.save()

    user = request.user
    journey_to = journey.journey_to
    journey_date = journey.date_of_start
    NEW_JOURNEY_POST_TEXT = f'I am joining {journey.who_added_the_journey} ' \
                            f'in a journey to ' \
                            f'{journey_to} on {journey_date}.'
    NEW_JOURNEY_NOTIF_TEXT = f'{user} is joining you in a journey to ' \
                             f'{journey_to} on {journey_date}.'
    post = Post.objects.create(is_place=True, content=NEW_JOURNEY_POST_TEXT,
                               author=user, place=journey.place_to,
                               journey=journey, notification_post=True)
    post.save()
    notification = Notification.objects.create(post=post,
                                               text=NEW_JOURNEY_NOTIF_TEXT,
                                               is_journey=True)
    notification.users.set(user.friends.all())
    notification.save()
    return HttpResponseRedirect(reverse('journeys:journey-page',
                                kwargs={'journey_id': journey_id}))


def leave_journey(request, journey_id):
    journey = Journey.objects.get(pk=journey_id)
    journey.participants.remove(request.user)
    journey.save()

    post = Post.objects.filter(author=request.user, journey=journey)
    post.delete()
    return HttpResponseRedirect(reverse('journeys:journey-page',
                                kwargs={'journey_id': journey_id}))


def remove_from_journey(request, journey_id, user_id):
    user = TLAccount.objects.get(pk=user_id)
    journey = Journey.objects.get(pk=journey_id)
    journey.participants.remove(user)
    journey.save()
    post = Post.objects.filter(author=user, journey=journey)
    post.delete()
    return HttpResponseRedirect(reverse('journeys:journey-page',
                                kwargs={'journey_id': journey_id}))
