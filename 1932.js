// https://www.acmicpc.net/problem/1932

const [_N, ...rawInputs] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(_N);
const triangle = [[0], ...rawInputs.map((line) => line.split(' ').map((s) => Number(s)))];

const table = Array.from(Array(N + 1), () => Array(N).fill(0));

table[1][0] = triangle[1][0];
for (let i = 2; i < N + 1; i++) {
  table[i][0] = table[i - 1][0] + triangle[i][0];
  for (let j = 1; j < i - 1; j++) {
    table[i][j] = Math.max(table[i - 1][j - 1], table[i - 1][j]) + triangle[i][j];
  }
  table[i][i - 1] = table[i - 1][i - 2] + triangle[i][i - 1];
}

console.log(Math.max(...table[N]));
