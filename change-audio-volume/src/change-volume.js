const fs = require('fs')
const path = require('path')
const { exec } = require('child_process');

const VOLUME = 4.0

const normalizeFileNames = () => {
  const inputDir = path.join(__dirname, '..', 'input')

  const outputDir = path.join(__dirname, '..', 'output', `volume-${VOLUME}`)
  const inputFiles = fs.readdirSync(inputDir)
  if (!fs.existsSync(outputDir)){
    fs.mkdirSync(outputDir);
  }
  for (let i = 0; i < inputFiles.length; i++) {
    const fileName = inputFiles[i]
    const command = `ffmpeg -i ${inputDir}/${fileName} -filter:a "volume=${VOLUME}" ${outputDir}/${fileName}`;
    exec(`${command}`, (err, stdout, stderr) => {
      if (err) {
        console.log(err)
        // node couldn't execute the command
        return;
      }
      // the *entire* stdout and stderr (buffered)
      console.log(`stdout: ${stdout}`);
      console.log(`stderr: ${stderr}`);
    });
    // ffmpeg -i input.wav -filter:a "volume=0.5" output.wav
  }
  // const outputFiles = fs.readdirSync(outputDir)
}

normalizeFileNames()

exports.normalizeFileNames = normalizeFileNames
