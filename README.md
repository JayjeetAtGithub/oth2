# oth2
Online Treasure Hunt Revamped


React Google/Facebook Login -> accessToken that is valid only for 3600 seconds and then we get a new token -> Django Social Oauth Server Verifies the token and fetches details from Facebook Oauth Server -> Saves the details in sessions and sends the details everytime with the requests 