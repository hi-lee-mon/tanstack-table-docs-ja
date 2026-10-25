---
id: ColumnDefTemplate
title: ColumnDefTemplate
---

```ts
type ColumnDefTemplate<TProps> = string | ((props) => any);
```

定義元: [types/ColumnDef.ts:64](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L64)

描画できる列のテンプレートの値です。

文字列はそのまま描画されます。関数は、関係するセルやヘッダーのコンテキストを受け取り、フレームワーク固有の描画結果を返せます。

## 型パラメーター {#type-parameters}

### TProps {#tprops}

`TProps` *extends* `object`
