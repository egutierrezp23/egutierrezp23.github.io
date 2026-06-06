import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Blog collection: bilingual posts authored in Markdown.
// Each post is a single .md file with bilingual frontmatter (title_en/title_es,
// summary_en/summary_es) and a body that contains BOTH languages wrapped in
// <div class="lang-en">…</div> and <div class="lang-es">…</div>. The site's
// global CSS shows only the active language via [data-site-lang].
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title_en: z.string(),
    title_es: z.string(),
    summary_en: z.string(),
    summary_es: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    // Optional metadata for posts that originated as articles in external outlets.
    original_url: z.string().url().optional(),
    original_outlet: z.string().optional(),
    original_lang: z.enum(['en', 'es']).optional(),
  }),
});

export const collections = { blog };
