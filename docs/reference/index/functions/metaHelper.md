---
id: metaHelper
title: metaHelper
---

```ts
function metaHelper<TMeta>(): TMeta;
```

定義元: [helpers/metaHelper.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/helpers/metaHelper.ts#L22)

`features` オプションの型専用スロット `tableMeta` / `columnMeta` を、型アサーションなしで宣言するためのヘルパーです。

`{} as TMeta` と同じ意味ですが、呼び出し側で型専用であることが読み取れます。また、meta の型が省略可能なプロパティだけを持つ場合に起きる `@typescript-eslint/no-unnecessary-type-assertion` の誤検知を避けられます（この場合、自動修正でアサーションが消されると、推論される meta の型が気づかないうちに `{}` に落ちてしまいます）。

戻り値は実体のない値で、実行時には無視され、テーブルに登録された機能から取り除かれます。使われるのは型だけです。

## 型パラメーター {#type-parameters}

### TMeta {#tmeta}

`TMeta` *extends* `object`

## 戻り値 {#returns}

`TMeta`

## 例 {#example}

```
import { metaHelper, tableFeatures, rowSortingFeature } from '@tanstack/react-table'
const features = tableFeatures({
  rowSortingFeature,
  tableMeta: metaHelper<MyTableMeta>(),
  columnMeta: metaHelper<MyColumnMeta>(),
});
```
