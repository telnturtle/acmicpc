// https://www.acmicpc.net/problem/1520

// input

const [_MN, ..._rows] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [M, N] = _MN.split(' ').map((s) => Number(s));

const m = _rows.map((row) => row.split(' ').map((s) => Number(s)));

// backtracking and memoization

const table = Array.from(Array(M), () => Array(N).fill(0));

const touched = Array.from(Array(M), () => Array(N).fill(false));

function f(i, j) {
  if (i + 1 === M && j + 1 === N) {
    return 1;
  }

  if (touched[i][j]) {
    return table[i][j];
  }
  touched[i][j] = true;

  let [inext, jnext] = [i - 1, j];
  if (inMap(inext, jnext) && gt(i, j, inext, jnext)) {
    table[i][j] += f(inext, jnext);
  }
  [inext, jnext] = [i + 1, j];
  if (inMap(inext, jnext) && gt(i, j, inext, jnext)) {
    table[i][j] += f(inext, jnext);
  }
  [inext, jnext] = [i, j - 1];
  if (inMap(inext, jnext) && gt(i, j, inext, jnext)) {
    table[i][j] += f(inext, jnext);
  }
  [inext, jnext] = [i, j + 1];
  if (inMap(inext, jnext) && gt(i, j, inext, jnext)) {
    table[i][j] += f(inext, jnext);
  }

  return table[i][j];
}

function inMap(i, j) {
  return 0 <= i && i < M && 0 <= j && j < N;
}

function gt(i, j, inext, jnext) {
  return m[i][j] > m[inext][jnext];
}

f(0, 0);

// // test output

// for (let i of table) {
//   console.log(i);
// }

// output

console.log(table[0][0]);
