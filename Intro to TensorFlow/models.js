// const a = tf.scalar(3.14).print();
function predit(input)
{
    return tf.tidy(() => {
        const x = tf.scalar(input);
        const ax2 = a.mul(x.square()); 
        const bx = b.mul(x);
        const y = ax2.add(bx).add(c);

        return y;
    })
}

// ax^2 + bx + c
const a = tf.scalar(2);
const b = tf.scalar(4);
const c = tf.scalar(8);

const result = predit(2).print();
// a.dispose();