const { getAudioDurationInSeconds } = require('get-audio-duration')

const inputFiles = ['input/0.mp3', "input/1.mp3", ' input/2.mp3', 'input/3.mp3', 'input/4.mp3', 'input/5.mp3', 'input/6.mp3']

inputFiles.map((name, index) => {
  getAudioDurationInSeconds(name).then((duration) => {
    console.log(index + ': ' +  duration)
  })
})
