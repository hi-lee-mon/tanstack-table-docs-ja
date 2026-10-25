---
id: getDefaultColumnSizingColumnDef
title: getDefaultColumnSizingColumnDef
---

```ts
function getDefaultColumnSizingColumnDef(): object;
```

定義元: [features/column-sizing/columnSizingFeature.utils.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-sizing/columnSizingFeature.utils.ts#L47)

列定義のための、組み込みの幅の既定値を作ります。

列定義やテーブルの既定値で上書きしない限り、列の既定値は `size: 150`、`minSize: 20`、`maxSize: Number.MAX_SAFE_INTEGER` です。

## 戻り値 {#returns}

`object`

### maxSize {#maxsize}

```ts
maxSize: number = Number.MAX_SAFE_INTEGER;
```

### minSize {#minsize}

```ts
minSize: number = 20;
```

### size {#size}

```ts
size: number = 150;
```

## 例 {#example}

```ts
const defaults = getDefaultColumnSizingColumnDef()
```
