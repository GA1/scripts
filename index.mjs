import { PDFDocument } from 'pdf-lib';
import fs from 'fs';
import path from 'path';

(async () => {
    try {
        // Create a new PDF document
        const pdfDoc = await PDFDocument.create();
        
        // Set metadata
        pdfDoc.setTitle('Merged Images PDF');
        pdfDoc.setAuthor('Kamil');
        pdfDoc.setCreator('img-to-pdf script');
        pdfDoc.setProducer('pdf-lib based script');
        
        // Read all files from input directory
        const inputDir = './input';
        const files = fs.readdirSync(inputDir);
        
        // Filter for common image formats
        const imageFiles = files.filter(file => {
            const ext = path.extname(file).toLowerCase();
            return ['.jpg', '.jpeg', '.png'].includes(ext);
        }).sort(); // Sort to ensure consistent order
        
        if (imageFiles.length === 0) {
            console.log('No image files found in ./input directory');
            console.log('Supported formats: .jpg, .jpeg, .png');
            return;
        }
        
        console.log(`Found ${imageFiles.length} image files:`);
        imageFiles.forEach(file => console.log(`  - ${file}`));
        
        // Process each image file
        for (const imageFile of imageFiles) {
            const imagePath = path.join(inputDir, imageFile);
            const imageBytes = fs.readFileSync(imagePath);
            
            let image;
            const ext = path.extname(imageFile).toLowerCase();
            
            // Embed image based on format with better quality settings
            if (ext === '.png') {
                // PNG: Embed without compression to preserve quality
                image = await pdfDoc.embedPng(imageBytes);
            } else if (['.jpg', '.jpeg'].includes(ext)) {
                // JPG: Embed with minimal compression
                image = await pdfDoc.embedJpg(imageBytes);
            }
            
            // Get image dimensions
            const { width, height } = image;
            
            // Add a new page with image dimensions
            const page = pdfDoc.addPage([width, height]);
            
            // Draw the image to fill the entire page without any transformations
            // that might affect color/brightness
            page.drawImage(image, {
                x: 0,
                y: 0,
                width: width,
                height: height,
                // Don't apply any opacity or color transformations
                opacity: 1.0,
            });
            
            console.log(`Added ${imageFile} (${width}x${height})`);
        }
        
        // Save the PDF without additional compression
        const pdfBytes = await pdfDoc.save({
            useObjectStreams: false, // Disable object streams for better compatibility
            addDefaultPage: false,   // Don't add default page
        });
        
        const outputPath = './result/merged-images.pdf';
        fs.writeFileSync(outputPath, pdfBytes);
        
        console.log(`\n✅ Successfully created PDF: ${outputPath}`);
        console.log(`📄 Total pages: ${imageFiles.length}`);
        console.log(`\n💡 If images still appear dark:`);
        console.log(`   • Try a different PDF viewer (Preview, Adobe, Chrome)`);
        console.log(`   • Check your display color profile settings`);
        console.log(`   • Original images might have different color spaces`);
        
    } catch (error) {
        console.error('❌ Error creating PDF:', error.message);
    }
})(); 