with open("twentytwo.txt", "r") as read:
  secrets = list(map(int, read.read().split("\n")))

MOD = 16777216

def next(secret):
  secret = (secret ^ (secret * 64)) % MOD
  secret = (secret ^ (secret // 32)) % MOD
  secret = (secret ^ (secret * 2048)) % MOD
  return secret

def one():
  total = 0
  for secret in secrets:
    for _ in range(2000):
      secret = next(secret)
    total += secret
  print(total)

def two():
  seqs = {}
  for secret in secrets:
    seen = set()
    seq = []
    prev = secret % 10
    for _ in range(2000):
      secret = next(secret)
      seq.append((secret % 10 - prev))
      prev = secret % 10
      if len(seq) == 4:
        seqt = tuple(seq)
        if seqt not in seen:
          seen.add(seqt)
          seqs[seqt] = seqs.get(seqt, 0) + prev
        seq.pop(0)
  print(max(seqs.values()))

one()
two()