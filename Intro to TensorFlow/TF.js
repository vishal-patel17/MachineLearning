const shape = [2,3]; // rows, columns
const a = tf.tensor([1.0,2.0,3.0,10.0,20.0,30.0], shape);
const b = tf.tensor2d([[1.0,2.0,3.0],[10.0,20.0,30.0]]);
// a.print();
// b.print();
zeros = tf.zeros(shape);
// zeros.print();
ones = tf.ones(shape);
// ones.print();

// varialbes:
 const initialValues = tf.zeros([5]);
 const biases = tf.variable(initialValues);
 biases.print();
 // document.getElementById("output").value = biases;

 const updatedValues = tf.tensor1d([0,1,2,3,4]);
 biases.assign(updatedValues);
 console.log("Updated values:");
 biases.print();
 // document.write(biases);

 // Ops on tensors:
 const sq = biases.square();
 sq.print();

 c = a.add(b); // sub, mul
 c.print();

 sq_sum = tf.square(tf.add(a,b));
 console.log("sq_sum: ")
 sq_sum.print();