# Proposal: 
Project ω ඞ ω - Web-scraper 

Team Diamond Hands:
Christopher Dervan,
Paul Sullivan,
William Howell,
Xavier Naranjo

Our main research topic and project proposal revolves around building a web-scraper for a popular Ethereum Network block explorer website, www.etherscan.io. In order to successfully implement such a project, we will have to research several techniques relating to how we can utilize techniques to parse, garner, and classify useful data points from the site, how to implement triggers with the data we are effectively able to “scrape” from the site, and how we may analyze and process that data into useable forms (ideally initially parsing the data in an organized fashion and ultimately possibly even generating visual tools like graphs/charts for the data if we can successfully accumulate these data in such an organized way).  Three pertinent questions to our research are as follows:
1) How will we build a web-scraper?
A) To answer this question, we will have to reference a myriad of resources which will 		     likely revolve around online resources. One of our team members, Xavier, has already accumulated some research and code materials that should represent a starting point for us. Our group members have minimal experience with such a project, so answering this question effectively will be very important toward our ultimate success.
2) How do we classify, organize, and process the incoming data from the web-scraper?
A) Etherscan has a large and diverse collection of data relating to activity on the 			     Ethereum Network. This includes data such as timestamps of transactions, wallet addresses, price amount of assets, amount of various crypto (ERC tokens) held in wallets, as well as in which application the transaction was logged. Other data that could be collected could be volume data over time and gas fees among a slew of other Ethereum Network-related transactional data. That being said, this data merely being scraped without an organizational scheme would ultimately be a large, jumbled mess of random strings and numbers, so this classification endeavor will be tantamount toward our goal of obtaining useful data from Etherscan. We will have to do research from the aforementioned sources in order to find examples and ideas on how we may collect the data in an organized way or parse/classify the data effectively post-collection.
3) What can we do with the data?  
A) Such a diverse set of data offers a lot of opportunities as to how to use the data. 		     Depending on which data we can effectively harvest (whether it is a combination or one data set), we could possibly track “bad actors” (I.e. network users engaging Miner Extracted Value schemes like “Sandwich Attacks”), we could chart historical price action over time using linear or logarithmic formats, or even monitor the actions of wallets that hold large amounts of certain ERC tokens and create alerts based on their activity. The possibilities for answering this question essentially are only limited by our creativity and ability to devise strategies to implement the best or most practical ideas we have.
We will be harvesting this data using a web-scraper and will build it in the python programming language with some external libraries and APIs. This in turn will open a variety of options for the implementation of a web-scraper with real-world use cases. Additionally, our team members ultimately leaned toward this idea, despite having many other proposal options, as we felt the learning process involved could give us some versatile skills that may be employed for various other fun and interesting web-scraping endeavors, such as scraping popular social media sites like Reddit and 4chan for certain trends and topics.
