# CarTrawler Code Assessment

This is my repo containing the code for the API assessment. I attempted to do this assignment in javascript ([can be seen in this repo](https://github.com/CoogyEoin/cartrawler_javascript_attempt))but the asynchrounous nature of the language caused too many difficulties for me so I decided to switch to using python on the third day and managed to get a working application. This lead to some shortcomings which I will discuss in the "nice to haves" section.


## Overview

This is an API application that runs on localhost port 8080. It has a single endpoint called /cars that takes a "method" keyword parameter in the request body. This endpoint calls the example CarTrawler API (https://www.cartrawler.com/ctabe/cars.json) and performs various actions on the data depending on the method specified. The valid methods are listed below.

* test: Simply returns a string saying "This is a test".
* remove_duplicates: Returns a list of cars with duplicate car models removed.
* call_endpoint: Calls the example cartrawler API and returns an unaltered JSON response.
* get_cheapest_of_each_car: Returns a list of cars with the cheapest of each model present in case of duplicates.
* filter_cdar_cars: Returns a list of cars with the vehicles containing the CDAR code filtered out.
* get_corporate_cars: Returns a list of all cars in the AVIS and ALAMO vendor groups.
* sort_low_to_high_by_group: Returns a JSON object of each group with their cars sorted from price low to high.


## Building and Setting up Application

To build and run the python API all you need to do is clone the git repo and run the main.py script. This is done with the below commands.

    git clone git@github.com:CoogyEoin/cartrawler_assessment.git
    cd cartrawler_assessment
    python main.py

To observe the results of the API calls you can use postman or run curl in another terminal like the below command. The method value in the data section should be changed according to which function you would like to call.

    curl --header "Content-Type: application/json" --request GET --data '{"method": "sort_low_to_high_by_group"}' http://localhost:8080/cars


## Code Overview

The repo itself contains a number of modules and handlers to account for the necessary functionality. The design of the application and modules was done to account for additional endpoints/methods to be added to the API.

The valid methods that can be called by the endpoint are defined in the handlers/api_handler module. It is a JSON object that maps the method keywords to their respective functions. This was done to make the structure of the API human readable and to account for additional functions to be added in the future for this endpoint or for other teams.

The ResponseHandler class was written to be re-usable for other applications. Although it essentially just calls the request library it is good to be able to handle exceptions and not having to write exception handling every time a request is made in the code.

The cars module is where the actual functionality lies in this application. I considered making the call_endpoint function private as it's being called by the customer-facing methods but I decided that there could be a business case for this being in the API as other teams may want to write their own processing functions.


## Nice to haves

As mentioned in the introduction I was under some slight time restraints as I decided to switch to doing the assignment in Python instead of javascript. There were a number of things I would have preferred to finish but I decided against it as I didn't want to go over the deadline.

* The functionality in the cars module could deal with some significant refactoring as they aren't the most efficient methods often using multiple for loops and if statements.

* I really would have preffered to finish this in javascript as I know it's the primary language used at CarTrawler but it has been a while since I worked with it and I was having issues processing the request data.

* I would have liked to have created a docker file to be able to run this in a container application. I may attempt to do this if I have a chance so keep an eye out for additional commits.
 
