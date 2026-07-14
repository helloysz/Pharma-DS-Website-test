// @ts-check
import { defineConfig } from 'astro/config';

import cloudflare from "@astrojs/cloudflare";

// https://astro.build/config
export default defineConfig({
  site: 'https://phds.nestat.org',

  // Output a fully static site that can be hosted anywhere.
  output: 'static',

  adapter: cloudflare()
});