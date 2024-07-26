from tests.conftest import USER_NAME,USER_EMAIL,USER_PASSWORD
import logging
import pytest
# docker-compose run test-service
#https://github.com/Describly/fastapi-sqlalchemy-alembic?tab=readme-ov-file
#https://www.youtube.com/watch?v=7_3TnuQ4EVY&t=381s

def test_create_user(client):
    data ={
        "name":USER_NAME,
        "email":USER_EMAIL,
        "password":USER_PASSWORD
    }
    response =client.post('/users',json=data) 
    assert response.status_code == 201
    assert "password" not in response.json()


# it should not allow duplicate email
def test_create_user_with_existing_email_should_not_return_status_code_201(client,user):
    
    request_payload={
        "name":"Sam Samal",
        "email":user.email,
        "password":USER_PASSWORD
    }
    response =client.post('/users',json=request_payload)
    assert response.status_code !=201
    
@pytest.mark.parametrize("password",["",12345])
def test_create_with_valid_password(client,test_logger,password):
    request_payload:dict = {
          "name":"Sam Samal",
        "email":USER_EMAIL,
        "password":''
    }
    response = client.post('/users', json=request_payload)
    test_logger.debug(f"Response content: {response.content}")
    assert response.status_code != 201    
#     assert response.status_code ==400
# def test_create_user_with_empty_password(client,test_logger):
#      request_payload={
#         "name":"Sam Samal",
#         "email":USER_EMAIL,
#         "password":''
#     }
#      response =client.post('/users',json=request_payload)
#      test_logger.debug(f"Response content: {response.content}")
#      assert response.status_code !=201

# def test_create_user_with_numeric_password(client,test_logger):
#     request_payload={
#         "name":"Sam Samal",
#         "email":USER_EMAIL,
#         "password":'123433'
#     }
#     response =client.post('/users',json=request_payload)
#     test_logger.debug(f"Response content: {response.content}")
#     assert response.status_code !=201


def test_create_user_with_char_password():
    pass
