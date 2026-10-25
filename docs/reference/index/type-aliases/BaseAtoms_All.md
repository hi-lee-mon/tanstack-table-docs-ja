---
id: BaseAtoms_All
title: BaseAtoms_All
---

```ts
type BaseAtoms_All = { [K in keyof TableState_All]?: Atom<Exclude<TableState_All[K], undefined>> };
```

定義元: [core/table/coreTablesFeature.types.ts:78](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L78)

アトムの型の、内部用の「全機能」入り平坦版です。`Table_Internal` はこれを使います。
そのため、（`TFeatures` についてジェネリックに書かれた）機能のコードは、どのスライスのアトム（`table.atoms.columnPinning` など）にもアクセスできます。現在の `TFeatures` のユニオンにないスライスが、TypeScript の型の絞り込みで消されることはありません。

キーは省略可能です。機能のコードは自分が持たないスライスのアトムも読めますが、そのスライスが現在のテーブルに登録されているとは限りません。
使う側はオプショナルチェーン（`table.atoms.columnPinning?.get() ?? default`）を使う必要があります。
