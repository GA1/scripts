import PDFMerger from 'pdf-merger-js';

let merger = new PDFMerger();

(async () => {
    await merger.add('./input/1.pdf');
    await merger.add('./input/2.pdf');
    await merger.add('./input/3.pdf');
    await merger.add('./input/4.pdf');

    await merger.setMetadata({
        producer: "pdf-merger-js based script",
        author: "Kamil",
        creator: "Kamil",
        title: "merged pdf"
    });

    await merger.save('./result/merged.pdf');
})();
