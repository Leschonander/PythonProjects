Data project being done with Jump Bikes open [API](https://dc.jumpmobility.com/opendata/free_bike_status.json).

Learned how to do the following:

1. Get better at wrangling data with Pandas, for example:
   * Turning a percentage dataframe that was a string into integers so they could be properly analyzed.
   * Converting dataframes with GeoJSON into GeoJSON is a intresting process.
   * More usage of `df.to_html` which is very nice for Pandas/Flask data projects. 
2. Got to do some more work in GeoJSON
3. Work with Mapbox, but do most of the gruntwork in Pandas on the server side. Nice fact is that this makes it easy to hide keys from the client.
4. `{{ data|safe }}` is required for transfering GeoJSON data from Flask backend to frontend to be used by Mapbox. 


[Image](https://pbs.twimg.com/media/Di-rdnjXoAUw0k8.jpg)
