Proposal: shades of foundation offered by a variety of beauty brands
around the world
================

# Section 1: Motivation and Purpose

**Our role**: Data scientist consultancy firm

**Target audience**: Global cosmetic marketing and consulting companies

Makeup foundation usually comes in many different shades, contributed by
factors such as hue, saturation, brightness, and lightness levels. Each
beauty brand also has its own distribution of makeup foundation products
that have the different shades to meet customer demands. If we could
understand which beauty brands and their foundation products that meet
the specific shades requirements, it could be helpful for cosmetic
marketing and consulting companies to make informed decisions.

To address this objective, we propose building a data visualization
dashboard that allows our target audience to visually and interactively
explore a dataset of makeup foundation shades by different global beauty
products from different brands. Our dashboard will show the distribution
of foundation products by shades and allow users to explore different
aspects of this data by filtering and re-ordering on different variables
such as brands, hue, and saturation in order to compare factors that
contribute to different foundation shades.

# Section 2: Description of the [data](https://github.com/the-pudding/data/tree/master/makeup-shades)

We will be visualizing a dataset of 625 observations. Each observation
has 8 associated relevant variables that describe a particular
foundation `product` from a particular `brand` with a particular shade
(represented as `hex` which stands for *hexadecimal color code* in the
dataset), which has associated hue `H`, saturation `S`, brightness `V`,
and lightness `L` numerical values, and has associated product `group`
(of 7 categories - *0: Fenty Beauty’s PRO FILT’R Foundation Only*; *1:
Make Up For Ever’s Ultra HD Foundation Only*; *2: US Best Sellers*; *3:
BIPOC-recommended Brands with BIPOC Founders*; *4: BIPOC-recommended
Brands with White Founders*; *5: Nigerian Best Sellers*; *6: Japanese
Best Sellers*; *7: Indian Best Sellers*).

# Section 3: Research questions and usage scenarios

Our project answers the broad research question of: “What is the range
and distribution of makeup foundations shades offered by each of the
best-selling cosmetics brands across the globe”. Our broad research
question can be further split into the 3 sub-questions specified below:

  - RQ1. What shades do best-selling foundation products of each country
    offer?  
  - RQ2. What brands are part of the best-selling foundation products in
    each country?
  - RQ3. What is the distribution of foundation shades offered by the
    best-selling brands in each country?

Below we have provided a usage scenario of our product by a member of
our intended target audience:

Beth is a consultant at a well-known global cosmetics marketing and
consulting company. As part of her job, Beth advises large cosmetics
companies on new product launches and strategies needed for entering new
international markets.

Beth is working closely with a client who is planning the launch a
makeup foundation product across the globe. Beth needs to understand her
client’s competitors across the globe. She also need to understand what
shades of foundation products her client’s competitors are offering as
well as the distribution of shades they are offering in each of the
global markets. This would allow Beth to advise her clients to design a
shade range that meets the needs of each of the markets they are
entering and to stock their products for each market appropriately.

When Beth uses the “Foundation Shades Across the Globe App”, she will
see the specific shades of global best-selling foundations and their
distribution on a lightness scale. Beth will be able to filter this
dataset by specific regions (e.g. US, Japan or Nigeria), or by specific
brands (e.g. L’Oreal or Maybelline) to view the shades of foundation
offered. She will further be able to see what brands are offered in each
of the regions to see who her client’s competitors are in each market.
Finally, she is able to view the distribution of shades on a lightness
scale for each region, to see if her clients need to focus on a
particular region of the shade spectrum when entering a specific market.

With the insight gained from this app, Beth advises her clients to offer
a wide range of shades in the US market as all her client’s competitors
are offering 20+ shades in the US market. She also notices a market
entry opportunity in India as most of her client’s competitors in India
offer a limited shade range that is skewed towards lighter tones. She
advises her clients to offer an expanded shade range in India and launch
a culturally-sensitive yet progressive marketing campaign on embracing
your natural skin tone by wearing an appropriately matched foundation
shade. Her clients are impressed by her data-driven insights.