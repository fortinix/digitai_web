import { execSync } from 'child_process';
import { join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const projectRoot = join(__dirname, '..');

console.log('==========================================');
console.log('Installing DigiAI Web Project Dependencies');
console.log('==========================================\n');

try {
  // Install webapp dependencies
  console.log('📦 [1/2] Installing webapp dependencies...');
  execSync('npm install', { cwd: join(projectRoot, 'webapp'), stdio: 'inherit' });
  console.log('✓ Webapp dependencies installed\n');

  // Install new-frontend dependencies
  console.log('📦 [2/2] Installing new-frontend dependencies...');
  execSync('npm install', { cwd: join(projectRoot, 'new-frontend'), stdio: 'inherit' });
  console.log('✓ New-frontend dependencies installed\n');

  console.log('==========================================');
  console.log('✓ All dependencies installed successfully!');
  console.log('==========================================\n');

  console.log('To run the project:');
  console.log('  - Frontend (Vite):  cd new-frontend && npm run dev');
  console.log('  - Backend (Express): cd webapp && npm run dev');
  console.log('');
  console.log('Frontend will be available at: http://localhost:3000');
  console.log('Backend will be available at: http://localhost:5000');

} catch (error) {
  console.error('❌ Error during installation:', error.message);
  process.exit(1);
}
