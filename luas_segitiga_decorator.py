def perbaiki_nilai(func):
  """Decorator"""
  def wrapper(alas, tinggi):
    if alas < 5:
      alas = 5
    if tinggi < 5:
      tinggi = 5
    return func(alas, tinggi)
  return wrapper

@perbaiki_nilai
def hitung_luas_segitiga(alas, tinggi):
  """Menghitung luas segitiga."""
  luas = 0.5 * alas * tinggi
  return luas

alas1 = 3
tinggi1 = 4
luas1 = hitung_luas_segitiga(alas1, tinggi1)
print(f"Luas segitiga dengan alas {alas1} dan tinggi {tinggi1} adalah {luas1}")

alas2 = 6
tinggi2 = 8
luas2 = hitung_luas_segitiga(alas2, tinggi2)
print(f"Luas segitiga dengan alas {alas2} dan tinggi {tinggi2} adalah {luas2}")