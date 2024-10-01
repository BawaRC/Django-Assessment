"""
Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer : Yes, Django signals run in the same database transaction as the caller by default. That is - If the transaction is rolled back, the signal's effects are also rolled back.
The code snippet to support the answer is as follow :
"""
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal executed, but changes might be rolled back")

# Simulating saving a user instance with transaction management
try:
    with transaction.atomic():
        user = User(username='test_user')
        user.save()
        raise Exception("Something went wrong, rolling back transaction")
except Exception as e:
    print(e)

# Check if user was saved
if not User.objects.filter(username='test_user').exists():
    print("User not saved, transaction rolled back")
else:
    print("User saved")

"""
Explanation - 
This code saves a user inside a transaction block. After saving, it raises an exception to force a rollback. Since the transaction is rolled back, the signal handler (user_saved_handler) prints a message, but the user is not saved to the database. This shows that the signal runs in the same transaction as the caller.
"""