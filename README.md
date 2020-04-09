# Zillow Regression Project

### In a deluge of data, which drop(s) are driving single-unit property values for Zillow.com?

Using the property data from those whose last transaction was between 1May and 30Jun of 2017 (the 'Hot Months'), I attempt to predict the value of single-unit properties based on tax district assessments.

Also, because property taxes are assessed at the county level, I need to know where (state and county) the sample pools are located, as well as the distribution of the tax rates for each county.  

## Objectives:
- Planning, acquiring, preparing, and exploring the data in the provided Zillow MySQL database to gain an understanding of which variables are independent from each other and which are not.

- Model trial-and-error: modeling all these variables against and with each other to determine which factors have the heaviest weights in determining single-unit property values.

- From these efforts, create a Google Slide presentation of 3-5 slides clearly laying out the results of my findings to an audience of Data Scientists working for Zillow.  

### Backing up a bit:

I had originally done my whiteborading for the cached project, determining error drivers in the Zillow 'Zestimate' algorithm.

When I realized the project paradigm had changed, I became a little detached; a 'woe is me' moment, for sure.  

BUT hope was not lost: in my initial exploration of the Zestimate algorithm, I noticed a couple of things that seemed problematic and were almost certainly drivers of error.

One, the algorithm relies heavily on customer feedback and input.  That type of reliance seems to be rich with Type I and Type II errors.  The majority of people only go to Zillow for sales-related activities: "How much do I sell my home for / how much is that home 'really' worth?"  Motivation is a key factor in losing one's objectivity, so it would seem the feedback they receive would be fraught with 'he said / she said' data and customer complaints.  It's easy to envision a trend where the more feedback they got, the further buyer and seller data would diverge from each other.

Secondly, foreclosures are not factored into the algorithm, whereas variables like 'area home sale price' are.  Anyone who has driven through neighborhoods with a foreclosed property(properties) knows that property values surrounding those foreclosures are diminished, at least from a buyer's perspective.  Their reasoning for not including foreclosures is that they are outliers.  While that may be true under normal conditions, Zillow was founded in 2006 - two years before the tremendously non-normal condition of the 2008 housing crash.   An increase in foreclosures (say, for the city of Detroit) would push outliers closer to - and possibly within - the normal distribution curve.  

Once my Minimum Viable Product is satisfactory, I would like to explore possible feature engineering that includes these and other factors I discovered while looking into the cached project deliverables.

## Full disclosure on my process:

Naturally, the data science pipeline / workflow is implemented, but I'm a bit 'old-school' and need to touch and feel my information.  I have printed out the necessary modules for my own reference, as well as whiteboarded all objectives, complete with Post-It notes of various colors to physically keep track of my progress.

Most of the dataframe coding and visualizations have been done using Jupyter Notebooks, an awesome and easy-to-use (and nearly full-on) IDE.   Imports and this README file are rooted in VSCode.  In preparation for this Codeup course, I did all my work in either PyCharm or Kaggle, so when checking things in my VSCode, one may see some noob-like stylings.