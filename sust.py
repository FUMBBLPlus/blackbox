import random

def sustainability(TV_1, TV_2, games_1, games_2, *,
    factor = 0.5,
    repeat_oppo = False,
    amplification = True,
    verbose = False,
  ):
  TV_min = min(TV_1, TV_2)
  TV_max = max(TV_1, TV_2)
  dTV_0 = 1000 * (TV_max / TV_min - 1)

  if verbose:
    print(f'dTV_0 = {dTV_0}')

  if amplification and 50 < dTV_0:
      dTV = dTV_0 * 3 - 100
  else:
      dTV = dTV_0

  if verbose:
    print(f'dTV = {dTV}')

  p_0 = 1 / (10**(dTV / 700) + 1)

  if verbose:
    print(f'p_0 = {p_0}')

  if verbose:
    print(f'factor = {factor}')

  p = p_0**(5**(1-2*factor))

  if verbose:
    print(f'p = {p}')

  d_0 = 0.5 - p

  if verbose:
    print(f'd_0 = {d_0}')

  d = (d_0 + random.uniform(0, 0.02)) / 0.52

  if verbose:
    print(f'd = {d}')

  S_0 = 1000 * d

  if verbose:
    print(f'S_0 = {S_0}')

  r_opp = (0.9 if repeat_oppo else 1)

  if verbose:
    print(f'r_opp = {r_opp}')

  if min(games_1, games_2) < 15 and 15 <= max(games_1, games_2):
      r_games = (min(games_1, games_2) + 1) / 15
  else:
      r_games = 1

  if verbose:
    print(f'r_games = {r_games}')

  S = S_0 * r_opp * r_games

  if verbose:
    print(f'S = {S}')

  return S


if __name__ == '__main__':
  import sys
  args = sys.argv[1:]
  if not args:
    print('USAGE: sust.py TV_1 TV_2 [games_1] [games_2]')
    sys.exit(1)
  if len(args) not in {2, 4}:
    print('ERROR: expected 2 or 4 parameters')
    sys.exit(2)
  try:
    args = [int(x) for x in args]
  except ValueError:
    print('ERROR: all parameters must be integers')
    sys.exit(3)
  TV_1, TV_2 = args[:2]
  if 4 <= len(args):
    games_1, games_2 = args[2:4]
  else:
    games_1, games_2 = 15, 15
  sustainability(TV_1, TV_2, games_1, games_2, verbose=True)
