const { saveString } = require('./file-utils')
const { getLines } = require('./file-utils')
const subsWithBrokenTimings = getLines('./input/subtitles-with-broken-timings.sbv')
const subsWithCorrectTimings = getLines('./input/subtitles-with-correct-timing.sbv')

if (
  subsWithBrokenTimings.length !== subsWithCorrectTimings.length
) {
  console.log('ERROR')
  console.log('Files have different number of lines')
  console.log('subtitles-with-correct-timing.txt: ' + subsWithCorrectTimings.length)
  console.log('subtitles-with-broken-timings.txt: ' + subsWithBrokenTimings.length)
} else {
  const result = []
  const N = subsWithBrokenTimings.length
  for (let i = 0; i < N; i++) {
    if (subsWithCorrectTimings[i].startsWith('0:')) {
      result.push(subsWithCorrectTimings[i])
    } else {
      result.push(subsWithBrokenTimings[i])
    }
  }
  console.log(result.length)
  saveString(`./output/captions.sbv`, result.join('\n'))
}
