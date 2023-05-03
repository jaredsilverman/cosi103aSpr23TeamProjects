/*
  movie.js -- Router for the movie finder
*/
const express = require('express');
const router = express.Router();
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);



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

router.post('/movie',
async (req,res,next) => {
     console.log('getting movie')
     res.locals.movie = req.body.movie
     res.locals.info = await get_info(req.body.movie)
     res.render('movieInfo')
})

const get_info = async (movie) => {
    const prompt = "What streaming services have the movie: "+movie;
    const completion = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: prompt,
        max_tokens: 1024
    });
    console.log(completion.data.choices[0].text);
    return (completion.data.choices[0].text)
  }


module.exports = router;
