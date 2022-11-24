const { dates } = require('./dates')

console.log(dates[180][0])

const START = 70

let lastAllowedDayToStayInTurkey = dates[START][0]

for (let i = START; i < dates.length; i++) {
  let daysInTurkey = 0
  for (let j = 0; j < 180; j++) {
    if (0 < i - j && dates[i - j][1]) {
      daysInTurkey++
    }
  }
  console.log(i, daysInTurkey, dates[i][0])
  if (90 < daysInTurkey) {
    dates[i][0]
    break;
  }
  lastAllowedDayToStayInTurkey = dates[i][0]
}

console.log(`Last allowed day to stay in Turkey is ${lastAllowedDayToStayInTurkey} (on this day I have to leave)`)
