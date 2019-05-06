import tensorflow as tf
from tensorflow.python.platform import gfile
import os

def load_pb_to_log(filename):
    with tf.Session() as sess:
        with gfile.FastGFile(filename, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            g_in = tf.import_graph_def(graph_def)
    LOGDIR = f'{filename}_log'
    train_writer = tf.summary.FileWriter(LOGDIR)
    train_writer.add_graph(sess.graph)

def main():
    for filename in os.listdir('Model'):
        fname, fext = os.path.splitext(filename)
        if fext == '.pb':
            load_pb_to_log(f'Model/{filename}')

if __name__ == "__main__":
    main()