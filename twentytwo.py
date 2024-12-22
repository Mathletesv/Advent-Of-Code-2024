with open("twentytwo.txt", "r") as read:
  secrets = list(map(int, read.read().split("\n")))

def one():
  total = 0
  for secret in secrets:
    for i in range(2000):
      mix = secret * 64
      secret ^= mix
      secret %= 16777216
      mix = secret // 32
      secret ^= mix
      secret %= 16777216
      mix = secret * 2048
      secret ^= mix
      secret %= 16777216
    total += secret
  print(total)

def two():
  seqs = {}
  for secret in secrets:
    seen = set()
    seq = []
    prev = secret % 10
    for i in range(2000):
      mix = secret * 64
      secret ^= mix
      secret %= 16777216
      mix = secret // 32
      secret ^= mix
      secret %= 16777216
      mix = secret * 2048
      secret ^= mix
      secret %= 16777216
      seq.append((secret % 10 - prev))
      prev = secret % 10
      if len(seq) == 4:
        seqt = tuple(seq)
        if seqt not in seen:
          seen.add(seqt)
          if seqt not in seqs:
            seqs[seqt] = 0
          seqs[seqt] += prev
        seq = seq[1:]
  print(max(seqs.values()))

one()
two()