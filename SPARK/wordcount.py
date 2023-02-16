import sys
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

    # This gets the content of the file line by line. Each line becomes an element in an array
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    # Now we get an array or words
    counts = lines.flatMap(lambda x: x.split(' '))

    # Now we get an array of 2-tuples. Each tuple looks like (word, 1).
    counts = counts.map(lambda x: (x, 1))

    # Now we get an array of 2-tupes. Each tuple looks like (wrod, count_of_this_word).
    counts = counts.reduceByKey(add)

    output = counts.collect()

    print(output)

    spark.stop()
