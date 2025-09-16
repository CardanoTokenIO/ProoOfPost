# The DANZO ARENA

![DANZO ARENA](../images/arena1.webp)

**[Join the Arena now](https://danzo.gg/#/arena)**

DANZO ARENA is a decentralized application running on Cardano. The goal of the arena is to add an extra layer of complexity to DANZO, gamify it, promote DANZO trading, and introduce a new memecoin standard: the MEMEFI standard.

## Arena Explanation Video

{% embed url="https://www.youtube.com/watch?v=K7rvNyAEKHk" %}

## How does the DANZO ARENA work?

The DANZO ARENA is exclusive to DANZO holders. Holders deposit their tokens and receive the appropriate amount of $HODLDANZO, which allows them to swap back to DANZO when they withdraw.

After the deposit, the tokens are added to the DANZO ARENA TVL together with other players' tokens. There is a standard withdrawal fee equal to 10% of the deposit. Of this fee, 8% is split among all the other players still in the game, and 2% is burned forever.

## What is the goal of the participant?

The goal of the participants is to hold their ARENA position longer than others so they can collect DANZO from early exits and withdraw without the withdrawal fee affecting them, as the collected fees cover the cost of exit.

Besides the basic function of the DANZO ARENA, DANZO ARENA participants also have the option to BORROW DANZO up to 30% of their ARENA POSITION with a fixed interest rate and loan duration.

Collateral for these loans is the amount of DANZO deposited plus the profits from people exiting the arena. This ensures a healthy and safe borrow-to-collateral ratio since we are operating with the same pair. Price fluctuations do not matter, and liquidation only occurs when the loan duration expires.

This gives the ability to DANZO ARENA participants to either short DANZO if they dare, take advantage of LP farming etc.

## Why would we give the ability to DANZO ARENA participants to short?

It's simple: more fun, increased trading volume, and with MINSWAP V2 coming up, we will be able to split trading volume fees among DANZO ARENA participants, as our LP tokens are locked with ADAORCA and not burned.

## What happens when someone fails to repay their loan before the loan period ends?

In this scenario, they keep the 30% they borrowed from their DANZO ARENA position, and the remaining 70% is split among the arena participants. The fee is equivalent to an exit of 10 times the position!

## The math behind the HodlCoin Game:

The game's state is a pair (R, S) where:

• R is the number of coins in the reserve,

• S is the supply of hodlCoins.

The price of a hodlCoin is: P(R, S) = R/ S

The user can perform 2 actions:

1) **hodl**: The user deposits n coins into the game's reserve, and the game mints and gives the user n / P (R,S) hodlCoins.

2) **un-hodl**: The user gives back n hodlCoins to the game, and the game burns them and gives the user n(1 − Φ)P(R, S) coins, where Φ is a fee such that 0 < Φ < 1.

The game is assumed to be initialized with R = 1 and S = 1 and the un-hodl action is disallowed if it would result in S = 0. This guarantees that P(R, S) is initially equal to 1 and is always well-defined.

## THEOREMS

**Theorem 1 (Never-Decreasing Price).** The price of hodlCoins never decreases: for any sequence of actions a1, . . . , ak, Pk ≥ P0, where P0 and Pk are the prices, respectively, before and after the sequence of actions.

**Proof.** Proof by induction:

Base case (to prove Pk ≥ P0 when k = 0): In this case, Pk = P0, trivially

Induction case (to prove that Pk+1 ≥ P0, assuming, by induction hypothesis, that Pk ≥ P0. Let Rk and Sk be R and S after action ak. Proof by case analysis:

![Arena Math](../images/arena2.webp)

## Discussion

The hodlCoin game can be seen as a dual of a Ponzi scheme. Whereas in a Ponzi scheme investors who enter earlier are paid with money from investors who enter later, in the hodlCoin game players who exit later are paid with money from players who exit earlier. Furthermore, whereas a ponzi scheme fools investors who are unaware of the scheme's operations, the hodlCoin game is fully transparent, its rules are clear and players are aware of them. Finally, whereas a Ponzi scheme is unstable and invariably leads to collapse, hodlCoin is conjectured to enjoy a self-stabilizing effect: if the price of the underlying asset is falling and players start to un-hodl to sell the underlying asset, this may encourage other players to hodl to benefit from the fees paid by those who are un-hodling; this may reduce the selling pressure on the underlying asset.

![Arena Concept](../images/arena3.webp)
