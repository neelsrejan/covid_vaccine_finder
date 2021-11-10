# Covid Vaccine Finder

## Background info
This project was created early on in 2021 when https://vaccinefinder.org/search/ was the default website to find vaccines near you, now the website is https://www.vaccines.gov/search/ and the code has not been updated to reflect changes in the new website. Nonetheless, the issue with the original website is that it would only show the top 50 results of a location regadless of distance. I live in 95035 and if I set my distance to 10 miles I would get 50 results, likewise if I set the disance to 50 miles I would also only get 50 results and a majority of them are places where no vaccine was present so I would miss out on tons of places that show vaccine availablity.

## Methodology
To counter this problem, you enter your zipcode and a distance the program the finds all the zipcodes within a radius of your choice, and for each zipcode, selenium inputs the new zipcode into the website, searches, scrapess the data, and returns the data into an csv whth only results of locations that claim vaccine availability. Through this I was able to find a location giving a vaccine 36 miles away from me in a zipcode I didn't know about and wouldnt have come across since the website would only give the top 50 results and nothing more even if the distance was within the programs said capabiliities. 
