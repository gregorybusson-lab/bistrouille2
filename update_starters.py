import re

with open('index.html', 'r') as f:
    content = f.read()

old = '''<article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Œufs mayo" src="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80"></div><div><div class="menu-item__name">Œufs mayo *</div><p class="menu-item__desc">Mayo maison, ciboulette, fleur de sel.</p></div><div class="menu-item__price">6€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Poireaux vinaigrette" src="https://images.unsplash.com/photo-1526312426976-593c2b999512?auto=format&fit=crop&w=600&q=80"></div><div><div class="menu-item__name">Poireaux vinaigrette *</div><p class="menu-item__desc">Vinaigrette moutardée, herbes fraîches, noisettes.</p></div><div class="menu-item__price">8€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Terrine du chef" src="https://images.unsplash.com/photo-1544025163-5fd6a5d7d8bf?auto=format&fit=crop&w=600&q=80"></div><div><div class="menu-item__name">Terrine du chef</div><p class="menu-item__desc">Pickles maison, pain de campagne tiède.</p></div><div class="menu-item__price">9€</div></article>'''

new = '''<article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Salade d’avocat et crevettes" src="https://storage.googleapis.com/getedgar_prod_storage/photos/01K87XP7MB7T2H0MRKR7EZX6P5.jpg"></div><div><div class="menu-item__name">Salade d’avocat et crevettes *</div><p class="menu-item__desc">Oranges et vinaigrette à l’huile de sésame, accompagnée d’une sauce cocktail.</p></div><div class="menu-item__price">10€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Planche de charcuterie à partager" src="https://storage.googleapis.com/getedgar_prod_storage/photos/01K87XQSCRQBWV20KMSZ5XHQKF.jpg"></div><div><div class="menu-item__name">Planche de charcuterie à partager</div><p class="menu-item__desc"></p></div><div class="menu-item__price">18€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Poêlée de supions en persillade" src="https://storage.googleapis.com/getedgar_prod_storage/photos/01K87Y3VFZ3B3DNNQCQ7RB264A.jpg"></div><div><div class="menu-item__name">Poêlée de supions en persillade</div><p class="menu-item__desc">Citron vert et émulsion de coquillages safranée.</p></div><div class="menu-item__price">14€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Oeufs Mayonnaise" src="https://storage.googleapis.com/getedgar_prod_storage/photos/01K87XS7SBNFY3R2DJCF2ZDDN1.jpg"></div><div><div class="menu-item__name">Oeufs Mayonnaise *</div><p class="menu-item__desc">Sur leur lit de macédoine revisitée.</p></div><div class="menu-item__price">8€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Ceux de Moëlle" src="logo.svg"></div><div><div class="menu-item__name">Ceux de Moëlle *</div><p class="menu-item__desc"></p></div><div class="menu-item__price">8.5€</div></article>
              <article class="menu-item"><div class="menu-item__thumb"><img loading="lazy" decoding="async" alt="Tartine Caramélisée" src="logo.svg"></div><div><div class="menu-item__name">Tartine Caramélisée *</div><p class="menu-item__desc">Pain de campagne, oignons caramélisés et fleur de sel.</p></div><div class="menu-item__price">6€</div></article>'''

content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated")
