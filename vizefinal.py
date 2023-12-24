vize=float(input("vize notunuz"))
final=float(input("final notunuz"))

sonuc=((0.4*vize)+(0.6*final))


if sonuc<50 or final <50:
	print("kaldınız")
else:
	print("gectiniz ortalama:",sonuc)
