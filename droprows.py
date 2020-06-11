import pandas as pd

df = pd.read_csv('scraped_data.csv')

to_drop = [
    'After Dark', 'Amazing Grace (Live in church ver.)',
    'Anata ni Deawanakereba kasetsutouka (Live in church ver.)',
    'Black Bird - Aimer “soleil et pluie” Asia Tour in Shanghai - Live',
    'Breaking Up Is Hard To Do', 'Baby Love', 'Bright Stars',
    'But still...', 'Calendar Girl', 'Change The World',
    'Cold Sun (Ryo Nagano Remix)', 'Crazy in Love',
    'Hoshikuzu Venus (Live in church ver.)', 'Ito'
    'I beg you - Aimer “soleil et pluie” Asia Tour in Shanghai - Live',
    'I Will Always Love You', '​i-mage (in/AR)', '​i-mage',
    'Just say good bye', 'Koyoi no Tsuki no You ni', 'L-O-V-E',
    'Listen', 'Mata Kimi ni Koi Shiteru', 'Mikazuki',
    'MOON RIVER -prologue-', 'Nemuri no mori (Kazuki Remix)',
    '​ninelie (cry-v)', '​pluie', 'Poker Face', 'Precious',
    'RE:I AM -English ver.-', 'RE:I AM (Live in church ver.)',
    'Refrain ga Sakenderu', 'Rokutosei no Yoru (Magic Blue ver.)',
    'S-ave', 'Sabishikute Nemurenai Yoru wa (Live in church ver.)',
    '​soleil', 'Song of... (AM)', 'Spark-Again',
    'StarRingChild -English ver.-', 'Told U So',
    'Tsuyoku Hakanai Mono Tachi',
    'TWINKLE TWINKLE LITTLE STAR -Prologue-', 'Viva La Vida',
    'WHEN YOU WISH UPON A STAR -prologue-', '春はゆく (Haru wa Yuku)'
    ]

df = df[~df['Song_title'].isin(to_drop)]
df = df[df['Word'].astype(str).str.contains('[a-zA-Z]')]
df.to_csv('cleaned_data.csv')
