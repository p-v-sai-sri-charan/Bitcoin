Bitcoin price Notifier
Need Mongodb

install requirements: 
pip install python 3
pip install pymongo

Procedure:

This code will connect to CoinMarketcap through API and get the Bitcoin data every hour
Those prices will be notified to the user using IFTTT and Telegram
To get these notification we will be using IFTTT it makes us to link between the two different platform/application  user at an ease. It works on a principal that if this then that so go to IFTTT/create click on the this and select Webhooks to receive a Post request and click on the that and select the notification to get the notification on mobile through IFTTT Application. And similarly click on the this and select Webhooks to receive a Post request and click on the that and select the Telegram(rich telegram updates) to get the bitcoin prices on mobile through telegram bot.  
For every hour you will be getting the telegram updates AND the data is stored in mongo db
If it touches the threshold value emergency IFTTT web app notification will be sent to the user


Youtube links:   https://youtu.be/DMvUhhrQAqQ
                  
                  https://youtu.be/l0wTVyoSTpQ


