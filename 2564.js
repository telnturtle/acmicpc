// https://www.acmicpc.net/problem/2564

// input

const [_IJ, _N, ..._STORES_AND_POS] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [J, I] = _IJ.split(' ').map((s) => Number(s));

const N = Number(_N);

/** The stores */
const STORES = _STORES_AND_POS.slice(0, -1).map((store) => store.split(' ').map((s) => Number(s)));

/** The position */
const POS = _STORES_AND_POS[_STORES_AND_POS.length - 1].split(' ').map((s) => Number(s));

// implement

const SUM = STORES.reduce((acc, store) => acc + dist(store, POS), 0);

// output

console.log(SUM);

// aux

function dist(p0, p1) {
  switch (true) {
    case dir(p0) === dir(p1):
      return Math.abs(coor(p0) - coor(p1));
    case dir(p0) === 1 && dir(p1) === 3:
      return coor(p0) + coor(p1);
    case dir(p0) === 3 && dir(p1) === 2:
      return I - coor(p0) + coor(p1);
    case dir(p0) === 2 && dir(p1) === 4:
      return J - coor(p0) + I - coor(p1);
    case dir(p0) === 4 && dir(p1) === 1:
      return coor(p0) + J - coor(p1);
    case dir(p1) === 1 && dir(p0) === 3:
      return coor(p1) + coor(p0);
    case dir(p1) === 3 && dir(p0) === 2:
      return I - coor(p1) + coor(p0);
    case dir(p1) === 2 && dir(p0) === 4:
      return J - coor(p1) + I - coor(p0);
    case dir(p1) === 4 && dir(p0) === 1:
      return coor(p1) + J - coor(p0);
    case isNS(p0) && isNS(p1):
      return Math.min(coor(p0) + coor(p1), 2 * J - coor(p0) - coor(p1)) + I;
    default: // !isNS(p0) && !isNS(p1):
      return Math.min(coor(p0) + coor(p1), 2 * I - coor(p0) - coor(p1)) + J;
  }
}

function dir([direction]) {
  return direction;
}

function coor([_, coor]) {
  return coor;
}

function isNS([direction]) {
  return direction <= 2;
}

// function xy([direction, coor]) {
//   return isNS(direction) ? [coor, 0] : [0, coor];
// }

// function x([direction, coor]) {
//   return isNS(direction) ? coor : 0;
// }

// function y([direction, coor]) {
//   return isNS(direction) ? coor : 0;
// }
