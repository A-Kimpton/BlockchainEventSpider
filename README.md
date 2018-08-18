# BlockchainEventSpider
A really simple spider to pull info from a web page.

This was a small project to experiment on using the google sheets api and webscraping. Do to the limitations of the frequency I can write to the sheets, im shelving this project.

If you want to use this application, you'll need to obtain a client_secret.json from the google dev console, and dump it in "ROOT/data/client_secret.json". I also hard coded the name of the sheet I was working with 'Data' - so you'll need to change that for your sheet.

# TODO

It can be easily expanded on:
 - I suggest you look at meetup.py to understand how to extend the WebScraper class. I designed it so that you only need to define what info you want from the page, and what to trigger when the page content has changed.
 - I also sugest you change the url lib dependancy for a better way to obtain the html. Some sites don't like that agent.
 - I also put the web scraping in a background thread, but you might want to put reach scaper in its own process or thread for faster loading.
 - If you can figure out how to write alot of data to the sheets with a singlew call, the function you need to look at is: ScaperHandler._write_to_doc()
 - Change the print statements for the built in logger
 - Currently I ping every site once each loop, once each loop is over, I try again. There is no delay other than the time it takes to look at each other page. You might want to change that.
 
 # Notes
 
You want to extend the WebScraper class because it has the functionality to pull info from the page, and calls the right functions when WebScraper.run() is executed. You should only worry about the 2 functions you need to override. You can see my example of Meetup - which is how I scrap from meetup.com
 
Current output:
![alt text](https://media.discordapp.net/attachments/475254258216861696/480450780965371905/e2fc125062bde51e75b766bd0c0d4982.png)
![alt_text](https://i.gyazo.com/47221eb4d772da2c651c753002ed12d0.png)

