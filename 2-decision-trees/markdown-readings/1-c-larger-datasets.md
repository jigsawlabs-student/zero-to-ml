### Working with larger datasets

In the above example, we were able to use our features to perfectly segment our leads into customers and noncustomers. However, when we have larger datasets, we may not be able to accomplish this. 

So this causes a couple of issues: 

1. How can we count only the data in homogenous groups if no group is homogenous 

Because features may not split our data into homogenous groups, we use a different metric. Essentially, we penalize each feature for the amount of "disorder" in the group. So if the split results in ten customers and two non-customers, this split receives a lower penalty than a split that results in half customers and half non-customers. So the principle stays the same, we choose splits that best separates our data, we just don't require perfect separation.

2. How do we make predictions with data that is not perfectly homogenous

We may find that our leaf nodes also have a mix of target data. So there may be some customers and some non-customers when training our decision tree. How do we assign a label? Well we just use majority rule. If most of the training data that falls into the leaf node ends up being a customer, then that is the value we assign.

### Summary

In this lesson, we learned about training a decision trees. We saw that we can train our decision tree by creating various tests, and then prioritizing tests that best separate our data into homogenous groups. Then we saw that the end result is a hypothesis function as a decision tree which we can use to predict our data. We summarized our procedure for training a tree as the following.



```
Given a subset of data
For each feature in our dataset
	○ Split the data according to the feature
	○ Compute consistency of data in each split 
Choose the feature with the highest consistency to split the data
Repeat for remaining subset
```



