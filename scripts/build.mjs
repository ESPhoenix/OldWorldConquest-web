import { cp, mkdir, rm } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';

const root = process.cwd();
const output = resolve(root, 'dist');

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });

async function copyFile(source, destination) {
  const target = resolve(output, destination);
  await mkdir(dirname(target), { recursive: true });
  await cp(resolve(root, source), target);
}

async function copyDirectory(source, destination) {
  await cp(resolve(root, source), resolve(output, destination), { recursive: true });
}

await copyFile('Conquest-Roster.html', 'index.html');
await copyFile('ATTRIBUTION.md', 'ATTRIBUTION.md');
await copyFile('old-world-builder/LICENSE.md', 'old-world-builder/LICENSE.md');
await copyDirectory('old-world-builder/src/assets', 'old-world-builder/src/assets');
await copyFile(
  'old-world-builder/src/components/rules-index/rules-index-export.json',
  'old-world-builder/src/components/rules-index/rules-index-export.json',
);
await copyFile('old-world-builder/src/utils/rules.js', 'old-world-builder/src/utils/rules.js');
await copyDirectory(
  'old-world-builder/public/games/the-old-world',
  'old-world-builder/public/games/the-old-world',
);
