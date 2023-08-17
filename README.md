# Link Shortener App


## Approach

I started out by researching how link shortening services such as bit.ly generally work, and how I can contextualize the problem as a microservice implementation. Since microservices are intended to be deployed independently of others, I decided to limit the scope to just the link-shortening functionality and assume that we have a working database and redirecting service that would complete the overall objective of providing shortened urls.

The microservice will expose a RESTful API that takes a long URL as input and returns a shortened URL. The API will be written using Flask, a lightweight framework for writing RESTful APIs in Python. 

A simple UI will allow a QA tester to input long urls and receive the shortened url from the API. The UI will be as simple and lightweight as possible, using vanilla javascript and html. 


## Assumptions

I assume that we have a working database that can store Links with code, long url, and short url entries. I also assume that we have a domain pa.ni and a microservice that uses the database to make redirects. We are also assuming that security is out of scope for this technical exercise. 


## Decision making and problem solving

I considered using express.js or Django, but decided to use Flask because it's what I know, and its a good fit for the simple microservice task. I wanted the microservice to be as simple as possible so that it's easily maintainable and reliable, as well as scalable using docker. Decided on using an MVC (Model View Controller) structure that allows for seperation of concerns with controllers, routes, services, config, and models as well as the main app.py. This also allows for testing of each component. The layout is also easy to understand for onboarding new members.

Flask blueprints allow us to organize our API by encapsulating functionality. This allows separation of concerns as we are making the API more modular. 
For generating the short urls, I decided to use hashlib. This is the most straightforward way to convert a long url into a hash, then use base64 encoding to turn the hash into an alphanumeric string which we can shorten to whatever length we decide. Added a default value of 8 for ~218 trillion different possible values using alphanumeric characters.



I did run into CORS issues when writing the javascript UI, reviewed CORS policies for flask and used the flask-cors for a development fix. Added a note that allowed origins need to be specified in production.



