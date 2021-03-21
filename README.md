Submission for The 2nd H-Act 2021

## Inspiration
Our inspiration for the project came with wanting to learn how to create our own GUI application in addition to API calls and web scraping.

The software we decided to create had to meet the following criteria:
- Match the theme of the hackathon
- Create code that runs outside of a terminal
- Be fun to make

## What it does
Tweetify scans through Twitter and looks for popular artists that people talk about.

It then ranks the artists based on mentions and generates a Spotify playlist on the user's account.

## How we built it
The application is based on python, uses Tweepy to scan discord, Spoptipy to generate a playlist, and billboard.py to build a list of top 25 artists to query on twitter.

## Challenges we ran into
<ins>Data Scraping</ins>

We wanted to dynamically create our list based on mentions of music or artists, but we could not find a way to categorize a topic and determine the specific song or artist. Instead, what opted to do was generate a list of 25 top artists from the billboard top 100, and use that as the search key for incoming tweets. We will then only save the top 10 most mentioned artists of the 25 at the time.

<ins> Multithreading Application</ins>

We wanted to create an event-driven program, but we lack experience in multithreaded programming. Our application originally kept pausing when querying the data.

<ins> Team Coordination</ins>

As this is our first hackathon, team project, and python isn't our most used language, we had to download tools for everything. We figured out logistics on the fly, and slowly created a rhythm that was just right for the team.

## Accomplishments that we're proud of
- Using multiple APIs to create a single functionality
- Creating and user testing the application's GUI
- Creating a logo for the application

## What we learned
- API calls
- Multithreading
- Team software development

## What's next for Tweetify
- We would like to eventually sample data from other social media sources such as Reddit or Instagram to get broader statistics.

## NOTES
- Elements may not display properly when compiled on Mac
- TOKENS.py must be updated to your own tokens


