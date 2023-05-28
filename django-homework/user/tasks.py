from celery import shared_task
from .models import User
from purchase.models import Purchase


@shared_task
def welcome_message():
    print('Hello, User! You\'re using Celery! :)')


@shared_task
def user_purchases(user_id):
    user = User.objects.get(id=user_id)
    purchase_count = Purchase.objects.filter(user_id=user).count()
    print(f"User {user.first_name} {user.last_name} has {purchase_count} purchases")


@shared_task
def users_count():
    users = User.objects.all()
    print(f"Users q-ty: {users.count()}")
