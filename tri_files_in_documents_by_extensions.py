from pathlib import Path

dirs = {
    "les_documents": [".docx", ".pdf", ".xlsx", ".pptx", ".txt", ".csv"],
    "les_photos": [".png", ".jpeg", ".bmp", ".jpg"],
    "les_videos": [".mp4", ".gif"],
    "Musiques": [".mp3", ".wav", ".flac"],
}

tri_dir = Path.home() / "Downloads"
files = [f for f in tri_dir.iterdir() if f.is_file()]

for f in files:
    suffix = f.suffix.lower()
    output_dir_name = next(
        (dir_name for dir_name, suffixes in dirs.items() if suffix in suffixes),
        "Autres",
    )
    output_dir = tri_dir / output_dir_name
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
