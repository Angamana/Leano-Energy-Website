const fs = require('fs');
const path = require('path');

const baseDir = 'C:\\Users\\angam\\Downloads\\Leano Website V1';

function searchFonts(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      searchFonts(filePath);
    } else if (file.endsWith('.css') || file.endsWith('.html')) {
      const content = fs.readFileSync(filePath, 'utf8');
      if (content.includes('font-family') || content.includes('LT Energy') || content.includes('lt-energy')) {
        const matches = content.match(/font-family:[^;\}]+/gi);
        if (matches) {
          const unique = [...new Set(matches)];
          console.log(`=== FILE: ${filePath} ===`);
          unique.slice(0, 8).forEach(m => console.log(`  ${m}`));
        }
      }
    }
  }
}

searchFonts(baseDir);
