var MongoClient = require('mongodb').MongoClient;
var http = require('http');
var express = require('express');
var url = 'mongodb://localhost:27017/elections_2018';

var app = express();

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
        str = result;
        console.log(str);
      });
    res.send(str);
    db.close();
  });
});

var server = app.listen(3000, function() {});
