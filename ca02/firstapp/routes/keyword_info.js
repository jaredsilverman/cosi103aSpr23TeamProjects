/*
  movie.js -- Router for the movie finder
*/
const express = require('express');
const router = express.Router();

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

router.get('/movie',
    isLoggedIn,
    (req,res,next) => {
    res.render('movie');
   })
module.exports = router;
