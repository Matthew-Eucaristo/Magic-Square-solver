
# Magic Square Solver

Magic Square is an n x n array which all diagonal, horizontal and vertical axes sum up exactly the same.

This repository contains an implementation of a brute-force algorithm for solving the Magic Square problem. The current implementation generates all possible permutations of the numbers from 1 to `n*n` and checks if each permutation forms a valid magic square.

## Time Complexity

The time complexity of the current algorithm is `O((n*n)! * n^2)`, where `n` is the size of the magic square. This means that the algorithm's running time grows factorially with the size of the magic square.

## Contributions

We welcome contributions to this project! If you have ideas for improving the algorithm or adding new features, please feel free to submit a pull request or open an issue.

## License

[MIT](LICENSE)
