// https://www.acmicpc.net/problem/16926

// input

const [_NMR, ..._A] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M, R] = _NMR.split(' ').map((s) => Number(s));

/** The matrix */
const A = _A.map((row) => row.split(' ').map((s) => Number(s)));

const [NP, MP] = [N - 1, M - 1];

// implement

const B = Array.from(Array(N), () => Array(M));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    const dist = distanceToBorder(i, j);
    let ir = i;
    let jr = j;
    for (let k = 0; k < R; k++) {
      [ir, jr] = rotate(ir, jr, dist);
    }
    B[ir][jr] = A[i][j];
  }
}

// output

for (let row of B) {
  const s = row.join(' ');
  console.log(s);
}

// aux

function distanceToBorder(i, j) {
  return Math.min(NP - i, i, MP - j, j);
}

function rotate(i, j, dist) {
  const ip = i - dist;
  const jp = j - dist;
  const imax = NP - 2 * dist;
  const jmax = MP - 2 * dist;
  const [ipnext, jpnext] = _rotate(ip, jp, imax, jmax);
  return [ipnext + dist, jpnext + dist];
}

function _rotate(ip, jp, imax, jmax) {
  // edge case
  switch (true) {
    case imax === 0 && jp === 0:
      return [ip, jp + 1];
    case imax === 0:
      return [ip, jp - 1];
    case ip === 0 && jmax === 0:
      return [ip + 1, jp];
    case jmax === 0:
      return [ip - 1, jp];
  }
  // normal case
  switch (true) {
    case ip !== imax && jp === 0:
      // ip, jp = < imax, 0
      return [ip + 1, jp];
    case ip === imax && jp !== jmax:
      // ip, jp = imax, < jmax
      return [ip, jp + 1];
    case ip !== 0 && jp === jmax:
      // ip, jp = > 0, jmax
      return [ip - 1, jp];
    default:
      // ip, jp = 0, > 0
      return [ip, jp - 1];
  }
}
