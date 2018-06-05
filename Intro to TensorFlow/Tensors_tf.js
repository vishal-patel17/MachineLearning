// a = tf.tensor([1,2,3,4], [2,2], 'float32').print(); // recommended using tf.tensor1d()

// a = tf.scalar(3.14, 'int32').print();

// a = tf.tensor3d([1,2,3,4,5,6], [2,3,1]).print();
// a.dispose();

// Buffers:
const buffer = tf.buffer([2,3]);
buffer.set(3,0,0);
buffer.set(5,1,0);
buffer.toTensor().print();

const x = tf.tensor([1,2]);
x.clone().print();

// Identity matrix:
const e = tf.eye(3).print();

const f = tf.fill([2,3], 1, 'bool').print();

const imgdata = new ImageData(1,1);
imgdata.data[0] = 100;
imgdata.data[1] = 150;
imgdata.data[2] = 200;
imgdata.data[3] = 250;

tf.fromPixels(imgdata).print();

tf.linspace(0, 9, 10).print();

const y = tf.onesLike(x).print();

const verbose = true;
tf.tensor2d([1,2,3,4], [2,2], 'int32').print(verbose); // default dtype: float32


