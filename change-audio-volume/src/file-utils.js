const fs = require('fs')

function getLines(filePath) {
  const text = fs.readFileSync(filePath,'utf8')
  return text.split('\n').filter(line => line !== '\n' && line !== '')
}

function saveString(filePath, stringToSave) {
  fs.writeFile(filePath, stringToSave, (error) => {
    if (error) {
      console.log('ERROR: ' + error)
    } else {
      console.log('SUCCESS SAVING FILE AS: ' + filePath)
    }
  })
}

module.exports.getLines = getLines
module.exports.saveString = saveString
