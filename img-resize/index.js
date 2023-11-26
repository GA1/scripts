const sharp = require('sharp');
const fs = require('fs');
const Jimp = require('jimp');
const imgNames = fs.readdirSync('./input');
console.log(imgNames)

async function resizeAllImages() { // Function name is same as of file name
  // Reading Image
  for (const name of imgNames) {


    let inputFile  = "./input/" + name;
    let outputFile = "./output/" + name;

    sharp(inputFile).resize({ height: 1000 }).toFile(outputFile)
      .then(function(newFileInfo) {
        // newFileInfo holds the output file properties
        console.log("Success")
      })
      .catch(function(err) {
        console.log("Error occured");
      });

    // const image = await Jimp.read('./input/' + name);
    // image.resize(1500, function(err){
    //   if (err) throw err;
    // }).write('./output/' + name);
  }
}

resizeAllImages(); // Calling the function here using async
