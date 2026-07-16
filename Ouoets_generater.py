from random import choice
bond_quotes = {
    "BFF": [
        "BFFs forever, no matter what.",
        "Best friends make life sweeter.",
        "Through thick and thin, BFFs stick.",
        "BFFs laugh, cry, and grow together.",
        "Forever friends, forever smiles.",
        "BFFs turn moments into memories.",
        "Life is better with a BFF.",
        "BFFs are the chosen family.",
        "A BFF knows your heart.",
        "Best friends, endless adventures."
    ],
    "Buddy": [
        "Good buddies make the day brighter.",
        "Buddy time is always fun.",
        "A buddy shares laughs and snacks.",
        "Life’s easier with a buddy.",
        "Buddies stick around in small ways.",
        "Every buddy adds a smile.",
        "A buddy knows the simple joys.",
        "Buddy moments are casual magic.",
        "Buddies bring comfort, not complications.",
        "A buddy makes ordinary days special."
    ],
    "Pal": [
        "A pal makes hard times lighter.",
        "Pals share the smallest joys.",
        "A pal is always there quietly.",
        "Pals make memories unforgettable.",
        "With a pal, life feels easier.",
        "Pals understand without words.",
        "A pal adds laughter to the day.",
        "Pals turn ordinary into extraordinary.",
        "A true pal never judges.",
        "Pals stay through ups and downs."
    ],
    "Mate": [
        "Mates make adventures memorable.",
        "A mate is your partner in crime.",
        "Mates double the fun in life.",
        "Laughs are louder with a mate.",
        "Mates share secrets and smiles.",
        "Every mate brings joy.",
        "Mates make dull days bright.",
        "A mate turns small plans into big memories.",
        "Mates are life’s bonus.",
        "A mate sticks even in silence."
    ],
    "Confidant": [
        "A confidant listens without judgment.",
        "Confidants know your hidden thoughts.",
        "Trust grows with a confidant.",
        "Confidants make your worries lighter.",
        "Secrets are safe with a confidant.",
        "A confidant understands your heart.",
        "Confidants are rare and precious.",
        "True confidants never betray trust.",
        "A confidant makes tough choices easier.",
        "Confidants turn pain into relief."
    ],
    "Lifelong": [
        "Lifelong friends know your roots.",
        "Memories with lifelong friends last forever.",
        "A lifelong friend grows with you.",
        "Through years, lifelong friends remain.",
        "Childhood bonds turn into lifelong friendship.",
        "Lifelong friends share silent understanding.",
        "Time strengthens lifelong bonds.",
        "Lifelong friends are irreplaceable.",
        "Laughs with lifelong friends never fade.",
        "A lifelong friend feels like home."
    ],
    "Sidekick": [
        "Sidekicks make every adventure better.",
        "Fun is doubled with a sidekick.",
        "A sidekick turns risks into memories.",
        "Sidekicks share every silly idea.",
        "Life is an adventure with a sidekick.",
        "Sidekicks laugh at your worst jokes.",
        "A sidekick makes fear fun.",
        "Every plan is brighter with a sidekick.",
        "Sidekicks stay when others run.",
        "Sidekicks add color to life."
    ],
    "NetBuddy": [
        "NetBuddies bridge the distance.",
        "Online friends feel close at heart.",
        "NetBuddies share smiles across screens.",
        "A NetBuddy is always a message away.",
        "Distance cannot break NetBuddy bonds.",
        "NetBuddies make chats memorable.",
        "Digital hugs from NetBuddies matter.",
        "A NetBuddy listens at any time.",
        "NetBuddies turn lonely nights into fun.",
        "Online friends are real friends too."
    ],
    "Supporter": [
        "Supporters lift you when you fall.",
        "A supporter strengthens your courage.",
        "Supporters make challenges lighter.",
        "True supporters celebrate small wins.",
        "Supporters are always on your side.",
        "A supportive friend eases burdens.",
        "Supporters believe in you silently.",
        "Supporters make hard times bearable.",
        "A supporter adds hope and strength.",
        "Supporters turn struggles into victories."
    ],
    "Companion": [
        "A companion walks with you through life.",
        "Companions share every joy and sorrow.",
        "Life is richer with a true companion.",
        "Companions stand steady in storms.",
        "A companion makes moments unforgettable.",
        "Companions feel like home.",
        "Every step is lighter with a companion.",
        "Companions stay even when paths diverge.",
        "A companion is a heart beside yours.",
        "Companions make life meaningful."
    ]
}
print("=== Friendship Bond Types ===")
for i, bond in enumerate(bond_quotes.keys(), 1):
    print(f"{i}. {bond}")

choice_input = input("\nEnter your bond type (BFF, Buddy, Pal, etc.): ").strip()

if choice_input in bond_quotes:
    random_quote = choice(bond_quotes[choice_input])
    print(f"\n💛 Your Bond: {choice_input}")
    print("✨ Random Quote: ", random_quote)
else:
    print("❌ Invalid input! Please enter a valid bond type.")
