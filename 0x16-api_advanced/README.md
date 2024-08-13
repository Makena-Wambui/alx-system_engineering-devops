THE AFTER PARAMETER
-----------------------
When you query an API like Reddit, you might not get all the results in one response.
Especially if they are many results.

Instead, you will get a portion of the results, eg the first 25 posts.. along with a token 'after' -> which tells the API where to start the next set of results.

To get more results, make another request to the same endpoint and include the after token from the previous response,
which tells the API to send the next batch of results.

