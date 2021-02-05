## Milestone 4 Reflection: Foundation Shades Across the Globe

### 1. What we have implemented

We have successfully implemented all 3 sections outlined in our Milestone 1 proposal. Additionally, we have made the following changes to improve our product:
1. As per milestone 3 and peer feedback, we are using different colour-palletes for the two histograms.  
2. As per Chris's suggestion in milestone 3, we have decided to move away from an unfilled histogram to a filled histogram with lower saturation colour-pallete and a white background to reduce the color clutter.
3. We resolved some of the padding and spacing issues present in our R dashboard by reverting to the Python dashboard.
4. We have added a favicon to our website tab.

### 2. What we decided not to implement

We did not implement minor stylistic changes due to the limited time available for this project. The requested stylistic changes were mostly related to the default settings of Dash and Plotly. Joel advised our group that tuning some of these settings (e.g. changing default tooltip text color and adding mean and median values to the tooltip) are beyond the scope of this course.

We did not implement any features beyond those outlined in our Milestone 1 proposal due to time-constraints. Our decision to not implement additional features was also motivated by our belief that our dashboard is a useful and functional product for our target audience in its current form.

### 3. Reflection on Feedback Receieved 
#### 3a. Has it been easy to use your app?
We have received positive comments on the intuitive design on our app. We feel that our app is well-implemented and easy to use. Some of the features that contribute to its ease-of-use include:
1. Minimal lag when using dropdowns, radio-buttons and sliders.
2. Ability to resize and dynamicly interact with histograms. This is facilitated by our choice of using Plotly.
3. Clean layout.

#### 3b. Are there reoccurring themes in your feedback on what is good and what can be improved?
The feedback we received in all three milestones has been positive overall. There has been feedback regarding the clustered look of the two stacked histograms and we hope that our final changes have addressed this piece of feedback.  

#### 3c. Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?
It would have been useful to have the opportunity to solicit direct feedback from an expert working in the cosmetics marketing industry. In particular, we would like to ask if the slider functionality would be of value to them.  

### 4. Choice of Python over R
We decided to use Python for three reasons:
1. Dash is primarily designed as a Python library and has greater functionality and compatiblity with Python.
2. Dynamic re-scaling when filtering countries or brands on the legends of our Plotly histograms is not available in R.
3. We faced troubles while debugging in R as the error messages were uninformative.
