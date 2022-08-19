const { dates } = require('./dates')

console.log(dates[180][0])

const START = 180

let lastAllowedDayToStayInTurkey = dates[START][0]

for (let i = START; i < dates.length; i++) {
  let daysInTurkey = 0
  for (let j = 0; j < 180; j++) {
    if (dates[i - j][1]) {
      daysInTurkey++
    }
  }
  if (90 < daysInTurkey) {
    break;
  }
  lastAllowedDayToStayInTurkey = dates[i][0]
}

console.log(`Last allowed day to stay in Turkey is ${lastAllowedDayToStayInTurkey}`)
