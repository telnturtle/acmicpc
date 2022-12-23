// https://www.acmicpc.net/problem/11054

// input

const [_N, _A] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(_N);
/** The sequence */
const s = [-Infinity, ..._A.split(' ').map((s) => Number(s)), Infinity];

// DP

const tablei = Array.from(Array(N + 2), () => Array(N + 2).fill(0));
const tabled = Array.from(Array(N + 2), () => Array(N + 2).fill(0));
const table = Array.from(Array(N + 2));

for (let j = N; j >= 1; j -= 1) {
  for (let i = 0; i <= j - 1; i += 1) {
    const keep = 1 + tablei[j][j + 1];
    const skip = tablei[i][j + 1];
    if (s[i] >= s[j]) {
      tablei[i][j] = skip;
    } else {
      tablei[i][j] = Math.max(keep, skip);
    }
  }
}
for (let j = 1; j <= N; j += 1) {
  for (let i = N + 1; i >= j + 1; i -= 1) {
    console.log({ i, j });
    const keep = 1 + tabled[j][j - 1];
    const skip = tabled[i][j - 1];
    if (i === 0 && j === 10) {
      console.log(tabled[0]);
    }
    if (s[i] <= s[j]) {
      tabled[i][j] = skip;
    } else {
      tabled[i][j] = Math.max(keep, skip);
    }
  }
}

// tablei.forEach((row) => console.log(row));
// console.log();
// tabled.forEach((row) => console.log(row));
console.log('\n\n');
for (let i of tablei) {
  let s = '';
  for (let j = 0; j <= N + 1; j++) {
    s += `${i[j]} `;
  }
  console.log(s);
}
console.log('\n\n');
for (let i of tabled) {
  let s = '';
  for (let j = 0; j <= N + 1; j++) {
    s += `${i[j]} `;
  }
  console.log(s);
}

for (let i = 1; i <= N; i++) {
  table[i] = tablei[i][i + 1] + tabled[i][i - 1] + 1;
}

console.log('\n\n');
console.log(table);
