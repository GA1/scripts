const text = 'Myślę: fruń z płacht gąsko, \n' +
    'jedź wbić nóż.';

// Function to remove content between quotes and square brackets
function cleanText(text) {
  return text
      .replace(/\[[^\]]*\]/g, '') // Remove content in square brackets first
      .replace(/"[^"]*"/g, '') // Then remove content in quotes
      .replace(/[,;:?]/g, '') // Remove punctuation
      .replace(/\s+/g, ' ') // Replace multiple spaces with single space
      .trim(); // Remove leading/trailing spaces
}

// Polish alphabet with both lowercase and uppercase letters
const polishAlphabet = {
  'a': 0, 'ą': 0, 'b': 0, 'c': 0, 'ć': 0, 'd': 0, 'e': 0, 'ę': 0,
  'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'ł': 0,
  'm': 0, 'n': 0, 'ń': 0, 'o': 0, 'ó': 0, 'p': 0, 'r': 0, 's': 0,
  'ś': 0, 't': 0, 'u': 0, 'w': 0, 'y': 0, 'z': 0, 'ź': 0, 'ż': 0
};

// Clean the text first
const cleanedText = cleanText(text);
console.log('Cleaned text:', cleanedText);

// Count total letters
let totalLetters = 0;

// Count letters in cleaned text
for (let char of cleanedText.toLowerCase()) {
  if (char in polishAlphabet) {
    polishAlphabet[char]++;
    totalLetters++;
  }
}

// Find missing letters (those with count 0)
const missingLetters = Object.entries(polishAlphabet)
    .filter(([_, count]) => count === 0)
    .map(([letter]) => letter);

console.log('\nTotal letters:', totalLetters);
console.log('Missing letters:', missingLetters.join(', '));
