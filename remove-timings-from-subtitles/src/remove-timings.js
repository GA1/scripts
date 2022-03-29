const { saveString } = require('./file-utils')
const { getLines } = require('./file-utils')
const inputSubtitles = getLines('./input/captions.sbv')

const result = []
const N = inputSubtitles.length
for (let i = 0; i < N; i++) {
  const line = inputSubtitles[i]
  if (line !== '\n' && !line.startsWith('0:')) {
    result.push(line)
  }
}
console.log(result.length)
saveString(`./output/captions.sbv`, result.join(' '))
