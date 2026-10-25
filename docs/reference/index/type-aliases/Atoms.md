---
id: Atoms
title: Atoms
---

```ts
type Atoms<TFeatures> = { [K in keyof TableState<TFeatures>]-?: ReadonlyAtom<TableState<TFeatures>[K]> };
```

定義元: [core/table/coreTablesFeature.types.ts:55](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L55)

`TableState` のスライスごとに1つある、読み取り専用の派生アトムのマップです。それぞれ、対応する `baseAtom` と、スライスごとの外部のアトムまたは外部の状態の値（指定されていれば）から導き出されます。

優先順位: `options.atoms[key]` > `options.state[key]` > `baseAtoms[key]`。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
