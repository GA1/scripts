import dotenv from 'dotenv'

dotenv.config()

const createFakeApiKeyBasedOn = (str: string): string => {
  const getRandomLower = () => String.fromCharCode(Math.floor(Math.random() * 26) + 97)
  const getRandomUpper = () => String.fromCharCode(Math.floor(Math.random() * 26) + 65)
  const getRandomDigit = () => String(Math.floor(Math.random() * 10))

  return str
    .split('')
    .map((char) => {
      if (char >= 'a' && char <= 'z') return getRandomLower()
      if (char >= 'A' && char <= 'Z') return getRandomUpper()
      if (char >= '0' && char <= '9') return getRandomDigit()
      return char
    })
    .join('')
}

console.log(createFakeApiKeyBasedOn(process.env.YOUR_REAL_SECRET || ''))
