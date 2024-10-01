"""
Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer : By default, Django signals are executed synchronously. That is - When a signal is triggered, the connected receiver functions are executed immediately and block the flow of execution until they are completed. 
The code snippet to support the answer is as follow :-
"""
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received for User: {instance.username}")
    # Simulate long-running task
    time.sleep(5)
    print("Signal processing done")

# Simulating saving a user instance
user = User(username='test_user')
user.save()

print("This line will only print after the signal has completed")

"""
Explanation - 
When saving a User, the user_saved_handler signal is triggered. The time.sleep(5) in the signal handler simulates a blocking operation. The message "This line will only print after the signal has completed" proves that the signal is executed synchronously because it only appears after the signal handler finishes.
"""