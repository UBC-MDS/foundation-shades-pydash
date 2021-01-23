## Milestone 2 Reflection: Foundation Shades Across the Globe

### 1. What we have implemented

We have implement all 3 sections outlined in our Milestone 1 proposal, which include:

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

* Interactive radio button for users to select an individual country and visualize different best-selling brands through the `Best Selling Brands by Country` histogram;

* Interactive sliders for users to input their own unique HSV values and see the top 5 most matching results from our `Best Selling Foundation Lists`.

### 4. What are the limitations

The limitations of our dashboard include:

* Relatively small dataset with limited brand categories:
  
  * The dataset used to build our app has merely 349 observations, which fall into 26 different brand categories across 4 different countries (US, Nigeria, Japan, and India).
  
  * This means that our dataset by nature could not fully represent all the brands and products of foundations.
  
  * Additionally, when users are filtering by country (e.g. filtering by Nigeria), the distribution of Lightness presented may not be fully representative of the entire foundation market of a country.
  
* Dash specific limitations:

  * When we tried to display different foundation shades/colours on Dash, the colour matching and displaying was particularly hard to implement. This is due to the fact that Dash doesn't have a built-in function support for displaying colours. We had to implement this feature manually with functions from other packages; which is inconvenient, time-consuming, and difficult to reproduce.
  
  * It is very difficult to change style of the app sliders, in particular the padding space between the `Hue`, `Saturation`, and `Value` headers and the sliders underneath. This detracts from the aesthetic pleasantness of our app.

### 5. What are potential improvements & additions

If we had more time in the future, we have a couple of potential additions in mind:

* We would like to try to include other cosmetic products, including but not limited to lipstick colors, eyeshadow colors, in addition to our current foundation shades.
  
  * With the addition of other cosmetic products, our app could become more useful, powerful, and dynamic for our target users (i.e. global cosmetic marketing and consulting companies). The additional makeup product would allow our target users to get a fuller view on the cosmetic products market as a whole.
  
  * Ideally, we would have toggles on the sidebar of the app for users to switch between different makeup products.

* We would also like to use a larger dataset of foundations, with data from more shades, brands, and countries. This would allow for our app to be more representative of the entire foundation market, and not just a segment of it.