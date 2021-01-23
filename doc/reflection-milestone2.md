## Milestone 2 Reflection: Foundation Shades Across the Globe

### 1. What we have implemented

We have implemented all the 3 sections we promised to implement from Milestone 1, which are:

1. `Best Seller Shades by Country` histogram;

2. `Best Selling Brands by Country` histogram;

3. `Finding the Top 5 Similar Foundations by HSV` section, with the top 5 matching results displayed in the same color as the foundation shades by Hue, Saturation, and Value/Brightness (HSV).

### 2. What we decided not to implement

We decided not to include the `country` filter under our `Finding the Top 5 Similar Foundations by HSV` section because:

* it could cause problems when there aren't many matching results, as some countries might not have that many matching shades of foundation, due to the nature of our rather small dataset;

* it could also cause problems when users don't select any country in the `country` filter. 

### 3. What we think our dashboard does well

Our current dashboard has included all the basic functionalities that we planned to have from Milestone 1, including the capabilities of:

* Interactive dropdown options for users to select multiple countries on the `Best Seller Shades by Country` histogram;

* Interactive radio items options for users to select on individual country and different brands on the `Best Selling Brands by Country` histogram;

* Interactive slider options for users to input their own unique and interested HSV values and see the top 5 most matching results from our `Best Selling Foundation Lists`.

### 4. What are the limitations

The limitations include:

* Relatively small dataset with limited brand categories:
  
  * The current dataset we used to build our app has only 349 observations, which fall into 26 different brand categories across 4 different countries (US, Nigeria, Japan, and India).
  
  * This means that our dataset by nature could not fully represent all the brands and products of foundations.
  
  * In addition, when users are filtering by country such as Nigeria, the Lightness shades of foundation products presented might not be fully representative of the whole Nigeria foundation market.   
  
  * As a result, our foundation shades color spectrum is also not wide and representative enough of the population foundation products. 
  
* Dash specific limitations:

  * When we tried to display different foundation shades color on Dash, the color matching and displaying part was particularly hard to implement as Dash doesn't have a build-in function for that, so we have to implement this manually with functions from other imports and packages, which was very inconvenient, time-consuming, and hard to reproduce.
  
  * It is very difficult to change style of the app sliders, in particular the padding space between the `Hue`, `Saturation`, and `Value` headers and the sliders underneath, which doesn't look the nicest.

### 5. What are potential improvements & additions

If we had more time in the future, we have a couple of potential additions in mind:

* We would like to try to include other cosmetic products, such as but not limited to lipstick colors, eyeshadow colors, in addition to our current foundation shades.
  
  * That way, our app could become more useful, powerful, and dynamic for our target users (global cosmetic marketing and consulting companies) to get a fuller view on not just the foundation markets, but also other cosmetic product markets.
  
  * Ideally, we would have toggles on the sidebar of the app for users to switch between different makeup products.

* We would also like to use a rather large dataset for our current foundation shades task, with more foundation shades, brands, and countries available, so that we could build an app that is representative of the entire foundation markets, and not just a few segments.