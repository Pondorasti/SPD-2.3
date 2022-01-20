# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

Pizza creation route throws a server error accompanied by a stack trace

```
TypeError: 'topping' is an invalid keyword argument for PizzaTopping
```

Taking a **trace backward** approach.

Looks like the error is coming from `app.py`, line 79, in `pizza_order_submit` route.

`PizzaTopping` initializer is using wrong property name (`topping` instead of `topping_type`). Fixed that, new error! Taking a look at `pizza_size_str` variable, it's null! HTML form input name is not matching, renamed it! Same problem with `order_name`... Noticed how db data is not commited after beind added, fixed that too! Fixed `PizzaTopping` array creation. Final bug fix, change `redirect(url_for('/'))` to `redirect(url_for('home'))`.

## Exercise 2

[[Your answer goes here!]]

## Exercise 3

[[Your answer goes here!]]
