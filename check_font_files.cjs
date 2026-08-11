const fs = require('fs');
const path = require('path');

const baseDir = 'C:\\Users\\angam\\Downloads\\Leano Website V1';

function findFonts(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      findFonts(filePath);
    } else if (file.match(/\.(ttf|woff|woff2|eot|otf)$/i) || file.includes('LT Energy') || file.includes('LT-Energy')) {
      console.log(`Font file: ${filePath}`);
    }
  }
}

findFonts(baseDir);
