<script setup lang="ts">
// Commit of TanStack/table (main branch) that this translation covers.
const srcSha = 'c14e0221'
const srcDate = '2026-10-21'
const srcUrl = `https://github.com/TanStack/table/commit/c14e0221b1e656c7bb35e7b3d4cdf188719a3599`
const buildDate = import.meta.env.VITE_BUILD_DATE
</script>

<template>
  <div class="version-note">
    <span>非公式翻訳 · 原著 &copy; Tanner Linsley（<a href="https://github.com/TanStack/table/blob/main/LICENSE">MIT License</a>）</span>
    <span class="sep">·</span>
    <span>翻訳対象: <a :href="srcUrl" target="_blank" rel="noopener">TanStack/table@{{ srcSha }}</a>（{{ srcDate }}）</span>
    <span class="sep">·</span>
    <span>翻訳最終更新 {{ buildDate }}</span>
  </div>
</template>

<style scoped>
.version-note {
  padding: 16px 24px 24px;
  text-align: center;
  font-size: 12px;
  color: var(--vp-c-text-3);
}
.version-note a {
  color: var(--vp-c-text-2);
}
.version-note .sep {
  margin: 0 6px;
}
</style>
