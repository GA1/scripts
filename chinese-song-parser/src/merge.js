const {saveString} = require("./file-utils");
const { getLines } = require('./file-utils')
const simplifiedLines = getLines('./input/simplified.txt')
const traditionalLines = getLines('./input/traditional.txt')
const pinyinLines = getLines('./input/pinyin.txt')
const englishLines = getLines('./input/english.txt')

if (
  simplifiedLines.length !== traditionalLines &&
  traditionalLines.length !== pinyinLines.length &&
  pinyinLines.length !== englishLines.length
) {
  console.log(11111111111111)
  console.log('Files have different number of lines')
  console.log('simplified.txt: ' + simplifiedLines.length)
  console.log('traditionalLines.txt: ' + traditionalLines.length)
  console.log('pinyin.txt: ' + pinyinLines.length)
  console.log('english.txt: ' + englishLines.length)
} else {
  const result = []
  const N = simplifiedLines.length;
  for (let i = 0; i < N; i++) {
    result.push(simplifiedLines[i])
    result.push(traditionalLines[i])
    result.push(pinyinLines[i])
    result.push(englishLines[i])
    result.push('')
  }
  saveString('./output/result.txt', result.join('\n'))
}
