# Zillow Regression Project

### In a deluge of data, which drop(s) are driving single-unit property values for Zillow.com?

Using the property data from those whose last transaction was between 1May and 30Jun of 2017 (the 'Hot Months'), I attempt to predict the value of single-unit properties based on tax district assessments.

Also, because property taxes are assessed at the county level, I need to know where (state and county) the sample pools are located, as well as the distribution of the tax rates for each county.  

## Objectives:
- Planning, acquiring, preparing, and exploring the data in the provided Zillow MySQL database to gain an understanding of which variables are independent from each other and which are not.

- Model trial-and-error: modeling all these variables against and with each other to determine which factors have the heaviest weights in determining single-unit property values.  Being that there are multiple features and a single target (home value), multiple univariate regression modeling will be the focus of this portion.

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

Most of the dataframe coding and visualizations have been done using Jupyter Notebooks, an awesome and easy-to-use development environment, especially for people like me who tend to think out loud.  In the notebooks are comments that range from snippet to tome - the decision to keep them in there is to show my thinking process throughout each phase of the project.

Imports and this README file are rooted in VSCode.  Previous python-ing had been performed in PyCharm in preparation for this course and Jupyter Notebooks during this course, so when perusing my code in VS, one may find some noob-like stylings. 

But, hey: as long as the functions work, right?

## Minimum Viable Product

At the very least, we are to use our modeling to predict single-unit property values using only three factors: the number of bedrooms, the number of bathrooms, and the overall square footage.  From this spec, I will attempt to reject the following three null-hypotheses:

**Number of Bedrooms**

- $H_0$ - The number of bedrooms is not a driver of single-unit property values.

- ($H_a$ - The number of bedrooms IS a driver of single-unit property values)

**Number of Bathrooms**

- $H_0$ - The number of bathrooms is not a driver of single-unit property values

- ($H_a$ - The number of bathrooms IS a driver of single_unit properties)

**Square Footage**

- $H_0$ - Square footage does not drive single-unit property values

- ($H_a$ - Square footage DOES INDEED drive singe-unit property values)

### Tending to null values in the dataset

Initial exploration of the data revealed some null values in the features 'square_feet' and 'tax_amount.'  It is not believed that these 25 values will have any significant affect on the projection of the remaining non-null variables (totaling 15,011), so these rows will be dropped altogether from our analysis.  

# Glossary of Terms

Several features in the provided data needed some clarification for me.  While not exhaustive, this is the segment in which I hope to keep track of their definitions:

**fips number / code**
- short for Federal Information Processing Standard
- it's a unique identifier for US counties / county equivalents
- composed of five numbers: first two are the state code, and the last three digits are the county code
- our database lists them as four-number codes; this is due to the first number being the placeholder zero(0)
(Source: https://en.wikipedia.org/wiki/FIPS_county_code)

**Recursive Feature Elimination**

A method of removing features of low importance to reduce model complexity and overfitting.  Not every feature (independent variable, or X value) is as important to the model as the next, and this method of 'feature herd thinning' iterates through the model, selecting the attributes that best predict the target variable (the y, or 'home_value', in this case).