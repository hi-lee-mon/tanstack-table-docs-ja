---
id: TransformDataValueFn
title: TransformDataValueFn
---

```ts
type TransformDataValueFn = (dataValue) => any;
```

定義元: [types/type-utils.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/type-utils.ts#L15)

フィルターやソートの比較関数に渡る前に、行の値を正規化します。

`constructFilterFn` / `constructSortFn` で作ったフィルター関数やソート関数に、`resolveDataValue` として付けてください（小文字にする、発音区別符号を取り除く、など）。

## パラメーター {#parameters}

### dataValue {#datavalue}

`any`

## 戻り値 {#returns}

`any`
