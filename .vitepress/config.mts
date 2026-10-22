import { defineConfig, type DefaultTheme } from 'vitepress'
import { execSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const VP = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.dirname(VP)
const OFFICIAL = 'https://tanstack.com/table/latest/docs/'

const git = (args: string, fallback = ''): string => {
  try {
    return execSync(`git ${args}`, { cwd: REPO }).toString().trim()
  } catch {
    return fallback
  }
}
process.env.VITE_BUILD_DATE = git('log -1 --format=%cs', 'unknown')

type Section = {
  label: string
  collapsed: boolean
  items: { label: string; to: string }[]
}
// 上流 docs/config.json から React 向けの項目だけを抜き出したもの
const SECTIONS: Section[] = JSON.parse(
  fs.readFileSync(path.join(VP, 'sidebar.json'), 'utf8')
)

const SECTION_LABELS: Record<string, string> = {
  'Getting Started': 'はじめに',
  'Core Guides': 'コアガイド',
  'Feature Guides': '機能ガイド',
  'API Reference': 'API リファレンス',
  'Table API Reference': 'Table API',
  'Column API Reference': 'Column API',
  'Row API Reference': 'Row API',
  'Cell API Reference': 'Cell API',
  'Header API Reference': 'Header API',
  'Features API Reference': 'Features API',
  'Static Functions API Reference': '静的関数 API',
  'Legacy API Reference': 'レガシー API',
  'Basic Examples': '基本のサンプル（公式サイト）',
  'Feature Examples': '機能別サンプル（公式サイト）',
  'Specialized Examples': '応用サンプル（公式サイト）',
  'Component Library Examples': 'コンポーネントライブラリのサンプル（公式サイト）',
}

// API 名そのままのラベルは訳さない。ここに無いラベルは原文のまま表示する
const ITEM_LABELS: Record<string, string> = {
  Overview: '概要',
  Installation: 'インストール',
  Devtools: 'Devtools',
  'Agent Skills (TanStack Intent)': 'エージェントスキル（TanStack Intent）',
  'Quick Start': 'クイックスタート',
  'Migrating to V9': 'V9 への移行',
  'useLegacyTable Guide': 'useLegacyTable ガイド',
  Features: '機能（features）',
  Data: 'データ',
  'Client-Side vs Server-Side': 'クライアントサイドとサーバーサイド',
  'Column Definitions': '列定義',
  'Table Instance': 'テーブルインスタンス',
  'Row Models': '行モデル',
  'Worker Row Models (Experimental)': 'Worker 行モデル（実験的）',
  Rows: '行',
  Cells: 'セル',
  'Header Groups': 'ヘッダーグループ',
  Headers: 'ヘッダー',
  Columns: '列',
  'Table and Column Meta': 'テーブルと列のメタ情報',
  'Type Helpers': '型ヘルパー',
  'Table State': 'テーブルの状態',
  'React Compiler': 'React Compiler',
  'Composable Tables (createTableHook)': '組み立て式テーブル（createTableHook）',
  'Table Context': 'テーブルコンテキスト',
  FlexRender: 'FlexRender',
  'Custom Plugins': 'カスタムプラグイン',
  'Cell Selection': 'セル選択',
  'Cell Spanning': 'セル結合',
  'Column Ordering': '列の並べ替え',
  'Column Pinning': '列の固定',
  'Column Sizing': '列幅',
  'Column Resizing': '列幅の変更',
  'Column Visibility': '列の表示切り替え',
  'Column Filtering': '列フィルター',
  'Global Filtering': 'グローバルフィルター',
  'Fuzzy Filtering': 'あいまい検索フィルター',
  Faceting: 'ファセット',
  Aggregation: '集計',
  Grouping: 'グループ化',
  Expanding: '行の展開',
  Pagination: 'ページネーション',
  'Row Pinning': '行の固定',
  'Row Selection': '行選択',
  Sorting: 'ソート',
  Virtualization: '仮想化',
  'Core API Reference': 'コア API リファレンス（英語）',
  'React API Reference': 'React API リファレンス',
  'Static Functions Overview': '静的関数の概要（英語）',
  'Legacy API Overview': 'レガシー API の概要',
}

function sidebar(): DefaultTheme.SidebarItem[] {
  return SECTIONS.map((s) => {
    const external = s.items.every((i) => i.to.includes('/examples/'))
    return {
      text: SECTION_LABELS[s.label] ?? s.label,
      collapsed: s.collapsed || external,
      items: s.items.map((i) => ({
        text: ITEM_LABELS[i.label] ?? i.label,
        link: i.to.includes('/examples/') ? OFFICIAL + i.to : `/docs/${i.to}`,
      })),
    }
  })
}

export default defineConfig({
  title: 'TanStack Table v9 非公式日本語ドキュメント',
  description: 'TanStack Table v9（React）公式ドキュメントの非公式日本語翻訳',
  lang: 'ja',
  srcDir: '.',
  base: process.env.VP_BASE || '/',
  ignoreDeadLinks: true,
  cleanUrls: true,
  srcExclude: [
    '**/node_modules/**',
    '.github/**',
    '.vitepress/**',
    'README.md',
    'TRANSLATING.md',
    'LICENSE.md',
    'docs/adr/**',
  ],
  vite: {
    plugins: [
      {
        name: 'vue-interpolation-guard',
        enforce: 'pre',
        transform(code, id) {
          if (!id.endsWith('.md')) return
          // インラインコード中の `{{` は Vue の補間として解釈されるため、ゼロ幅スペースで崩す
          return code.replace(/`[^`\n]*`/g, (s) =>
            s.replace(/\{\{/g, '{​{').replace(/\}\}/g, '}​}')
          )
        },
      },
    ],
  },
  themeConfig: {
    siteTitle: 'TanStack Table v9 非公式',
    nav: [
      { text: 'ドキュメント', link: '/docs/overview' },
      { text: 'クイックスタート', link: '/docs/framework/react/quick-start' },
      { text: 'React API', link: '/docs/framework/react/reference/index' },
      { text: '用語集', link: '/GLOSSARY' },
      { text: '公式サイト', link: 'https://tanstack.com/table/latest' },
    ],
    sidebar: { '/docs/': sidebar() },
    search: { provider: 'local' },
    outline: { level: [2, 3], label: 'このページの内容' },
    docFooter: { prev: '前のページ', next: '次のページ' },
    editLink: {
      pattern: 'https://github.com/hi-lee-mon/tanstack-table-docs-ja/edit/main/:path',
      text: 'このページを編集',
    },
    lastUpdated: { text: '最終更新', formatOptions: { dateStyle: 'short' } },
    footer: {
      message:
        '非公式翻訳です。正確な情報は <a href="https://tanstack.com/table/latest">tanstack.com/table</a> を参照してください。',
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/hi-lee-mon/tanstack-table-docs-ja' },
    ],
  },
})
