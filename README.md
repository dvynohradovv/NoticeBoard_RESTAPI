# notice-board-drf

# Basic models:
## ● User
![image](https://user-images.githubusercontent.com/55922843/158640762-0cdfa853-baf7-49da-9e23-c8549b367123.png)

## ● Post (always made by a user)
![image](https://user-images.githubusercontent.com/55922843/158640816-7c77e343-5adc-471a-b2cd-5298fe1c2496.png)

# Basic Features:

## ● user signup
### `api/auth/users/`
![image](https://user-images.githubusercontent.com/55922843/158642242-e54107c6-15d5-4b9b-87d7-a426ff65e4dc.png)

## ● user login
### `api/api-auth/login/`
![image](https://user-images.githubusercontent.com/55922843/158641541-e9179363-1fb9-42cd-a5f1-c5434311ec30.png)

## ● post creation
### `api/posts/`
![image](https://user-images.githubusercontent.com/55922843/158646788-c446551e-4732-40f5-b64c-45feb73f27a0.png)

## ● post edit, like, unlike
### `api/post_likes/:id`
![image](https://user-images.githubusercontent.com/55922843/158647819-6c46f412-361b-42a9-9e06-d269da651ced.png)
![image](https://user-images.githubusercontent.com/55922843/158648377-182f8a12-6e32-457d-acb8-80e5b2fc8157.png)

## ● analytics about how many likes was made. API should return analytics aggregated by day.
`/api/analitics/?date_from=2020-02-02&date_to=2020-02-15` 
![image](https://user-images.githubusercontent.com/55922843/158659060-ca5190c8-a710-48b8-bf26-5b3e08cee1d7.png)


## ● user activity an endpoint which will show when user was login last time and when he mades a last request to the service.
`api/users/1/`
![image](https://user-images.githubusercontent.com/55922843/158659671-4c27dbcf-e2c1-4269-ac09-b293126473a6.png)


Requirements:
## ● Implement token authentication (JWT is prefered)
![image](https://user-images.githubusercontent.com/55922843/158660712-73f4e4de-cf15-4c13-a97b-8fad08bee36e.png)
