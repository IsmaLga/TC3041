var MongoClient = require('mongodb').MongoClient;
var http = require('http');
var express = require('express');
var cors = require('cors')
var url = 'mongodb://localhost:27017/elections_2018';

var app = express();
app.use(cors())

var str = '';

// retrieves candidate data
app.route('/candidates/:candidate').get(function(req, res) {
  var candidate = req.params.candidate;
  MongoClient.connect(url, function(err, db) {
    var dbo = db.db('elections_2018');
    var query = { username: '@' + candidate };
    dbo
      .collection('candidates')
      .find(query)
      .toArray(function(err, result) {
        if (err) throw err;
        res.send(result);
      });
    db.close();
  });
});

// retrieves candidate data
app.route('/dates').get(function(req, res) {
  var candidate = req.params.candidate;
  MongoClient.connect(url, function(err, db) {
    var dbo = db.db('elections_2018');
    dbo
      .collection('dates')
      .find()
      .toArray(function(err, result) {
        if (err) throw err;
        res.send(result);
      });
    db.close();
  });
});
// retrieves a candidate positives tweets
app.route('/candidates/:candidate/positive_tweets/').get(function(req, res) {
  var candidate = req.params.candidate;
  MongoClient.connect(url, function(err, db) {
    var dbo = db.db('elections_2018');
    var query = { username:'@' + candidate}
    dbo
      .collection('dates')
      .find()
      .toArray(function(err, result) {
        if (err) throw err;
        res.send(result);
      });
    db.close();
  });
});

// retrieves a candidate positives tweets for an specific date 
app.route('/candidates/:candidate/positive_tweets/:date').get(function(req, res) {
  var candidate = req.params.candidate;
  MongoClient.connect(url, function(err, db) {
    var dbo = db.db('elections_2018');
    dbo
      .collection('dates')
      .find()
      .toArray(function(err, result) {
        if (err) throw err;
        res.send(result);
      });
    db.close();
  });
});

var server = app.listen(3000, function() {});
