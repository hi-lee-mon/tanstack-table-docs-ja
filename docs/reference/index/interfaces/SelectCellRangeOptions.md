---
id: SelectCellRangeOptions
title: SelectCellRangeOptions
---

定義元: [features/cell-selection/cellSelectionFeature.types.ts:74](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L74)

## プロパティ {#properties}

### ~~additive?~~ {#additive}

```ts
optional additive?: boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:86](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L86)

範囲を、既存の範囲を置き換えずに追加するかどうかです。既定値は `false` です。

#### 非推奨 {#deprecated}

代わりに `mode: 'include'` を使ってください。

***

### mode? {#mode}

```ts
optional mode?: CellSelectionRangeMode;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:79](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L79)

選択を置き換えるか、範囲を追加するか、範囲を差し引くかを指定します。既定値は `replace` です。
