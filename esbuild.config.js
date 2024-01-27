import * as esbuild from 'esbuild'
import postCssPlugin from 'esbuild-style-plugin'
import tailwindcss from 'tailwindcss'
import autoprefixer from 'autoprefixer';
import postcssImport from 'postcss-import';

let ctx = await esbuild.context({
  entryPoints: ['./client/main.js'],
  bundle: true,
  loader: {
    '.ttf': 'file',
    '.woff': 'file',
    '.eot': 'file',
    '.svg': 'file'
  },
  outdir: './website/static/website/dist/',
  plugins: [postCssPlugin({
    postcss: {
      plugins: [
        postcssImport,
        tailwindcss,
        autoprefixer,
      ],
    }
  })],
})

await ctx.watch();

console.log("🟢 Client server is watching for changes...");
