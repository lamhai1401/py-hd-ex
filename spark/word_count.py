from pyspark import SparkContext

def main():
    sc = SparkContext(appName='SparkWordCount', master='local[*]')

    input_file = sc.textFile('resources/input.txt')
    counts = input_file.flatMap(lambda line: line.split()) \
                    .map(lambda word: (word, 1)) \
                    .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile('./output')

    sc.stop()

if __name__ == '__main__':
    main()

# spark-submit --master local ./spark/word_count.py
