
# Part 2: Paula breaks production

## What's the problem?

After pushing a new change Paula has broken production. :/

## So what happened?

- Paula was installing a new security monitoring package 
- Turns out, this package, allowed remote access into the company network
- Italian Hackers entered the network and created some fake surveys
- The Italians created fake surveys in **pairs** 
  - For each pair the `name` fields on the survey are **Semordnilaps** of each other
  - Eg. for survey1 the `name` could be `dog` and survey2 would be `god`
  - Or `maps` and `spam`


## The Task

1. Given a list of surveys of size `N`, return a list of tuples, containing the two `tx_id`s for each pair of fake Italian surveys.
2. Each survey object has the attributes
   - `tx_id`
   - `name`
3. A pair of surveys is considered to be fake, if there exists another survey in the list, who's name backwards is equal to the name of the survey (A Semordnilaps).


## Examples

Consider the simple list with three surveys...
```python
list = [
  {
    "tx_id": 123,
    "name": "xxffllo"
  },
  {
    "tx_id": 456,
    "name": "random"
  },
  {
    "tx_id": 789,
    "name": "ollffxx"
  }
]

```

The output should be `[(123, 789)]` as the names for the first and last items are each other backwards (Semordnilaps).

### Notes

- Names are unique, i.e no two names will be equal to each other
- If no fake survey pairs are found, return an empty list
