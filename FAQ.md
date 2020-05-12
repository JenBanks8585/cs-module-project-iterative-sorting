# FAQ

## Contents

### Complexity/Big-O

* [How do you assess space complexity?](#q100)


### General

* [Should we use a language's built-in functionality as much as possible?](#q300)
* [What are the tradeoffs with in-place versus non-in-place sorting solutions?](#q400)

## Questions

<a name="q100"></a>
### How do you assess space complexity?

Generally speaking, at work and in interviews, people are more interested in
time complexity. That said, _space complexity_, or how much additional space is
required to process _n_ elements of data, is also very important.

Space complexity does _not_ include the space required to hold the data you are
going to process. It only includes the _additional_ space requirements of your
algorithm.

Here's an example with `O(1)` space requirements:

```python
def alg(data):
    result = 0

    for v in data:
        result += v

    return result
```

Clearly the _time_ complexity is `O(n)`. As list `data` grows, the time it takes
to complete the algorithm grows proportionately.

But the _space_ complexity is `O(1)`. The additional space required to complete
the algorithm was:

* `result`: `O(1)`
* `v`: `O(1)`

And neither of those change in size regardless of how big list `data` is. `data`
could have a zillion elements, and the algorithm would still only require space
for `result` and `v`.

What about this:

```python
def alg(data):
    new_data = data.copy()   # <-- Added this line

    result = 0

    for v in new_data:
        result += v

    return result
```

Here we have more space allocated.

* `result`: `O(1)`
* `v`: `O(1)`
* `new_data`: `O(n)`

`new_data` gets bigger as `data` gets bigger, so it's `O(n)`. So we have:

`O(1) + O(1) + O(n)` space requirements. `O(n)` dominates, so the final result
is `O(n)`.

Where things get really tricky is when you have a recursive call. Each call to
the function allocates space for all the local variables.

And it gets doubly tricky if you're making a copy of the data each call, like
with a slice.

Here's the same algorithm as before that adds all the elements in a list, except
this one does it recursively. Recall that the initial iterative version was
`O(1)` space complexity.

```python
def alg(data):
    if data == []:
        return 0

    first_val = data[0]

    return first_val + alg(data[1:])
```

Every time we make a call into `alg()`, we get new space for local variables. So
any local variable that was `O(1)` on its own, now gets _n_ copies and becomes
`O(1*n)` or `O(n)`.

But that's not all. When we slice `data` on the recursive call, we get a new
list. So that means every call we're getting another copy of the list, and each
copy is `O(n)` space as well. And we're making _n_ recursive calls, so we need
_n_ copies of `O(n)` space, which comes to `O(n*n)` or `O(n^2)` space.

> Sure, it's not a _complete_ copy of the list. It's missing the first element.
> So each call has a shorter and shorter list, like:
>
> ```python
> [ 1, 2, 3, 4 ]
> [ 2, 3, 4 ]
> [ 3, 4 ]
> [ 4 ]
> [ ]
> ```
>
> So that means the first call wasn't really `O(n)`, but was more like
> `O(0.8*n)`, and the second was `O(0.6*n)`, and so on.
>
> But recall that we drop constants with Big-O, so those still just become
> `O(n)`.

So we have _n_ recursive calls.

`first_val` on its own is `O(1)`. But we recurse _n_ times, so it becomes
`O(1*n)` or just `O(n)`.

Each slice of `data` on its own is `O(n)`. But we recurse _n_ times, so it
becomes `O(n*n)` or `O(n^2)`.

So the total space complexity for this algorithm is:

`O(n) + O(n^2)`. The `O(n^2)` dominates, so the final space complexity is just
`O(n^2)`.

Again, compare to the `O(1)` space complexity of the initial iterative solution.

In some languages, notably
[Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)) and other
[functional programming
languages](https://en.wikipedia.org/wiki/Functional_programming), you can write
recursive solutions with `O(1)` space complexity. These languages take advantage
of a feature known as [_tail call
optimization_](https://en.wikipedia.org/wiki/Tail_call) to make this possible.
By coding things correctly, the language can automatically convert your
recursive solution into an iterative solution. Stock C and Python do not support
tail call optimization.

--------------------------------------------------------------------------

<a name="q300"></a>
### Should we use a language's built-in functionality as much as possible?

Yes.

Generally the built-in functionality is better tested and better optimized than
something you could write.

That said, there might be times you want to write your own versions. Maybe the
built-in doesn't do exactly what you need. Or maybe you want to rewrite the
built-in as a learning exercise, for example.

--------------------------------------------------------------------------

<a name="q400"></a>
### What are the tradeoffs with in-place versus non-in-place sorting solutions?

Memory: in-place typically takes less memory since you're reusing the original
storage for the list to hold the finally sorted list. If you allocate more lists
to hold the result, that takes more memory.

Code clarity: in-place sometimes has more complex code making the algorithm
harder to understand.

As an example, here's a non-in-place Quicksort, which seems to be generally
clearer than the in-place variant, but uses far more memory:

```python
def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right

def quicksort(data):
    if data == []:
        return data

    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)
```