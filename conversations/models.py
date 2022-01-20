from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models
# Conversation은 Message의 집합

class Conversation(core_models.TimeStampedModel):

    """ Conversations Definition """

    participants = models.ManyToManyField("users.User", related_name = "conversation", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)


    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    """ Message Definition, Message는 Conversation의 원소 """

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages",on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name="messages",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"