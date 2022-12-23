// https://www.acmicpc.net/problem/1790

// input

const [_NK] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = _NK.split(' ').map((s) => Number(s));

// implementation

const ntok = {
  // 10: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(10),
  // 100: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(100),
  // 1000: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(1000),
  // 1000: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(1000),
  // 10000: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(10000),
  // 100000: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(100000),
  // 1000000: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(1000000),
  // 1000000000: ((v) => Array(v).reduce((acc, cur, idx) => acc + ntonofd(_), 0))(1000000000),
};

function f() {
  switch (true) {
    case N < 10:
      return N < K ? -1 : K;

    case N < 10:
      return;

    default:
      break;
  }
}

console.log(ntok);

// aux
/** Number -> Number of digits */
function ntonofd(n) {
  return Math.floor(Math.log10(n)) + 1;
}

function ntolofs(n) {
  switch (true) {
    case n < 10:
      return n;
    case n < 100:
      return 9 + 2 * (n - 9);
    case n < 1000:
      return 9 + 2 * 90 + 3 * (n - 99);
    case n < 1000:
      return 9 + 2 * 90 + 3 * 900 + 4 * (n - 999);
    case n < 10000:
      return 9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * (n - 9999);
    case n < 100000:
      return 9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * (n - 99999);
    case n < 1000000:
      return 9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * 900000 + 7 * (n - 999999);
    case n < 10000000:
      return 9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * 900000 + 7 * 9000000 + 8 * (n - 9999999);
    case n === 100000000:
      return 9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * 900000 + 7 * 9000000 + 8 * 90000000 + 9;
  }
}
