/*
  keyword_info.js -- Router for the JavaScript keyword info
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

router.get('/keyword',
  isLoggedIn,
  (req,res,next) => {
    res.render('keyword');
  }
)

router.post('/keyword',
  isLoggedIn,
  async (req, res, next) => {
    res.locals.keyword = req.body.keyword;
    const prompt = "What does the " + req.body.keyword + " keyword do in JavaScript?"
    const completion = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: prompt,
      max_tokens: 1024
    });
    res.locals.answer = completion.data.choices[0].text;
    console.log(completion.data);
    res.render('keywordInfo');
  }
)

module.exports = router;
