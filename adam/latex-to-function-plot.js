const latex_to_function_plot = latex => (latex
  .replaceAll(/\\cdot\b/g, '*')
  .replaceAll(/(\d)\s*(\p{L})/gu, (_, number, letter) => `${number}*${letter}`)
  .replaceAll(/(\p{L})\s+(\p{L})/gu, (_, letter1, letter2) => `${letter1}*${letter2}`)
  .replaceAll(/(?<!\\)\b\p{L}+/gu, letters => letters.split('').join('*'))
  .replaceAll(/\\frac\{(.*?)}\{/g, (_, numerator) => `(${numerator})/(`)
  .replaceAll(/(?<!\\)(?!\\){/g, '(')
  .replaceAll(/(?<!\\)(?!\\)}/g, ')')
  .replaceAll(/\\left|\\right|\\/g, '')
);

[
  '\\frac{1}{3}',
  '\\sqrt{2}',
  '\\frac{-b+\\sqrt{b^2-4ac}}{2a}',
  'e^{\\pi i}',
  '\\left\\{\\right\\}',
].forEach(latex => console.log(latex_to_function_plot(latex)));
