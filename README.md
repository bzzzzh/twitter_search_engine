# CS172 Final project
- Yuteng Zhang	
- SID: 862017519

- Bohan Zhang
- SID: 861215636

- Dishon Jordan
- SID: 862083504

# Introduction
This is a small search engine for Twitter. 
<br/>In Part 1, we build a crawler (from scratch) to collect tweets from the Twitter Streaming API
<br/>In Part 2, we use an opensource tool called ElasticSearch along with the Kibana console to index all the collected tweets.
<br/>In Part 3, we propose and implement an extension of the search engine created in Parts 1 & 2. We chose to build
an interactive interface for the user using flask python.
<br/>
<br/>Since C++ is not allowed, We chose to use python to write this assignment.
<br/>The submission contains a python file elastic.py to run the search engine, along with the templates folder containing the simple frontend html file and the twitter_stream file containing the json data file and a python file twitter_stream.py for crawling data. 


# Part 1
To run this program, first clone the project and open to its root directory:
```
$ git clone https://github.com/CS-UCR/final-project-solid.git
$ cd final-project-solid
```

To install the library:
```
$ pip3 install tweepy
$ pip3 install lxml
```

To run the crawler:
```
$ python3 twitter_stream.py
```
The program could be terminated by pressing CTRL + C while running
<br/>After the termination, all the data crawled so far will be stored in a json file in the same directory with twitter_stream.py
<br/>
<br/>
Collaboration Details:
<br/>This part was developed by Dishon Jordan. 
<br/>

# Part 2
To import data into ElasticSearch, we chose to use the Kibana console.
<br/>First download ElasticSearch and unzip:
```
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.0-darwin-x86_64.tar.gz
$ tar -xvf elasticsearch-7.5.0-darwin-x86_64.tar.gz
```

Then download Kibana and unzip:
```
$ curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.5.0-darwin-x86_64.tar.gz
$ tar -xvf kibana-7.5.0-darwin-x86_64.tar.gz
```

Run ElasticSearch and Kibana:
```
$ ./elasticsearch-7.5.0/bin/elasticsearch
$ ./kibana-7.5.0-darwin-x86_64/bin/kibana
```

<br/>Go to your localhost:5601/, if both ElasticSearch and Kibana runs successfully, should be able to see a page like this:
<br/>Click on the "upload data from log file" button
![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/a.png?raw=true)

<br/><br/>Next, select the data file you wish to import
![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/b.png?raw=true)

<br/><br/>You will see your file contents and a short summary, check if it's correct and hit import
![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/c.png?raw=true)

<br/><br/>The final step is to enter the index name you wish to give to your data
![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/d.png?raw=true)

<br/>Wait for it finishes, and after that goto the ElasticSearch port localhost:9200/the_index_name_you_entered/, to see your data
![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/e.png?raw=true)

<br/>
<br/>


# Part 3
We build our web frontend interface using flask python
<br/>To install the library:

```
$ pip3 install flask
$ pip3 install requests
```
To run the web app:
```
$ env FLASK_APP=elastic.py flask run
```
The app runs on localhost:5000/ by default. Below is the web app
![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/f.png?raw=true)

<br/>
<br/>This is a sample output result

![img](https://github.com/CS-UCR/final-project-solid/blob/master/img/g.png?raw=true)
