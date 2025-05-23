# 🖼️ ASCII Art

Un script Python simple pour convertir une image en **ASCII Art** et l'enregistrer dans un fichier `.txt`. Utilise **Pillow** pour l’image et **NumPy** pour un traitement efficace des pixels.

---

## ⚙️ Dépendances

* [Pillow](https://python-pillow.org/)
* [NumPy](https://numpy.org/)

Installe-les avec :

```bash
pip install pillow numpy
```

---

## 🚀 Utilisation

```python
image_to_ascii("ascii.jpg", "ascii.txt", width=1000)
```

Cette ligne est la n°29 voici comment la modifier :
* `image_path` : chemin de l’image d’entrée.
* `output_txt` : nom du fichier texte de sortie (par défaut : `ascii_image.txt`).
* `width` : largeur de l’image en caractères (par défaut : 500).

---

## 🧠 Fonctionnement

* L’image est convertie en **niveaux de gris** (`L` mode).
* Elle est redimensionnée avec un ratio respecté pour un rendu lisible.
* Chaque pixel est **mappé à un caractère ASCII** selon sa luminosité.
* Le tout est sauvegardé dans un fichier `.txt`.

---

## 📌 Exemple

### Entrée

![](exemple.jpg)

### Sortie (`output.txt`)

```
@@@@@@@@@@###########%%%%%%%######*****oooooo
@@@@@@######********ooooooooaaaaahhhhhhhkkkkk
....
```

---

## 📄 Licence

MIT – Fais-en ce que tu veux, mais cite l’auteur si tu le redistribues.
