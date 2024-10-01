# **Questions for Django**

## [Topic: **Django Signals**](https://docs.djangoproject.com/en/3.2/topics/signals/)

**Question 1**: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer** : By default, Django signals are executed synchronously. That is \- When a signal is triggered, the connected receiver functions are executed immediately and block the flow of execution until they are completed.   
The code snippet to support the answer is as follow :-

	import time  
    from django.db.models.signals import post\_save  
    from django.dispatch import receiver  
    from django.contrib.auth.models import User

    @receiver(post\_save, sender=User)  
    def user\_saved\_handler(sender, instance, \*\*kwargs):  
        print(f"Signal received for User: {instance.username}")  
        \# Simulate long-running task  
        time.sleep(7)  
        print("Signal processing done")

    \# Simulating saving a user instance  
    user \= User(username='test\_user')  
    user.save()

    print("This line will only print after the signal has completed") 

*Explanation* \-
   
When saving a User, the user\_saved\_handler signal is triggered. The time.sleep(5) in the signal handler simulates a blocking operation. The message "This line will only print after the signal has completed" proves that the signal is executed synchronously because it only appears after the signal handler finishes.

#

**Question 2**: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer** : Yes, by default, Django signals run in the same thread as the caller. That is \- The signal and the caller share the same thread context.  
The code snippet to support the answer is as follow :

	import threading  
    from django.db.models.signals import post\_save  
    from django.dispatch import receiver  
    from django.contrib.auth.models import User

    @receiver(post\_save, sender=User)  
    def user\_saved\_handler(sender, instance, \*\*kwargs):  
        print(f"Signal running in thread: {threading.current\_thread().name}")

    \# Simulating saving a user instance  
    print(f"Save method called in thread: {threading.current\_thread().name}")  
    user \= User(username='test\_user')  
    user.save()

*Explanation* \-
   
This snippet prints the thread name where the save() method is called and the thread where the signal is handled. If both messages show the same thread name, it confirms that the signal runs in the same thread as the caller.

#

**Question 3**: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer** : Yes, Django signals run in the same database transaction as the caller by default. That is \- If the transaction is rolled back, the signal's effects are also rolled back.  
The code snippet to support the answer is as follow :

	from django.db import transaction  
    from django.db.models.signals import post\_save  
    from django.dispatch import receiver  
    from django.contrib.auth.models import User

    @receiver(post\_save, sender=User)  
    def user\_saved\_handler(sender, instance, \*\*kwargs):  
        print("Signal executed, but changes might be rolled back")

    \# Simulating saving a user instance with transaction management  
    try:  
        with transaction.atomic():  
            user \= User(username='test\_user')  
            user.save()  
            raise Exception("Something went wrong, rolling back transaction")  
    except Exception as e:  
        print(e)

    \# Check if user was saved  
    if not User.objects.filter(username='test\_user').exists():  
        print("User not saved, transaction rolled back")  
    else:  
        print("User saved")

*Explanation* \-
   
This code saves a user inside a transaction block. After saving, it raises an exception to force a rollback. Since the transaction is rolled back, the signal handler (user\_saved\_handler) prints a message, but the user is not saved to the database. This shows that the signal runs in the same transaction as the caller.

#

## Topic: **Custom Classes** in Python

**Description:** You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the `Rectangle` class requires `length:int` and `width:int` to be initialized.  
2. We can iterate over an instance of the `Rectangle` class   
3. When an instance of the `Rectangle` class is iterated over, we first get its length in the format: **`{'length': <VALUE_OF_LENGTH>}`** followed by the width **`{width: <VALUE_OF_WIDTH>}`**



**Answer** : The code snippet for custom class is as follows - 

    class Rectangle:
        def __init__(self, length: int, width: int):
            self.length = length
            self.width = width

        def __iter__(self):
            # Yield the length in the specified format
            yield {'length': self.length}
            # Then yield the width in the specified format
            yield {'width': self.width}

    # Example usage:
    rect = Rectangle(10, 5)

    # Iterate over the instance
    for attribute in rect:
        print(attribute)



*Explanation* \- 

Initialization: The Rectangle class is initialized with two parameters: length and width, both of which are integers.

Iteration with \_\_iter\_\_: The \_\_iter\_\_ method is defined to allow iteration over the instance. The method uses yield to first return the length in the required format ({'length': \<value\>}) and then the width ({'width': \<value\>}).  
	  
**Output Example:**

    {'length': 10}  
    {'width': 5}

This implementation meets the requirements by making the Rectangle class both iterable and able to yield its length and width in the specified format.
#