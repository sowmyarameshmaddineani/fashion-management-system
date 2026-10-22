import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashion_store.settings')
django.setup()

from store.models import Category, Product

print("Clearing old database records...")
Product.objects.all().delete()
Category.objects.all().delete()

# Create Categories
men_cat = Category.objects.create(name='Men', slug='men')
women_cat = Category.objects.create(name='Women', slug='women')
kids_cat = Category.objects.create(name='Kids', slug='kids')
acc_cat = Category.objects.create(name='Accessories', slug='accessories')

catalog = [
    # --- MEN (10 Items) ---
    {
        "cat": men_cat,
        "title": "Royal Navy Blue Silk Kurta Pyjama Set",
        "desc": "Traditional North Indian festive silk kurta paired with comfortable white pyjamas.",
        "image": "https://images.unsplash.com/photo-1597983074815-f513d8091873?w=600",
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
        "title": "Classic Black Linen Casual Shirt",
        "desc": "Breathable black linen shirt perfect for modern casual outings.",
        "image": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=600",
        "price": 1299, "discount": 999
    },
    {
        "cat": men_cat,
        "title": "Olive Green Cotton Short Kurta",
        "desc": "Fusion-style olive green short kurta designed for contemporary ethnic wear.",
        "image": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=600",
        "price": 1599, "discount": 1199
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
        "title": "Teal Blue Checkered Casual Cotton Shirt",
        "desc": "Vibrant teal checkered shirt tailored for comfortable daily wear.",
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600",
        "price": 1399, "discount": 1099
    },
    {
        "cat": men_cat,
        "title": "Charcoal Grey Slim Fit Formal Suit",
        "desc": "Sharp professional two-piece suit for corporate meetings and receptions.",
        "image": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600",
        "price": 4599, "discount": 3799
    },
    {
        "cat": men_cat,
        "title": "Mustard Yellow Cotton Festive Dhoti Kurta",
        "desc": "Bright festive wear combining a sunshine yellow kurta with traditional cotton dhoti.",
        "image": "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?w=600",
        "price": 2199, "discount": 1799
    },
    {
        "cat": men_cat,
        "title": "Rust Orange Streetwear Hoodie",
        "desc": "Cozy fleece pullover hoodie featuring modern urban styling.",
        "image": "https://images.unsplash.com/photo-1509967419530-da38b4704bc6?w=600",
        "price": 1799, "discount": 1399
    },

    # --- WOMEN (10 Items) ---
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
        "image": "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?w=600",
        "price": 4599, "discount": 3699
    },
    {
        "cat": women_cat,
        "title": "Floral Summer Cotton Midi Dress",
        "desc": "Breezy pastel floral print dress designed for warm weather elegance.",
        "image": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600",
        "price": 1699, "discount": 1299
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
        "title": "Sky Blue Cotton Printed Kurti Set",
        "desc": "Casual everyday wear straight-cut cotton kurti with matching trousers and dupatta.",
        "image": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=600",
        "price": 1499, "discount": 1199
    },
    {
        "cat": women_cat,
        "title": "Teal Blue Elegant Party Gown",
        "desc": "Contemporary Western-style evening gown featuring a flattering fit and flare silhouette.",
        "image": "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=600",
        "price": 3299, "discount": 2599
    },
    {
        "cat": women_cat,
        "title": "Classic High-Waist Blue Denim Jeans",
        "desc": "Comfortable stretch denim jeans offering a timeless casual fit.",
        "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600",
        "price": 1799, "discount": 1399
    },
    {
        "cat": women_cat,
        "title": "Beige Chic Oversized Blazer",
        "desc": "Modern neutral-toned blazer for professional power dressing and casual layering.",
        "image": "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=600",
        "price": 2899, "discount": 2299
    },
    {
        "cat": women_cat,
        "title": "Crimson Red Velvet Party Dress",
        "desc": "Luxurious soft velvet midi dress designed for winter parties and celebrations.",
        "image": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=600",
        "price": 2799, "discount": 2199
    },

    # --- KIDS (10 Items) ---
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
        "title": "Children Denim Dungarees & T-Shirt",
        "desc": "Durable cotton overalls paired with a cute striped tee for active play.",
        "image": "https://images.unsplash.com/photo-1522771930-78848d9293e8?w=600",
        "price": 1299, "discount": 999
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
        "title": "Girls Floral Cotton Lehenga Choli",
        "desc": "Lightweight ethnic wear lehenga set designed for comfortable festive dancing.",
        "image": "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=600",
        "price": 1899, "discount": 1499
    },
    {
        "cat": kids_cat,
        "title": "Junior Yellow Cotton Short Kurta",
        "desc": "Breezy yellow cotton ethnic top paired with comfortable white pyjamas.",
        "image": "https://images.unsplash.com/photo-1503944583220-74e893e2f784?w=600",
        "price": 999, "discount": 799
    },
    {
        "cat": kids_cat,
        "title": "Toddler Warm Fleece Hoodie",
        "desc": "Cozy pullover hoodie to keep little ones warm during chilly evenings.",
        "image": "https://images.unsplash.com/photo-1519457431-44ccd64a579b?w=600",
        "price": 1199, "discount": 899
    },
    {
        "cat": kids_cat,
        "title": "Girls Mint Green Anarkali Suit",
        "desc": "Charming little ethnic suit crafted with soft breathable cotton fabric.",
        "image": "https://images.unsplash.com/photo-1596870230751-ebdfce98ec42?w=600",
        "price": 1599, "discount": 1299
    },
    {
        "cat": kids_cat,
        "title": "Boys Checkered Casual Cotton Shirt",
        "desc": "Smart everyday button-down shirt for young boys.",
        "image": "https://images.unsplash.com/photo-1522771930-78848d9293e8?w=600",
        "price": 899, "discount": 699
    },

    # --- ACCESSORIES (10 Items) ---
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
        "title": "Bridal Zari Embroidered Clutch",
        "desc": "Stunning party clutch embellished with beads and metallic threadwork.",
        "image": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=600",
        "price": 1499, "discount": 1199
    },
    {
        "cat": acc_cat,
        "title": "Men Classic Silk Pocket Square & Stole",
        "desc": "Matching jacquard silk pocket square and matching stole set for ethnic suits.",
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600",
        "price": 799, "discount": 599
    },
    {
        "cat": acc_cat,
        "title": "Traditional Silver Oxidized Choker",
        "desc": "Boho-chic German silver choker necklace for ethnic and fusion outfits.",
        "image": "https://images.unsplash.com/photo-1611591478339-30c6810ef50c?w=600",
        "price": 1199, "discount": 899
    },
    {
        "cat": acc_cat,
        "title": "Designer Metallic Waist Belt / Kamarbandh",
        "desc": "Graceful traditional waist ornament worn over sarees and lehengas.",
        "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600",
        "price": 1599, "discount": 1299
    },
    {
        "cat": acc_cat,
        "title": "Men Metallic Analog Wrist Watch",
        "desc": "Sleek stainless steel luxury wrist watch for formal and festive wear.",
        "image": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=600",
        "price": 3499, "discount": 2799
    },
    {
        "cat": acc_cat,
        "title": "Women Floral Hair Gajra & Pins",
        "desc": "Traditional jasmine and rose floral hair accessory for South/North Indian braids.",
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600",
        "price": 499, "discount": 349
    }
]

print(f"Seeding exactly {len(catalog)} items (10 per sector)...")

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

print("Successfully populated exactly 10 items per sector (40 total items)!")