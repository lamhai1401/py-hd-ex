from snakebite.client import Client

client = Client('localhost', 9000)

# for x in client.ls(['/']):
#     print (x)

for result in client.mkdir(['/input'], create_parent=True):
    print (result)

# for f in client.copyToLocal(['/input/input.txt'], '/tmp'):
#     print (f)

# for l in client.text(['/input/input.txt']):
#     print (l)


# $HADOOP_HOME/sbin/start-dfs.sh
