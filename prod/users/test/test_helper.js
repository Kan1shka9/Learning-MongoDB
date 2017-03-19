const mongoose = require('mongoose');

// Use the ES6 implementation of the Promise
mongoose.Promise = global.Promise;

mongoose.connect('mongodb://localhost/users_test');
mongoose.connection
  .once('open', () => console.log('Good to go!'))
  .on('error', (error) => {
    console.warn('Warning', error);
  });

beforeEach((done) => {
  mongoose.connection.collections.users.drop(() => {
    // Ready to run the next test!
    done();
  });
});
