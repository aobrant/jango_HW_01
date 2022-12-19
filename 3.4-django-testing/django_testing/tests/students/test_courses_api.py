# def test_example():
#     assert False, "Just test example"
from random import randint
import os
import json
from django.conf import settings


import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student
@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username='Test', password='password')

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs,make_m2m=True)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_getting_1st_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/{course.id}/')

    # Assert
    assert response.status_code == 200
    assert response.data['id'] == course.id

@pytest.mark.django_db
def test_getting_lst_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    assert len(response.data) == len(course)

@pytest.mark.django_db
def test_course_filtration_id(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)
    random_id = [c.id for c in course][randint(0, 9)]


    # Act
    response = client.get(f'/api/v1/courses/?id={random_id}')

    # Assert
    assert response.status_code == 200
    assert response.data[0]['id'] == random_id


@pytest.mark.django_db
def test_course_create(client):
    # Arrange
    path = os.path.join(settings.BASE_DIR, 'tests', 'courses.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Act
        create_response = client.post('/api/v1/courses/', data=data[0])

    # Assert
        assert create_response.status_code == 201

@pytest.mark.django_db
def test_course_renew(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    original_response = client.get(f'/api/v1/courses/{course.id}/')
    update_response = client.put(f'/api/v1/courses/{course.id}/', data={'name': 'name_new'})

    # Assert
    assert update_response.status_code == 200
    assert update_response.data != original_response.data

@pytest.mark.django_db
def test_course_delete(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)


    # Act
    retrieve_response = client.get(f'/api/v1/courses/{course.id}/')
    delete_response = client.delete(f'/api/v1/courses/{course.id}/')

    # Assert
    assert delete_response.status_code == 204

@pytest.mark.django_db
def test_course_name_filtrate(client, course_factory):
     # Arrange
     course = course_factory(_quantity=10)
     random_name = [c.name for c in course][randint(0, 9)]

     # Act
     response = client.get('/api/v1/courses/',{'name': random_name})

     # Assert
     assert response.status_code == 200
     assert response.data[0]['name'] == random_name







