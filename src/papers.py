# data from https://academicgraph.blob.core.windows.net/graph-2016-02-05/index.html

# The text file was loaded into hadoop file system
papers = sc.textFile("PaperReferences")
# This should display 3 lines, where the first element is "paper" and the second is "paper reference"
print papers.take(3)

# Here I'm just splitting each line into a tuple.
paperTuples = papers.map(lambda x: tuple(x.split()))
print paperTuples.take(5)

# Here I'm converting each line to the first element of the tuple and the number '1', in preparation for counting the degree.
paperRefs = paperTuples.map(lambda t: (t[0], 1))

citeCount = paperRefs.reduceByKey(lambda x,y: x+y)
# This takes way too long.
citeCount.take(5)
