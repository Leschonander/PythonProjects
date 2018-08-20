# Singer JumpBike D.C Tap

So their is this open source python project called [Singer](https://www.singer.io/) that is designed to create open source ETL's. 
ETL stands for Extract, Transform and Load and honestly I did not know that till today. 

To understand more what a ETL is and what use is a Tap I created one for the Jump Bike D.C [API](https://dc.jumpmobility.com/opendata). This one grabs information from the free bike status JSON feed with the normal use case being to dump it into a CSV file. 

If you wanted to run it, one would have to do the following:

```python
pip install singer
# Then do the following pip install below to throw the data into a CSV file.
pip install target-csv
```
After that assuming you downloaded the file somewhere you would excute the following command.
`python jumpBikeTap.py | target-csv `

After that a CSV sheet with data from the api is created.

While a nice start, need to work on the following things:

1. Limit the amount of records dump to the length of the feed.
2. Better format for the CSV file.
3. Erm, understand the point of a data tap 🤔🤔🤔

Other then that, for other transit + data obessed people, go nuts 🙌 .