from pyspark import SparkContext

sc = SparkContext('local')

words = sc.textFile("/usr/share/dict/words")
print(words.filter(lambda w: w.startswith("spar")).take(5))
print(words)


