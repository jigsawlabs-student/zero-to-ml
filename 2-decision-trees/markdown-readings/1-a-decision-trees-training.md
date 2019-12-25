### Introduction

In the last lesson, we learned about decision trees. And saw that decision trees essentially provide us with a series of tests to determine if our data falls into one category or another. In this lesson, we'll see how to start with a dataset and, from there, construct a decision tree. Our technique will be the following.

To predict whether our data will fall into one group or another, we find a characteristic that most separates our data into those different groups. Then, we find the characteristic that most separates our remaining data. When we are done separating all of our data, we have a mechanism to predict what will occur with future data. Let's see this by way of example.

### Our Data

Once again, we have the following data about our customer leads.

| Attended College | Under Thirty | Borough   | Income | Customer |
| ---------------- | ------------ | --------- | ------ | :------: |
| ?                | Yes          | Manhattan | < 55   |    0     |
| Yes              | Yes          | Brooklyn  | < 55   |    0     |
| ?                | No           | Brooklyn  | < 55   |    1     |
| No               | No           | Queens    | > 55   |    1     |
| ?                | No           | Queens    | < 55   |    1     |
| Yes              | No           | Queens    | >55    |    0     |
| Yes              | No           | Queens    | >55    |    0     |
| Yes              | Yes          | Manhattan | >55    |    0     |

Once again, we use the data to predict whether or not a lead will be a customer. Just like always, we have the "answers" for this data, which tell ius if our past leads became a customer. That information is in the customer column. The number 1 means that the lead became a customer, and 0 means they did not. 

The rest of our columns are the features of the data we'll use to predict whether someone becomes a customer.

#### Our Procedure

We'll predict whether someone will be come a customer by looking at the characteristics that most distinguished customers from non-customers. So we'll use a series of tests. For the above observations we can ask questions like:

* Does the lead have a graduate level of education? 
* Is the lead under thirty? 
* Is the lead from Manhattan? 
* Or from Brooklyn? 
* Is the lead's income over 55k?

The responses to these tests can help us predict whether or not someone will become a customer. If we see that that everyone under thirty is a customer, then we might be able to use this to predict how future leads will turn out. Once we choose one test that best separates our data, we'll then look at the rest of the data that was not separated, and find the test that best separates this remaining data.

 Let's summarize our procedure.

```
Given a subset of data
For each feature in our dataset
	○ Split the data according to the feature
	○ Compute consistency of data in each split 
Choose the feature with the highest consistency to split the data
Repeat for remaining subset
```

Let's try it out on the data to see how it works. Let's go.

