# oth2
Online Treasure Hunt Revamped


React Google/Facebook Login -> accessToken that is valid only for 3600 seconds and then we get a new token -> Django Social Oauth Server Verifies the token and fetches details from Facebook Oauth Server -> Saves the details in sessions and sends the details everytime with the requests 


POST : http://localhost:8080/auth/convert-token -> to save the user to the database and save the accessToken received 
GET : http://localhost:8080/route-to-your-view/ -> Headers : Bearer <access-token-recieved> -> to authenticate everytime
