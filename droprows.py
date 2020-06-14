import pandas as pd

df = pd.read_csv('data/scraped_data.csv')

# cover songs, duplicate songs, and songs not released yet
to_drop = [
    'After Dark', 'Amazing Grace (Live in church ver.)',
    'Anata ni Deawanakereba kasetsutouka (Live in church ver.)',
    'Black Bird - Aimer “soleil et pluie” Asia Tour in Shanghai - Live',
    'Breaking Up Is Hard To Do', 'Baby Love', 'Bright Stars',
    'But still...', 'Calendar Girl', 'Change The World',
    'Cold Sun (Ryo Nagano Remix)', 'Crazy in Love',
    'Hoshikuzu Venus (Live in church ver.)', 'Ito', 'One -epilogue-'
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
    'StarRingChild -English ver.-', 'Told U So', 'もう一度'
    'Tsuyoku Hakanai Mono Tachi', 'AM02:00 (Haruka nakamura La Nuit remix)',
    'TWINKLE TWINKLE LITTLE STAR -Prologue-', 'Viva La Vida',
    'WHEN YOU WISH UPON A STAR -prologue-', '春はゆく (Haru wa Yuku)',
    'I beg you - Aimer “soleil et pluie” Asia Tour in Shanghai - Live'
    ]

# rename songs
df.loc[(df.Song_title == 'Akane Sasu (茜さす)', 'Song_title')] = 'Akane Sasu'
df.loc[(df.Song_title == 'Anata ni Deawanakereba ~Kasetsutouka~ (あなたに出会わなければ ～夏雪冬花～)', 'Song_title')] = 'Anata ni Deawanakereba ~Kasetsutouka~'
df.loc[(df.Song_title == 'Chiisana Hoshi no Melody (小さな星のメロディー)', 'Song_title')] = 'Chiisana Hoshi no Melody'
df.loc[(df.Song_title == 'Chouchou Musubi (蝶々結び)', 'Song_title')] = 'Chouchou Musubi'
df.loc[(df.Song_title == 'Dare ka, Umi wo. (誰か、海を。))', 'Song_title')] = 'Dare ka, Umi wo.'
df.loc[(df.Song_title == 'Egao (笑顔)', 'Song_title')] = 'Egao'
df.loc[(df.Song_title == 'Fuyu no Diamond (冬のダイヤモンド) [Re-echoed by Genki Rockets]', 'Song_title')] = 'Fuyu no Diamond'
df.loc[(df.Song_title == 'Hanabiratachi no March (花びらたちのマーチ)', 'Song_title')] = 'Hanabiratachi no March'
df.loc[(df.Song_title == 'Hana no Uta (花の唄)', 'Song_title')] = 'Hana no Uta'
df.loc[(df.Song_title == 'Hoshikuzu Venus (星屑ビーナス)', 'Song_title')] = 'Hoshikuzu Venus'
df.loc[(df.Song_title == 'Hoshi no Kieta Yoru ni (星の消えた夜に) [Re-echoed by Genki Rockets × give me wallets]', 'Song_title')] = 'Hoshi no Kieta Yoru ni'
df.loc[(df.Song_title == 'I-mage ＜in/AR＞ (Romanized)', 'Song_title')] = 'I-mage <in/AR>'
df.loc[(df.Song_title == 'Kachou Fuugetsu (歌鳥風月)', 'Song_title')] = 'Kachou Fuugetsu'
df.loc[(df.Song_title == 'Kanashimi wa Aurora ni (悲しみはオーロラに) [Restarred by Takagi Masakatsu]', 'Song_title')] = 'Kanashimi wa Aurora ni'
df.loc[(df.Song_title == 'Kataomoi (カタオモイ)', 'Song_title')] = 'Kataomoi '
df.loc[(df.Song_title == 'Kimi wo Matsu (君を待つ)', 'Song_title')] = 'Kimi wo Matsu'
df.loc[(df.Song_title == 'Kizuna (キズナ)', 'Song_title')] = 'Kizuna '
df.loc[(df.Song_title == 'Kogoesou na Kisetsu Kara (凍えそうな季節から)', 'Song_title')] = 'Kogoesou na Kisetsu Kara'
df.loc[(df.Song_title == 'Kowairo (声色)', 'Song_title')] = 'Kowairo'
df.loc[(df.Song_title == 'Kyou Kara Omoide (Live in church ver.)', 'Song_title')] = 'Kyou Kara Omoide'
df.loc[(df.Song_title == 'Mabayui bakari (眩いばかり)', 'Song_title')] = 'Mabayui bakari'
df.loc[(df.Song_title == 'Nemuri no Mori (眠りの森)', 'Song_title')] = 'Nemuri no Mori'
df.loc[(df.Song_title == 'Omoide wa Kirei de (思い出は奇麗で)', 'Song_title')] = 'Omoide wa Kirei de'
df.loc[(df.Song_title == 'Rokutosei no Yoru (六等星の夜)', 'Song_title')] = 'Rokutosei no Yoru'
df.loc[(df.Song_title == 'Sabishikute Nemurenai Yoru wa (寂しくて眠れない夜は)', 'Song_title')] = 'Sabishikute Nemurenai Yoru wa'
df.loc[(df.Song_title == 'セプテンバーさん (September San)', 'Song_title')] = 'September San'
df.loc[(df.Song_title == 'Shichigatsu no Tsubasa (7月の翼)', 'Song_title')] = 'Shichigatsu no Tsubasa'
df.loc[(df.Song_title == 'Yakou Ressha (夜行列車) ~nothing to lose~', 'Song_title')] = 'Yakou Ressha ~nothing to lose~'
df.loc[(df.Song_title == 'Yuki no Furu Machi (雪の降る街)', 'Song_title')] = 'Yuki no Furu Machi'
df.loc[(df.Song_title == '夏草に君を想う (Natsukusani Kimiwo Omou)', 'Song_title')] = 'Natsukusani Kimi wo Omou'

# final cleanup
df = df[~df['Song_title'].isin(to_drop)]
df = df[df['Word'].astype(str).str.contains('[a-zA-Z]')]
df.to_csv('data/cleaned_data.csv', index=False)

