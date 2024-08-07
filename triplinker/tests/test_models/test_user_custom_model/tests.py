# Another app modules.
import pytest

# !Triplinker modules:
from accounts.models.TLAccount_frequest import TLAccount


@pytest.mark.django_db
@pytest.fixture
def user_obj():
    new_acc = TLAccount.objects.create_user('Robin', 'Long',
    	'robin@example.com', "M", "1992-09-13", "US", "secret")
    return new_acc


@pytest.mark.django_db
def test_user_has_created(user_obj):
    assert user_obj.__class__.objects.count() == 1


@pytest.mark.django_db
def test_main_fields(user_obj):
	assert user_obj.first_name == "Robin"
	assert user_obj.second_name == "Long"
	assert user_obj.email == "robin@example.com"
	assert user_obj.sex == "M"
	assert user_obj.date_of_birth == "1992-09-13"
	assert user_obj.country == "US"
	assert user_obj.is_active == True
	assert user_obj.is_admin == False
	assert user_obj.is_superuser == False
	assert user_obj.is_staff == False
