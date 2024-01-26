import path from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    sourcemap: true,
    lib: {
      entry: path.resolve(__dirname, 'client/main.js'),
      name: 'Ecommerce',
      fileName: (format) => `main.js`,
      formats: ['es'],
    },
    rollupOptions: {
      output: {
        dir: path.resolve(__dirname, 'website/static/website/dist'),
      }
    }
  }
})
