
nomera = {
	"abrikos":3490, 
	"buka":2984, 
	"cub":3573, 
	"durka":9635
	}

def poisk(d: dict, item):
	value = d.get(item)
	if type(value) != int:
		value = "такого нету"
	return value

def zapis(d: dict, imya, nomer):
	if imya in d.keys():
		return "такой уже есть"
	else:
		d.update({imya: nomer})
		return "записано"

def udaleniye(d: dict, imya):
	try:
		nomer = d.pop(imya)
		return "удалено: " + imya + " " + str(nomer)
	except KeyError:
		return "такого нету"

print(udaleniye(nomera, "cu"))