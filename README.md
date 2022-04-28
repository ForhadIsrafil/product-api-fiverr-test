# product-api-fiverr-test

#Product-API(Fiverr) (2022)

## Base url: http://127.0.0.1:8000/api/

### HTTP REQUEST :  **POST /user/login**

###### params

```json
{
  "username": "knzd@phpbb.uu.gl",
  "password": "123456"
}
```

###### output

### possible response list:

1. HTTP_200_OK ----- success
2. HTTP_400_BAD_REQUEST ----- Required fields not given

``` json
{
    "first_name": "forhad",
    "last_name": "israfil",
    "email": "ifee@gmail.com",
    "token": "de363096afea5f8a4cc8e7fc271539a0d759f0a6"
}
```

### HTTP REQUEST :  **POST /user/signup**

###### params

```json
{
  "first_name": "forhad",
  "last_name": "israfil",
  "username": "ifeee",
  "email": "ifeee@gmail.com",
  "password": "lasdfkj"
}
```

###### output

### possible response list:

1. HTTP_201_CREATED ----- success
2. HTTP_400_BAD_REQUEST ----- Required fields not given

``` json
{
    "success": true
}
```

### HTTP REQUEST :  **POST /create-product**

###### params

### Authorization

```json
{
  "Authorization": "Token de363096afea5f8a4cc8e7fc271539a0d759f0a6"
}
```

### Body

```json
{
  "name": "product 23",
  "_class": "Dry Food",
  "price": 220,
  "status": "available",
  "image": "https://images.unsplash.com/photo-1598799170815-933217492614",
  "variant": [
    "7308afe2-fbfd-46b6-9aac-4094a83be4ee",
    "d4279a15-d500-42ce-8a77-e0d6111a7295",
    "de74699d-1249-4dda-82f0-e14f3e219cb6"
  ]
}
```

###### output

### possible response list:

1. HTTP_201_CREATED ----- success
2. HTTP_400_BAD_REQUEST ----- Required fields not given

``` json
{
    "success": true
}
```

### HTTP REQUEST :  **PATCH /product/<str:id>**

###### params

### Authorization

```json
{
  "Authorization": "Token de363096afea5f8a4cc8e7fc271539a0d759f0a6"
}
```

### Body

```json
{
  "name": "product 23",
  "_class": "Dry Food",
  "price": 220,
  "status": "available",
  "image": "https://images.unsplash.com/photo-1598799170815-933217492614",
  "variant": [
    "7308afe2-fbfd-46b6-9aac-4094a83be4ee",
    "d4279a15-d500-42ce-8a77-e0d6111a7295",
    "de74699d-1249-4dda-82f0-e14f3e219cb6"
  ]
}
```

###### output

### possible response list:

1. HTTP_202_ACCEPTED ----- success
2. HTTP_404_NOT_FOUND ----- ID not found
3. HTTP_400_BAD_REQUEST ----- Required fields not given

```json
{
  "success": true
}
```

### HTTP REQUEST :  **DELETE /product/<str:id>**

###### params

### Authorization

```json
{
  "Authorization": "Token de363096afea5f8a4cc8e7fc271539a0d759f0a6"
}
```

###### output

### possible response list:

1. HTTP_204_NO_CONTENT ----- success
2. HTTP_404_NOT_FOUND ----- ID not found

```json
{
  "success": true
}
```

### HTTP REQUEST :  **GET /product/<str:id>**

###### params

### Authorization

```json
{
  "Authorization": "Token de363096afea5f8a4cc8e7fc271539a0d759f0a6"
}
```

###### output

### possible response list:

1. HTTP_200_OK ----- success
2. HTTP_404_NOT_FOUND ----- ID not found

```json
{
  "id": "cb9054ab-7797-4bab-b89e-e125fda03e95",
  "name": "product 23",
  "_class": "Dry Food",
  "price": 300.0,
  "image": "https://images.unsplash.com/photo-1598799170815-933217492614",
  "status": "available",
  "variant": [
    {
      "id": "7308afe2-fbfd-46b6-9aac-4094a83be4ee",
      "title": "Anchor",
      "availableStock": 60
    },
    {
      "id": "d4279a15-d500-42ce-8a77-e0d6111a7295",
      "title": "Nestle",
      "availableStock": 90
    },
    {
      "id": "de74699d-1249-4dda-82f0-e14f3e219cb6",
      "title": "Cadbury",
      "availableStock": 20
    }
  ]
}
```

### HTTP REQUEST :  **GET /search-product?search=unavailable**

###### params

### Authorization

```json
{
  "Authorization": "Token de363096afea5f8a4cc8e7fc271539a0d759f0a6"
}
```

###### output

### possible response list:

1. HTTP_200_OK ----- success

```json
{
  "data": [
    {
      "id": "dcbf9b3c-367a-4525-964c-615ee9d11111",
      "name": "product 23",
      "_class": "Dry Food",
      "price": 220.0,
      "image": "https://images.unsplash.com/photo-1598799170815-933217492614",
      "status": "unavailable",
      "variant": [
        {
          "id": "7308afe2-fbfd-46b6-9aac-4094a83be4ee",
          "title": "Anchor",
          "availableStock": 60
        },
        {
          "id": "d4279a15-d500-42ce-8a77-e0d6111a7295",
          "title": "Nestle",
          "availableStock": 90
        },
        {
          "id": "de74699d-1249-4dda-82f0-e14f3e219cb6",
          "title": "Cadbury",
          "availableStock": 20
        }
      ]
    }
  ]
}
```
