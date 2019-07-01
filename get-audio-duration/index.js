const { getAudioDurationInSeconds } = require('get-audio-duration')

const inputFileNames = ['input/0.mp3', "input/1.mp3", 'input/2.mp3', 'input/3.mp3', 'input/4.mp3', 'input/5.mp3', 'input/6.mp3']

async function printDurations() {
  for (let i = 0; i < inputFileNames.length; i++) {
    const name = inputFileNames[i];
    await getAudioDurationInSeconds(name).then((duration) => {
      console.log(i + ': ' + duration)
    })
  }
}

printDurations()