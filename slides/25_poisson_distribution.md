# Poisson Distribution
* Poisson Phenomena
* Poisson PMF
* Relationship with Binomial


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# The Poisson Distribution

The Poisson Probability Distribution represents the number of events occuring in a given interval of time or space
* $\lambda$ represents the typical or expected frequency in a given interval

**Constraints:**
1. The rate represented by lambda is consistent
2. Each “success” or event is independent, discrete, and random
3. Two events cannot occur at the exact same instant


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# The Poisson Probability Mass Function (PMF)
* Given a typical frequency, $\lambda$, find the probability for a specific number of outcomes $k$
* $\lambda$ can be adapted to different sizes of interval
* The PMF provides the 

$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Poisson Example Problems

$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$

**Example 1**
On average, ten people visit the ATM in an hour. What is the probability that 12 people visit the ATM in an hour?

$\lambda = 10$
$k = 12$

$$
P(\lambda=10, k=12) = \frac{e^{-10} \cdot 10^{12}}{12!} = 0.0948
$$

Thus the probability of 12 people visiting the ATM in an hour is 0.0948.


**Example 2**
A specific space telescope takes random images of deep space. On average 23 Super Giant stars are seen in an image. What is the probability that two randomly selected images will have a total count of 35 Super Giant stars in them?

$\lambda = 23 * 2$
$k = 35$

$$
P(\lambda=46, k=35) = \frac{e^{-46} \cdot 46^{35}}{35!} = 0.01602
$$

Thus the probability of seeing 35 stars in two images is 0.01602.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `poisson_pmf()` function.
* $e = 2.71828$
* Note, both the constant `e` and the `factorial()` function are available from the `math` module.


$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
Code the `poisson_pmf()` function.
Note, both the constant `e` and the `factorial()` function are available from the `math` module.

$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


```python
from math import e, factorial

# print(e) # 2.718281828459045

def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Poisson's relationship to Binomial
**The binomial distribution tends toward the Poisson distribution as:**
$n \rightarrow \infty$
$p \rightarrow 0$
$\lambda = np$ stays constant

**Binomial PMF**

$$
P(X=k) = {n \choose k} p^k(1-p)^{n-k}
$$

The Mean, or Expectation in a Binomial distribution is $np$


**Poisson PMF**
$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$
The Mean of a Poisson distribution is $\lambda$


If we set $\lambda$ equal to $np$, we can see that $p=\frac{\lambda}{n}$: 

$$
\lambda = np \rightarrow p=\frac{\lambda}{n}
$$

and then substitue $\frac{\lambda}{n}$ for $p$ in the Binomial PMF:
$$
P(X=k) = {n \choose k} \frac{\lambda}{n}^k(1-\frac{\lambda}{n})^{n-k}
$$

We can take $n$ toward infinity now (which takes $p$ toward 0), and approach the result of the Poisson PMF.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Verifying Poisson's relationship to Binomial 
Try this with different values of $\lambda$ and $k$


```python
from math import e, factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)


# Let's start with an n of 1 and fix lmbda and k
lmbda = 10
k = 10

for n in range(k, 10000):
    print(f'binom: {round(binomial_pmf(n, k, p=(lmbda/n)),7)}')
    print(f'poiss: {round(poisson_pmf(lmbda, k),7)}')
    print()
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Euler's Number $e$
[Playlist describing Emergence of Euler's Number $e$](https://www.youtube.com/watch?v=Mw52nDwPh8k&list=PL5T50pwCrPUrIxYqP8jC8ctUUItW6csXG)

We can think of $e$ as a constant utilized in the Poisson PMF to describe a rate of decay, or the spreading out of successes over ever dividing moments tending toward $\infty$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)


**Phenomenon:**
Cars passing by an intersection at a certain time of day/year,  for the duration of a fixed amount of time, will likely follow a Poisson distribution

**Question:**
A given intersection will have, on avg, 15 cars pass through in 10 minutes. What is the probability that 20 cars pass through in 15 minutes?


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution


**Phenomenon:**
Cars passing by an intersection at a certain time of day/year,  for the duration of a fixed amount of time, will likely follow a Poisson distribution

**Question:**
A given intersection will have, on avg, 15 cars pass through in 10 minutes. What is the probability that 20 cars pass through in 15 minutes?

```python
lmbda = 15 * (15/10) # this can be a fraction
k = 20

print(poisson_pmf(lmbda, k)) # -> ~0.0769
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (5 minutes)
#### Code the `poisson_cdf` function


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
#### Code the `poisson_cdf` function

```python
def poisson_cdf(lmbda, k_high):
    cdf = 0.0

    for k in range(k_high+1):
        cdf += poisson_pmf(lmbda, k)

    return cdf
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)

A given intersection will have, on avg, 15 cars pass through in 10 minutes. What is the probability that
more than 15 cars will pass through in 15 minutes?


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

```python
lmbda = 15 * (15/10)

print(1 - poisson_cdf(lmbda, k_high=15)) # 0.9366
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (6 minutes)
#### Code the `poisson_pmf_dict()`
* your parameters will be 
    * `lmbda`
    * `low_k`
    * `high_k`

Holding `lmbda` constant, write a function that returns a dictionary showing the probs for number of events from `low_k` to `high_k` (inclusive)


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

```python
def poisson_pmf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lmbda, k)

    return d

d = poisson_pmf_dict(10, 0, 30)

for k, v in d.items():
    print(f'{k}: {round(v, 6)}')
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (2 minutes)

You are observing a phenomenon that follows perfectly a poisson process.

Given a certain number of observation (10000), how would you determine how many events to expect for each value of k given  `lmbda=10`, `low_k=0`, `high_k=30`?


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

Simply multiply each probability by the number of observations.

In code:

```python
def poisson_count_exp(lmbda, low_k, high_k, num_samples=10000):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = round(poisson_pmf(lmbda, k) * num_samples)

    return d

d = poisson_count_exp(10, 0, 30, num_samples=10000)

for k, v in d.items():
    print(f'{k}: {v}')
```
