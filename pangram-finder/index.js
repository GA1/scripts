const s = 'Co wspólnego mają zdania:\n' +
    '\n' +
    '[show both pangrams on the screen]\n' +
    '\n' +
    '“Dość błazeństw, żrą mój pęk luźnych fig” i \n' +
    '\n' +
    '“Myślę: Fruń z płacht gąsko, jedź wbić nóż”,\n' +
    '\n' +
    'obydwa polskimi pangramami, bo zawierają każdą literę języka polskiego, nawet lepiej, są pangramami idealnymi, bo zawierają każdą literę tylko raz; jeśli nie weźmiemy pod uwagę tych dwóch pangramów idealnych to i cała moja wypowiedź z tego wideo byłaby pangramem ale brakuje mi jednej litery, której? [zoom in on my raised eyebrows]';

// Function to remove content between quotes and square brackets
function cleanText(text) {
  // Remove content between double quotes
  text = text.replace(/“[^”]*"/g, '');
  // Remove content between square brackets
  text = text.replace(/\[[^\]]*\]/g, '');
  return text;
}

// Polish alphabet with both lowercase and uppercase letters
const polishAlphabet = {
  'a': 0, 'ą': 0, 'b': 0, 'c': 0, 'ć': 0, 'd': 0, 'e': 0, 'ę': 0,
  'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'ł': 0,
  'm': 0, 'n': 0, 'ń': 0, 'o': 0, 'ó': 0, 'p': 0, 'r': 0, 's': 0,
  'ś': 0, 't': 0, 'u': 0, 'w': 0, 'y': 0, 'z': 0, 'ź': 0, 'ż': 0
};

// Clean the text first
const cleanedText = cleanText(s);

console.log(s)

// Count letters in cleaned text
for (let char of cleanedText.toLowerCase()) {
  if (char in polishAlphabet) {
    polishAlphabet[char]++;
  }
}

// Print only letters that appear in the text
for (let [letter, count] of Object.entries(polishAlphabet)) {
  if (count > 0) {
    console.log(`${letter}: ${count}`);
  }
}
