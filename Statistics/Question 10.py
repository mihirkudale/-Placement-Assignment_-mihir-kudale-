Q-10. A factory produces light bulbs, and the probability of a bulb being defective is 0.05.
The factory produces a large batch of 500 light bulbs.
a. What is the probability that exactly 20 bulbs are defective?
b. What is the probability that at least 10 bulbs are defective?
c. What is the probability that at max 15 bulbs are defective?
d. On average, how many defective bulbs would you expect in a batch of 500?

Ans: a. Probability that exactly 20 bulbs are defective:

P(X = 20) = (500C20) * (0.05)^20 * (1 - 0.05)^(500 - 20)

Using a calculator or statistical software, we find:

P(X = 20) ≈ 0.029312827

b. Probability that at least 10 bulbs are defective:

P(X ≥ 10) = P(X = 10) + P(X = 11) + ... + P(X = 500)

Calculating this sum directly can be time-consuming, so we can use the complement rule:

P(X ≥ 10) = 1 - P(X < 10)

P(X < 10) = P(X = 0) + P(X = 1) + ... + P(X = 9)

Using a calculator or statistical software, we find:

P(X ≥ 10) ≈ 0.999984024

c. Probability that at most 15 bulbs are defective:

P(X ≤ 15) = P(X = 0) + P(X = 1) + ... + P(X = 15)

Using a calculator or statistical software, we find:

P(X ≤ 15) ≈ 0.9999999999999997

d. Expected number of defective bulbs in a batch of 500:

μ = n * p

μ = 500 * 0.05

μ = 25

Therefore, on average, you would expect 25 defective bulbs in a batch of 500.