import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashion_store.settings')
django.setup()

from store.models import Category, Product

print("Resetting database for 20 curated Indian fashion items...")
Product.objects.all().delete()
Category.objects.all().delete()

# Create Categories
men_cat = Category.objects.create(name='Men', slug='men')
women_cat = Category.objects.create(name='Women', slug='women')
kids_cat = Category.objects.create(name='Kids', slug='kids')
acc_cat = Category.objects.create(name='Accessories', slug='accessories')

catalog = [
    # --- MEN (5 Items) ---
    {
        "cat": men_cat,
        "title": "Royal Navy Blue Silk Kurta Pyjama Set",
        "desc": "Traditional North Indian festive silk kurta paired with comfortable white pyjamas.",
        "image": "https://images.unsplash.com/photo-1617137984095-74e4e5e3613f?w=600", # Updated working image link
        "price": 2499, "discount": 1999
    },
    {
        "cat": men_cat,
        "title": "Traditional White Kasavu Cotton Shirt",
        "desc": "Authentic South Indian Kerala cotton shirt for weddings and festivals.",
        "image": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600",
        "price": 1899, "discount": 1499
    },
    {
        "cat": men_cat,
        "title": "Maroon Velvet Wedding Sherwani",
        "desc": "Heavy embroidered North Indian groom sherwani crafted in rich maroon velvet.",
        "image": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600",
        "price": 4999, "discount": 3999
    },
    {
        "cat": men_cat,
        "title": "Beige Designer Nehru Jacket Set",
        "desc": "Sleek sleeveless Nehru jacket layered over a crisp pastel kurta.",
        "image": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=600",
        "price": 2999, "discount": 2499
    },
    {
        "cat": men_cat,
        "title": "Olive Green Cotton Short Kurta",
        "desc": "Fusion-style olive green short kurta designed for contemporary ethnic wear.",
        "image": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=600",
        "price": 1599, "discount": 1199
    },

    # --- WOMEN (5 Items) ---
    {
        "cat": women_cat,
        "title": "Kanchipuram Red & Gold Pure Silk Saree",
        "desc": "Exquisite South Indian traditional bridal silk saree with rich Zari pallu.",
        "image": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600",
        "price": 4899, "discount": 3999
    },
    {
        "cat": women_cat,
        "title": "Pastel Pink Georgette Anarkali Suit",
        "desc": "Flowing North Indian floor-length Anarkali suit adorned with delicate threadwork.",
        "image": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=600",
        "price": 3499, "discount": 2799
    },
    {
        "cat": women_cat,
        "title": "Emerald Green Banarasi Brocade Saree",
        "desc": "Classic North Indian royal Banarasi silk saree with intricate gold weaving.",
        "image": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=600",
        "price": 4599, "discount": 3699
    },
    {
        "cat": women_cat,
        "title": "Mustard Yellow Designer Lehenga Choli",
        "desc": "Stunning festive lehenga skirt paired with an embellished designer choli and dupatta.",
        "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600",
        "price": 4999, "discount": 4199
    },
    {
        "cat": women_cat,
        "title": "Teal Blue Elegant Party Gown",
        "desc": "Contemporary Western-style evening gown featuring a flattering fit and flare silhouette.",
        "image": "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=600",
        "price": 3299, "discount": 2599
    },

    # --- KIDS (5 Items) ---
    {
        "cat": kids_cat,
        "title": "Kids Golden Silk Kurta Pyjama Set",
        "desc": "Adorable festive ethnic wear specially tailored for young boys.",
        "image": "https://images.unsplash.com/photo-1519457431-44ccd64a579b?w=600",
        "price": 1499, "discount": 1199
    },
    {
        "cat": kids_cat,
        "title": "Baby Girls Traditional Pattu Pavadai",
        "desc": "Classic South Indian silk skirt and blouse set for traditional ceremonies.",
        "image": "https://images.unsplash.com/photo-1596870230751-ebdfce98ec42?w=600",
        "price": 1699, "discount": 1299
    },
    {
        "cat": kids_cat,
        "title": "Kids Pastel Pink Party Frock",
        "desc": "Flared tulle party dress with ribbon bow for birthdays and celebrations.",
        "image": "https://images.unsplash.com/photo-1503944583220-74e893e2f784?w=600",
        "price": 1399, "discount": 1099
    },
    {
        "cat": kids_cat,
        "title": "Boys Royal Blue Sherwani Set",
        "desc": "Miniature ceremonial sherwani for young boys attending weddings.",
        "image": "https://images.unsplash.com/photo-1471286174890-9c112ffca5b4?w=600",
        "price": 2199, "discount": 1799
    },
    {
        "cat": kids_cat,
        "title": "Children Denim Dungarees & T-Shirt",
        "desc": "Durable cotton overalls paired with a cute striped tee for active play.",
        "image": "https://images.unsplash.com/photo-1522771930-78848d9293e8?w=600",
        "price": 1299, "discount": 999
    },

    # --- ACCESSORIES (5 Items) ---
    {
        "cat": acc_cat,
        "title": "Traditional Kundan Gold Necklace Set",
        "desc": "Exquisite bridal ethnic necklace paired with matching earrings.",
        "image": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=600",
        "price": 2999, "discount": 2399
    },
    {
        "cat": acc_cat,
        "title": "Antique Temple Jewellery Jhumkas",
        "desc": "South Indian temple-style gold plated hanging jhumka earrings.",
        "image": "https://images.unsplash.com/photo-1630019852942-f89202989a59?w=600",
        "price": 1299, "discount": 999
    },
    {
        "cat": acc_cat,
        "title": "Embroidered Ethnic Silk Potli Bag",
        "desc": "Handcrafted traditional drawstring pouch adorned with zari embroidery.",
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=600",
        "price": 899, "discount": 699
    },
    {
        "cat": acc_cat,
        "title": "Men Leather Mojaris / Juttis",
        "desc": "Handmade ethnic leather footwear designed to match traditional sherwanis and kurtas.",
        "image": "https://images.unsplash.com/photo-1533867617858-e7d97e0afd8b?w=600",
        "price": 1999, "discount": 1599
    },
    {
        "cat": acc_cat,
        "title": "Traditional Silver Oxidized Choker",
        "desc": "Boho-chic German silver choker necklace for ethnic and fusion outfits.",
        "image": "https://images.unsplash.com/photo-1611591478339-30c6810ef50c?w=600",
        "price": 1199, "discount": 899
    }
]

print(f"Seeding exactly {len(catalog)} items (5 per sector)...")

for item in catalog:
    Product.objects.create(
        category=item['cat'],
        title=item['title'],
        description=item['desc'],
        price=item['price'],
        discount_price=item['discount'],
        stock=50,
        image_url=item['image'],
        is_featured=True
    )

print("Successfully populated 5 items per sector with correct images!")