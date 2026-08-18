"Loads raw Bible text from two public-domain translations (KJV, WEB) and normalizes them into one clean"
"flat JSON file with consistent schema and metadata(testament, genre) for embedding + filtering downstream."

"Sources :
" -KJV: https://github.com/aruljohn/Bible-kjv  (one JSON file per book)"
" -WEB: https://github.com/TehShrike/world-english-bible (event-stream JSON)"

KJV_DIR = Path("Bible-kjv")
WEB_DIR = Path("world-english-bible/json")
OUT_PATH = Path("data/verses.json")

