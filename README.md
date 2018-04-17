# justcling_api
Its a simple api which can fetch and update data in api.

If you want to fetch data the url is-:(its a get request)

/api/v1/user/info/<user_id>/
(user_id is an integer -: it represent which user details you want to be printed)

If you want to update the gender of a user -:(its a post request)

/api/v1/user/gender/<user_id>/
and in params pass gender=male, female or other


Things used to make the api-:

Django restframework
Database-:Postgres
