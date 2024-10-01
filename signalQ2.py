"""
Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer : Yes, by default, Django signals run in the same thread as the caller. That is - The signal and the caller share the same thread context.
The code snippet to support the answer is as follow :
"""
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Simulating saving a user instance
print(f"Save method called in thread: {threading.current_thread().name}")
user = User(username='test_user')
user.save()

"""
Explanation - 
This snippet prints the thread name where the save() method is called and the thread where the signal is handled. If both messages show the same thread name, it confirms that the signal runs in the same thread as the caller.
"""