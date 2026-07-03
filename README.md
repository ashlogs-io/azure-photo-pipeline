# photo-app

A Python pipeline that compresses large images and saves photos as compressed files. These compressed files can be viewed on the web.

## What it does
- `image_resize.py` - compresses photos from rawimages/ into compressedimages/, handles multiple formats, skips non-images
- `build_gallery.py` - reads compressedimages/ and builds gallery.html

## Requirements
- Python 3.10+
- pillow (`pip3 install pillow`)
- pillow-heif (`pip3 install pillow-heif`)

## How to run 
1. Add your original photos to 'rawimages/'
2. Run the image resize script:
    ```bash
    python3 image_resize.py
    ```
3. Build gallery to show photos on the web
    ```bash
    python3 build_gallery.py
    ```

## Folder structure
```
photo-app/
├── rawimages/ #raw image files saved here (git ignored)
├── build_gallery.py
├── image_resize.py
└── README.md
```

## What's next
- Migrating all this to Azure Blob Storage
- Automating image resize and building gallery with Azure functions
