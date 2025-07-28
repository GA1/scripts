# Image to PDF Merger

A simple Node.js script that merges multiple image files into a single PDF document.

## Features

- Supports JPG, JPEG, and PNG image formats
- Automatically processes all images in the input directory
- Each image becomes a separate page in the PDF
- Maintains original image dimensions
- Sorts images alphabetically for consistent ordering

## Setup

1. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

## Usage

1. Place your image files in the `./input/` directory
2. Run the script:
   ```bash
   npm start
   # or
   yarn start
   ```
3. The merged PDF will be created as `./result/merged-images.pdf`

## Supported Formats

- `.jpg` / `.jpeg`
- `.png`

## Directory Structure

```
img-to-pdf/
├── input/           # Place your image files here
├── result/          # Output PDF will be generated here
├── index.mjs        # Main script
├── package.json     # Dependencies
└── README.md        # This file
```

## Example

If you have these files in `./input/`:
- `image1.jpg`
- `image2.png`
- `image3.jpeg`

The script will create a PDF with 3 pages, one for each image, in alphabetical order. 