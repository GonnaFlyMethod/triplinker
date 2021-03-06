# Django modules.
from django.db import models

# !Triplinker modules:

# Another apps modules.
from accounts.models.TLAccount_frequest import TLAccount
from trip_places.models import Place


class Journey(models.Model):

    VISIBILITY_CHOICES = [
        ("All", "All users"),
        ("FriendsFollowers", "Friends & followers"),
        ("Friends", "Friends only"),
        ("Me", "Only me"),
    ]
    visibility = models.CharField("The level of visibility", max_length=16,
                                  choices=VISIBILITY_CHOICES, blank=False,
                                  null=True)
    journey_from = models.CharField("The point where the journey was started",
                                    max_length=35, blank=True, null=True)
    place_from = models.ForeignKey(Place, on_delete=models.CASCADE,
                                   related_name="start_places", blank=True,
                                   null=True)
    date_of_start = models.DateField(null=True)
    journey_to = models.CharField("The point where the journey was finished",
                                  max_length=35, blank=True,  null=True)
    place_to = models.ForeignKey(Place, on_delete=models.CASCADE,
                                 related_name="end_places", blank=True,
                                 null=True)
    date_of_end = models.DateField(null=True)

    vb_name_p = 'Particapants of the journey'

    participants = models.ManyToManyField(TLAccount,
                                          through='journeys.Participant',
                                          verbose_name=vb_name_p, blank=True,
                                          default=None,
                                          related_name='get_jrns')

    description = models.TextField("Describe your journey", max_length=500,
                                   blank=True, null=True)
    vb_name_who = "The person who has created the journey's page"

    acc = TLAccount
    who_added_the_journey = models.ForeignKey(acc, verbose_name=vb_name_who,
                                              related_name='who_added',
                                              on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        format_s = self.journey_from, self.journey_to, self.place_from
        return 'From: {}, to: {}, start place: {}'.format(*format_s)

    def get_visibility(self):
        return self.visibility

    def check_instance(self):
        return 'Journey'

    class Meta:
        ordering = ('-timestamp',)
        app_label = 'journeys'
        verbose_name = 'Journey'
        verbose_name_plural = 'Journeys'


class Participant(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE, null=True)
    participant = models.ForeignKey(TLAccount, on_delete=models.CASCADE,
                                    related_name='participant_set', null=True)

    def __str__(self):
        jrn_s = self.journey.journey_from
        jrn_f = self.journey.journey_to
        partic = self.participant.email
        return "Journey: {} - {}, participant: {}".format(jrn_s, jrn_f, partic)


class Activity(models.Model):
    journey = models.ForeignKey(Journey, related_name="activities",
                                on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField("Description of activity",
                                   max_length=35, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name="places", blank=True, null=True)
    date_of_start = models.DateField(null=True, blank=True,)
    date_of_end = models.DateField(null=True, blank=True,)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Journey {self.journey}"

    class Meta:
        ordering = ('-timestamp',)
        app_label = 'journeys'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
