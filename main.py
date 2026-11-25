import os

# Unsent: The Micro-Confession Sprint — a two-part micro-confession.
# The reason it stayed unsent lives inside the message itself: saying
# "I forgive you" out loud risks sounding like a ledger, so it stays typed.
ENTRY = "To: Dad\nI forgave you years ago. I just never learned how to say it without sounding like I was still keeping score."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
