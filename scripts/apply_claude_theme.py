#!/usr/bin/env python3
"""
Apply Claude Design System (terracotta, charcoal ink, warm peach, cream canvas)
to all visual assets in the repository.
"""

import hashlib
import json
import os
import sys
import time
from PIL import Image, ImageSequence

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Authoritative Color Anchors (Green Theme -> Claude Design System)
ANCHORS = [
    # Primary Accent: Forest Green -> Claude Signature Terracotta
    ((24, 57, 42), (217, 119, 87)),      # #18392a -> #d97757
    ((24, 56, 41), (217, 119, 87)),
    ((25, 59, 43), (217, 119, 87)),
    ((23, 55, 40), (217, 119, 87)),

    # Dark Ink: Greenish Black -> Claude Dark Charcoal Ink
    ((24, 37, 31), (31, 30, 29)),        # #18251f -> #1f1e1d
    ((24, 36, 30), (31, 30, 29)),
    ((27, 40, 34), (31, 30, 29)),
    ((35, 48, 42), (45, 42, 40)),

    # Soft Accent Fill: Pale Mint/Sage -> Claude Soft Peach / Light Clay
    ((225, 234, 219), (244, 232, 223)),  # #e1eadb -> #f4e8df
    ((221, 232, 223), (244, 232, 223)),
    ((212, 226, 208), (242, 228, 218)),
    ((238, 243, 234), (248, 239, 233)),
    ((240, 245, 235), (248, 239, 233)),

    # Accent Borders: Sage Green Border -> Claude Warm Terracotta Line
    ((113, 131, 109), (201, 115, 86)),   # #71836d -> #c97356
    ((125, 143, 121), (201, 115, 86)),

    # Container Borders: Light Green Border -> Claude Warm Card Border
    ((188, 200, 183), (227, 216, 206)),  # #bcc8b7 -> #e3d8ce
    ((204, 213, 201), (227, 216, 206)),  # #ccd5c9 -> #e3d8ce
    ((205, 214, 200), (227, 216, 206)),  # #cdd6c8 -> #e3d8ce
    ((196, 207, 190), (224, 213, 202)),
    ((211, 220, 205), (230, 220, 210)),

    # Secondary Muted Text: Muted Green -> Claude Warm Muted Ink
    ((84, 99, 88), (115, 107, 99)),      # #546358 -> #736b63
    ((81, 90, 86), (115, 107, 99)),

    # Neutrals, Cards & Canvas Backgrounds:
    ((254, 254, 252), (254, 254, 252)),  # #fefefc -> white card base
    ((255, 255, 255), (255, 255, 255)),  # pure white
    ((252, 251, 248), (250, 247, 242)),  # #fcfbf8 -> #faf7f2 (Claude cream canvas)
    ((245, 244, 239), (247, 242, 236)),
    ((241, 240, 235), (245, 240, 234)),  # #f1f0eb -> #f5f0ea (Claude warm inner section)
]


def map_color(rgb):
    """Maps a single (r, g, b) tuple using IDW distance weighting."""
    for src, dst in ANCHORS:
        if rgb == src:
            return dst

    weights = []
    for src, dst in ANCHORS:
        dr = rgb[0] - src[0]
        dg = rgb[1] - src[1]
        db = rgb[2] - src[2]
        dist_sq = dr * dr + dg * dg + db * db
        if dist_sq < 1:
            return dst
        weights.append(1.0 / (dist_sq ** 2.2))

    total_w = sum(weights)
    out_r = sum(w * dst[0] for w, (s, dst) in zip(weights, ANCHORS)) / total_w
    out_g = sum(w * dst[1] for w, (s, dst) in zip(weights, ANCHORS)) / total_w
    out_b = sum(w * dst[2] for w, (s, dst) in zip(weights, ANCHORS)) / total_w
    return (int(round(out_r)), int(round(out_g)), int(round(out_b)))


def recolor_image(path, preserve_boxes=None):
    """Recolors a single PNG image file."""
    t0 = time.time()
    img = Image.open(path).convert('RGB')
    preserved_crops = []
    if preserve_boxes:
        for box in preserve_boxes:
            preserved_crops.append((img.crop(box), box))

    colors = set(img.getdata())
    lut = {c: map_color(c) for c in colors}

    out = Image.new('RGB', img.size)
    out.putdata([lut[p] for p in img.getdata()])

    if preserved_crops:
        for crop, box in preserved_crops:
            out.paste(crop, box)

    out.save(path)
    print(f"  [PNG] {os.path.basename(path)} ({img.size[0]}x{img.size[1]}) recolored in {time.time() - t0:.2f}s")


def recolor_gif(path, preserve_boxes=None):
    """Recolors a GIF animation frame-by-frame."""
    t0 = time.time()
    gif = Image.open(path)
    durations = []
    frames = []

    # Precompute global LUT across frames
    all_colors = set()
    for frame in ImageSequence.Iterator(gif):
        durations.append(frame.info.get('duration', 70))
        all_colors.update(frame.convert('RGB').getdata())

    lut = {c: map_color(c) for c in all_colors}

    # Generate palette image
    palette_colors = list(set(lut.values()))[:256]
    while len(palette_colors) < 256:
        palette_colors.append((0, 0, 0))
    flat_pal = [val for col in palette_colors for val in col]
    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(flat_pal)

    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        rgb = frame.convert('RGB')
        preserved = []
        if preserve_boxes:
            for box in preserve_boxes:
                preserved.append((rgb.crop(box), box))

        new_data = [lut[p] for p in rgb.getdata()]
        out_frame = Image.new('RGB', frame.size)
        out_frame.putdata(new_data)

        if preserved:
            for crop, box in preserved:
                out_frame.paste(crop, box)

        frame_p = out_frame.quantize(palette=pal_img, dither=Image.Dither.NONE)
        frames.append(frame_p)

    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0
    )
    print(f"  [GIF] {os.path.basename(path)} ({len(frames)} frames) recolored in {time.time() - t0:.2f}s")


def update_manifest():
    """Recalculates SHA-256 hashes in manifest.json."""
    manifest_path = os.path.join(ASSETS_DIR, 'manifest.json')
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    for item in manifest.get('assets', []):
        fpath = os.path.join(ASSETS_DIR, item['file'])
        with open(fpath, 'rb') as fp:
            item['sha256'] = hashlib.sha256(fp.read()).hexdigest()

    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
        f.write('\n')
    print("  [Manifest] manifest.json hashes updated.")


def main():
    print("=== Transforming Assets to Claude Theme ===")
    
    # 1. linkedin-funnel.png
    recolor_image(os.path.join(ASSETS_DIR, 'linkedin-funnel.png'))

    # 2. content-waterfall-map.png
    recolor_image(os.path.join(ASSETS_DIR, 'content-waterfall-map.png'))

    # 3. content-waterfall@2x.png (preserve 2 avatar photos)
    cw_boxes = [
        (100, 70, 260, 230),      # Top badge avatar
        (100, 3530, 230, 3650),   # Bottom banner avatar
    ]
    recolor_image(os.path.join(ASSETS_DIR, 'content-waterfall@2x.png'), preserve_boxes=cw_boxes)

    # 4. content-waterfall.gif (preserve top avatar badge across frames)
    # Scaled coords for 1080x1350: top avatar badge at x=34..88, y=24..78
    gif_cw_boxes = [(34, 24, 88, 78)]
    recolor_gif(os.path.join(ASSETS_DIR, 'content-waterfall.gif'), preserve_boxes=gif_cw_boxes)

    # 5. linkedin-funnel.gif
    recolor_gif(os.path.join(ASSETS_DIR, 'linkedin-funnel.gif'))

    # Update manifest
    update_manifest()
    print("=== All assets successfully converted to Claude Theme! ===")


if __name__ == '__main__':
    main()
