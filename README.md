# Link Shortener App

## Running the app

Simply run:

    docker compose up --build

## Testing the app

Run the full test suite:

    pytest

## Approach

To begin, I performed research on existing link shortening services such as bit.ly. I focused on transforming the challenge into a microservice implementation, enabling me to balance complexity and project scope effectively. To complete the exercise in a reasonable timeframe, I decided to limit the scope to just the link-shortening functionality and assumed that we had a working database and redirecting service that would complete the overall objective of providing shortened URLs. The deliverable is a link shortening service, that was the primary objective for me.

The microservice will expose a RESTful API that takes a long URL as input and returns a shortened URL. The API will be written using Flask, a lightweight framework for writing RESTful APIs in Python. Simple unit testing will also be implemented using pytest.

A simple UI allows a QA tester to input long URLs and receive the shortened URL from the API. The UI will be as simple and lightweight as possible, using Flask templates. 


## Assumptions

I assumed that we have a working database that can store links with code (the hashed n digit identifier), long URL, and short URL entries. I also assumed that we have a domain pa.ni and a microservice that uses the database to make redirects. Furthermore, I assumed that security concerns are out of scope for this technical exercise. I made these assumptions in order to complete the exercise in a reasonable time frame.


## Decision-making and problem-solving

I considered using Express.js or Django, but decided to use Flask because it's what I know, and it's a good fit for the simple microservice problem. I wanted the microservice to be as simple as possible so that it's easily maintainable and reliable, as well as scalable using docker. Flask is also easily scalable for smaller web applications such as this. A micro framework is a good choice for a microservice. An MVC (Model View Controller) structure allows for separation of concerns with controllers, routes, services, and models as well as the main app.py. The separation of concerns inherent in these patterns facilitates better maintainability and scalability. Further, implementing a redirect route and database access would be straightforward in this file structure by adding access to databases and business logic to services and a redirect route in routes. We can test each component separately. The layout is also easy to understand for onboarding new members.

Flask blueprints allow us to organize our API by encapsulating functionality. This allows separation of concerns as we are making the API more modular. 
For generating the short URLs, I decided to use hashlib. This is the most straightforward way to convert a long URL into a hash, and then use base64 encoding to turn the hash into an alphanumeric string which we can shorten to whatever length we decide. I decided to use a default value of 8 digits for ~218 trillion possible values using alphanumeric characters.

I ran into CORS issues when writing the JavaScript UI, reviewed CORS policies for flask and used the flask-cors package for a development fix. Added a note that allowed origins need to be specified in production. 



