---
id: ExternalAtoms
title: ExternalAtoms
---

```ts
type ExternalAtoms<TFeatures> = Partial<{ [K in keyof TableState<TFeatures>]: Atom<TableState<TFeatures>[K]> }>;
```

定義元: [core/table/coreTablesFeature.types.ts:64](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L64)

`TableState` のスライスごとに1つある、省略可能な外部のアトムのマップです。使う側は、どの状態スライスにも自分の書き込み可能なアトムを渡して、そのスライスを自分で持てます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
