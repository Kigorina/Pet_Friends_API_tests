from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

#Get api key tests

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_unvalid_user(email='siper28464@95ta.com', password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_valid_password(email=valid_email, password='valid_password'):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

# Get api pets tests

def test_get_all_pets_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

#Post api pets tests

def test_add_new_pet_valid_data(name='Vaska', animal_type='Cotyara', age='5', pet_photo='images/cat.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_incorrect_data(name='!%$#^&&&**^', animal_type='15489', age='11111111111', pet_photo='images/cat.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_name_kirilitza(name='Васька', animal_type='Cotyara', age='3', pet_photo='images/cat.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_data(name='', animal_type='', age='', pet_photo='images/cat.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_wrong_file_format(name='Vaska', animal_type='Cat', age='6', pet_photo='images/cat.pdf'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
#Delete api pets tests

def test_delete_pet_successfully():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Kot-programmer", "Cat", "5", "images/cat.jpeg")
        _, my_pets = pf.delete_pet(auth_key, "my_pets")
    pet_id = my_pets['pets'] [0] ['id']
    status, _ = pf.delete_pet(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

# Put api pets tests

def test_update_pet_info_successfully(name='Kot-programmer', animal_type='Cat', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.put_pet(auth_key, my_pets['pets'] [0] ['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

#Post api create pet test

def test_create_pet_simple_successfully(name='Mifodiy', animal_type='racoon', age='6'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

#Post api pets set photo tests

def test_set_photo_successfully(pet_photo='images/racoon.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.set_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        










