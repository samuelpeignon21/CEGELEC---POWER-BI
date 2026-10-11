# -*- coding: utf-8 -*-
"""Télécharge en LOCAL les images du site officiel cegelec.nc utilisées par la maquette.

Les logos et photos appartiennent à Cegelec / VINCI Energies : ils ne sont volontairement
pas inclus dans ce dépôt. Ce script les récupère sur le site officiel pour un usage local
(consultation de la maquette). Ne pas les republier sans accord de l'entreprise.

Usage :  python telecharger_assets.py
Pour recadrer les images à bandes blanches : pip install pillow (facultatif).
"""
import os
import shutil
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))

IMAGES = [
    ("assets/photos/ck2_caroussel.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/ck2_caroussel.jpg"),
    ("assets/photos/core-and-backbone.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/core-and-backbone.jpg"),
    ("assets/photos/focola_1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/focola_1.jpg"),
    ("assets/photos/focola_2.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/focola_2.jpg"),    ("assets/logo_cegelec.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/logo_entete_cegelec.jpg"),
    ("assets/officiel/105408359.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/105408359.jpg"),
    ("assets/officiel/106922831.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/106922831.jpg"),
    ("assets/officiel/1157999803.jpeg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/1157999803.jpeg"),
    ("assets/officiel/1307362408.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/1307362408.png"),
    ("assets/officiel/1634872398445-768x1024-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/1634872398445-768x1024-1.jpg"),
    ("assets/officiel/1737249268.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/1737249268.jpg"),
    ("assets/officiel/2092819312.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/2092819312.jpg"),
    ("assets/officiel/2365190285.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/2365190285.jpg"),
    ("assets/officiel/2785689624.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/2785689624.jpg"),
    ("assets/officiel/292626281.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/292626281.png"),
    ("assets/officiel/2930811143.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/2930811143.jpg"),
    ("assets/officiel/2949785025.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/2949785025.png"),
    ("assets/officiel/3224788864.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/3224788864.png"),
    ("assets/officiel/3768182803.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/3768182803.png"),
    ("assets/officiel/4137872684.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/4137872684.png"),
    ("assets/officiel/4269834471.jpeg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/4269834471.jpeg"),
    ("assets/officiel/4280860750.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/4280860750.jpg"),
    ("assets/officiel/4282327447.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/4282327447.jpg"),
    ("assets/officiel/526345763.png", "https://www.cegelec.nc/app/uploads/sites/394/2020/12/526345763.png"),
    ("assets/officiel/actemium_logo-e1611180030773-300x47-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/actemium_logo-e1611180030773-300x47-1.jpg"),
    ("assets/officiel/actemium-removebg-preview.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/actemium-removebg-preview.png"),
    ("assets/officiel/api_thumb_450-3.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2023/06/api_thumb_450-3.jpg"),
    ("assets/officiel/axians.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/axians.png"),
    ("assets/officiel/axians_1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/axians_1.jpg"),
    ("assets/officiel/axians_logo-e1611180087442.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/axians_logo-e1611180087442.jpg"),
    ("assets/officiel/axians_presnetation.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/axians_presnetation.png"),
    ("assets/officiel/bs_entreprise.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/bs_entreprise.jpg"),
    ("assets/officiel/bs_ilot_maitre-1024x576-1.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/bs_ilot_maitre-1024x576-1.png"),
    ("assets/officiel/carte_nouvelle-caledonie.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/carte_nouvelle-caledonie.png"),
    ("assets/officiel/cegelec_logo-1-e1608011795431-300x99-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/cegelec_logo-1-e1608011795431-300x99-1.jpg"),
    ("assets/officiel/cegelec-logo-2-1024x421-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/cegelec-logo-2-1024x421-1.jpg"),
    ("assets/officiel/centre-de-detention-1024x576-1.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/centre-de-detention-1024x576-1.png"),
    ("assets/officiel/dfgh-1024x768-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/dfgh-1024x768-1.jpg"),
    ("assets/officiel/fcbtp_logo-e1611181984995.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/fcbtp_logo-e1611181984995.png"),
    ("assets/officiel/frise_chronologique-e1611181339447.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/frise_chronologique-e1611181339447.png"),
    ("assets/officiel/IMG_2506.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/IMG_2506.jpg"),
    ("assets/officiel/lamedef_logo-e1611182072639.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/lamedef_logo-e1611182072639.jpg"),
    ("assets/officiel/logo_afbtp.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/logo_afbtp.jpg"),
    ("assets/officiel/logo_citeos-e1611178197790-300x73-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/logo_citeos-e1611178197790-300x73-1.jpg"),
    ("assets/officiel/logo_onnc-e1611182123751.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/logo_onnc-e1611182123751.jpg"),
    ("assets/officiel/maintenance_energies.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/maintenance_energies.jpg"),
    ("assets/officiel/MicrosoftTeams-image-20-scaled.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2023/03/MicrosoftTeams-image-20-scaled.jpg"),
    ("assets/officiel/omexom.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/omexom.png"),
    ("assets/officiel/Omexom-800x472-new-e1611180519178-300x53-1.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/Omexom-800x472-new-e1611180519178-300x53-1.png"),
    ("assets/officiel/Omexom-site-corp@2x-1-e1686714666643.png", "https://www.cegelec.nc/app/uploads/sites/394/2023/06/Omexom-site-corp@2x-1-e1686714666643.png"),
    ("assets/officiel/organisation.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/organisation.jpg"),
    ("assets/officiel/pexels-saban-karabeli-10537250-scaled.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2023/06/pexels-saban-karabeli-10537250-scaled.jpg"),
    ("assets/officiel/power-2881462_1280-e1686631714444.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2023/06/power-2881462_1280-e1686631714444.jpg"),
    ("assets/officiel/reseau_ftth-1-1024x576-1.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/reseau_ftth-1-1024x576-1.png"),
    ("assets/officiel/Sans-titre.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/Sans-titre.jpg"),
    ("assets/officiel/Schema-VINCI.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/Schema-VINCI.png"),
    ("assets/officiel/serres-photovolatiques.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/serres-photovolatiques.jpg"),
    ("assets/officiel/systeme_dispacthing-1024x566-1.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/systeme_dispacthing-1024x566-1.png"),
    ("assets/officiel/Tri-1024x173-1.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/Tri-1024x173-1.jpg"),
    ("assets/officiel/word_clean_up.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/word_clean_up.jpg"),
    ("assets/photos/3224788864.png", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/3224788864.png"),
    ("assets/photos/4269834471.jpeg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/4269834471.jpeg"),
    ("assets/photos/caroussel_numbo.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/caroussel_numbo.jpg"),
    ("assets/photos/dumbea_mall.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/dumbea_mall.jpg"),
    ("assets/photos/serres-photovolatiques.jpg", "https://www.cegelec.nc/app/uploads/sites/394/2022/11/serres-photovolatiques.jpg"),
]

# Images à bandes blanches sur les côtés : on en crée une version recadrée (_crop)
A_RECADRER = [
    "assets/photos/focola_1.jpg",
    "assets/photos/focola_2.jpg",
    "assets/photos/ck2_caroussel.jpg",
    "assets/photos/core-and-backbone.jpg",
]


def telecharger():
    ok = 0
    for chemin, url in IMAGES:
        cible = os.path.join(ICI, *chemin.split("/"))
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        if os.path.exists(cible):
            continue
        requete = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(requete, timeout=30) as rep, open(cible, "wb") as f:
                f.write(rep.read())
            ok += 1
        except Exception as e:  # noqa: BLE001
            print("  échec :", chemin, "->", e)
    print(f"{ok} image(s) téléchargée(s), {len(IMAGES)} attendues.")


def recadrer():
    try:
        from PIL import Image
    except ImportError:
        print("Pillow absent : les images à bandes blanches sont copiées sans recadrage (pip install pillow).")
        Image = None
    for chemin in A_RECADRER:
        src = os.path.join(ICI, *chemin.split("/"))
        if not os.path.exists(src):
            print("  source absente, recadrage ignoré :", chemin)
            continue
        base, ext = os.path.splitext(src)
        dst = base + "_crop" + ext
        if os.path.exists(dst):
            continue
        if Image is None:
            shutil.copyfile(src, dst)
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        lignes = [5, int(h * 0.2), int(h * 0.4), int(h * 0.6), int(h * 0.8), h - 5]

        def colonne_blanche(x):
            return all(min(im.getpixel((x, y))) >= 245 for y in lignes)

        gauche = 0
        while gauche < w - 1 and colonne_blanche(gauche):
            gauche += 1
        droite = w - 1
        while droite > gauche and colonne_blanche(droite):
            droite -= 1
        im.crop((gauche, 0, droite + 1, h)).save(dst, quality=92)
        print("recadrée :", os.path.basename(dst))


if __name__ == "__main__":
    telecharger()
    recadrer()
    os.makedirs(os.path.join(ICI, "assets", "equipe"), exist_ok=True)
    print("Terminé. Lance ensuite :  python build.py  puis ouvre index.html")