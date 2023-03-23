# Location Tracking:

Initially we looked into how to track location with each player in order to collect trash. The initial thought was to use the google maps api to be able to do real time location tracking, however we encountered the problem of:

• Needing a billing account in order to access data from google with the generated api key. This is a problem because the api key will be posted on github where people could use the key which is attached to our billing account and make requests which could cause the team to lose funds.
• Real-time tracking. The problem with this is that the geolocation api given by google must be refreshed every time you want to refresh your location which will send multiple requests and will only set your location at that time.

To overcome this we decided that it would be a good idea to create qr codes for each building where gamekeepers will be able to add certain trash to the designated location and the players will be able to pick up these trash items.
We have now created a test app for the qr codes where we have created python code to generate these qr codes for some buildings scattered around campus and display them to a website relating to the building.
