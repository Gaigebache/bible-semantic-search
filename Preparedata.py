"Loads raw Bible text from two public-domain translations (KJV, WEB) and normalizes them into one clean"
"flat JSON file with consistent schema and metadata(testament, genre) for embedding + filtering downstream."

"Sources :
" -KJV: https://github.com/aruljohn/Bible-kjv  (one JSON file per book)"
" -WEB: https://github.com/TehShrike/world-english-bible (event-stream JSON)"

KJV_DIR = Path("Bible-kjv")
WEB_DIR = Path("world-english-bible/json")
OUT_PATH = Path("data/verses.json")

# (testament, genre) 
BOOK_META = {
    "Genesis": ("Old Testament", "Law"), "Exodus": ("Old Testament", "Law"),
    "Leviticus": ("Old Testament", "Law"), "Numbers": ("Old Testament", "Law"),
    "Deuteronomy": ("Old Testament", "Law"),
    "Joshua": ("Old Testament", "History"), "Judges": ("Old Testament", "History"),
    "Ruth": ("Old Testament", "History"), "1 Samuel": ("Old Testament", "History"),
    "2 Samuel": ("Old Testament", "History"), "1 Kings": ("Old Testament", "History"),
    "2 Kings": ("Old Testament", "History"), "1 Chronicles": ("Old Testament", "History"),
    "2 Chronicles": ("Old Testament", "History"), "Ezra": ("Old Testament", "History"),
    "Nehemiah": ("Old Testament", "History"), "Esther": ("Old Testament", "History"),
    "Job": ("Old Testament", "Wisdom/Poetry"), "Psalms": ("Old Testament", "Wisdom/Poetry"),
    "Proverbs": ("Old Testament", "Wisdom/Poetry"), "Ecclesiastes": ("Old Testament", "Wisdom/Poetry"),
    "Song of Solomon": ("Old Testament", "Wisdom/Poetry"),
    "Isaiah": ("Old Testament", "Major Prophets"), "Jeremiah": ("Old Testament", "Major Prophets"),
    "Lamentations": ("Old Testament", "Major Prophets"), "Ezekiel": ("Old Testament", "Major Prophets"),
    "Daniel": ("Old Testament", "Major Prophets"),
    "Hosea": ("Old Testament", "Minor Prophets"), "Joel": ("Old Testament", "Minor Prophets"),
    "Amos": ("Old Testament", "Minor Prophets"), "Obadiah": ("Old Testament", "Minor Prophets"),
    "Jonah": ("Old Testament", "Minor Prophets"), "Micah": ("Old Testament", "Minor Prophets"),
    "Nahum": ("Old Testament", "Minor Prophets"), "Habakkuk": ("Old Testament", "Minor Prophets"),
    "Zephaniah": ("Old Testament", "Minor Prophets"), "Haggai": ("Old Testament", "Minor Prophets"),
    "Zechariah": ("Old Testament", "Minor Prophets"), "Malachi": ("Old Testament", "Minor Prophets"),
    "Matthew": ("New Testament", "Gospel"), "Mark": ("New Testament", "Gospel"),
    "Luke": ("New Testament", "Gospel"), "John": ("New Testament", "Gospel"),
    "Acts": ("New Testament", "History"),
    "Romans": ("New Testament", "Epistle"), "1 Corinthians": ("New Testament", "Epistle"),
    "2 Corinthians": ("New Testament", "Epistle"), "Galatians": ("New Testament", "Epistle"),
    "Ephesians": ("New Testament", "Epistle"), "Philippians": ("New Testament", "Epistle"),
    "Colossians": ("New Testament", "Epistle"), "1 Thessalonians": ("New Testament", "Epistle"),
    "2 Thessalonians": ("New Testament", "Epistle"), "1 Timothy": ("New Testament", "Epistle"),
    "2 Timothy": ("New Testament", "Epistle"), "Titus": ("New Testament", "Epistle"),
    "Philemon": ("New Testament", "Epistle"), "Hebrews": ("New Testament", "Epistle"),
    "James": ("New Testament", "Epistle"), "1 Peter": ("New Testament", "Epistle"),
    "2 Peter": ("New Testament", "Epistle"), "1 John": ("New Testament", "Epistle"),
    "2 John": ("New Testament", "Epistle"), "3 John": ("New Testament", "Epistle"),
    "Jude": ("New Testament", "Epistle"), "Revelation": ("New Testament", "Apocalyptic"),
}
assert len(BOOK_META) == 66, f"Expected 66 books, got {len(BOOK_META)}"

#WEB filenames are lowercased or squashed
WEB_FILENAME_TO_BOOK = {re.sub(r"[^a-z0-9]+", "", name.lower()):name for name in BOOK_META}

def slugify(book: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", book.lower()).strip("-")

def load_kjv():
    records = []
    for book, (testament, genre) in BOOK_META.items():
        #KJV repo files drop spaces
        fname = KJV_DIR / f"{book.replace(' ', '')}.json"
        with open(fname, encoding="utf-8") as f:
            data = json.load(f)
        for chapter in data["chapters"]:


