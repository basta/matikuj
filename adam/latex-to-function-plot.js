// \sqrt[n]{x} does not work and can't be done without parsing the whole thing :(
const latex_to_function_plot = latex => (latex
  .replaceAll(/\\cdot\b/gu,          '*')
  // .replaceAll(/(\d)\s*(\p{L})/gu,    (_, number, letter) => `${number}*${letter}`)
  // .replaceAll(/(\p{L})\s+(\p{L})/gu, (_, letter1, letter2) => `${letter1}*${letter2}`)
  // .replaceAll(/(?<!\\)\b\p{L}+/gu,   letters => letters.split('').join('*'))
  .replaceAll(/\\frac\{(.*?)\}\{/gu, (_, numerator) => `(${numerator})/(`)
  .replaceAll(/(?<!\\)(?!\\)\{/gu,   '(')
  .replaceAll(/(?<!\\)(?!\\)\}/gu,   ')')
  .replaceAll(/\\left|\\right|\\/gu, '')
  .replaceAll(/\bpi\b/gu, 'PI')
  .replaceAll(/\be\b/gu, 'E')
);

[
  '\\frac{1}{3}',
  '\\sqrt{2}',
  '\\frac{-b+\\sqrt{b^2-4ac}}{2a}',
  'e^{\\pi i}',
  '\\left\\{\\right\\}',
  'a^2+2\\cdot a\\cdot b+b^2',
].forEach(latex => console.log(latex_to_function_plot(latex)));
