// https://www.acmicpc.net/problem/9251

const [S, S1] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [L, L1] = [S.length, S1.length];

const table = Array.from(Array(L + 1), () => Array(L1 + 1).fill(0));

for (let i = 0; i < L + 1; i++) {
  table[i][0] = 0;
}
for (let j = 0; j < L + 1; j++) {
  table[0][j] = 0;
}
for (let i = 1; i < L + 1; i++) {
  for (let j = 1; j < L1 + 1; j++) {
    const [c, c1] = [S[i - 1], S1[j - 1]];
    if (c === c1) {
      table[i][j] = Math.max(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1] + 1);
    } else {
      table[i][j] = Math.max(table[i - 1][j], table[i][j - 1]);
    }
  }
}

console.log(table[L][L1]);
