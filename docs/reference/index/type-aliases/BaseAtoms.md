---
id: BaseAtoms
title: BaseAtoms
---

```ts
type BaseAtoms<TFeatures> = { [K in keyof TableState<TFeatures>]-?: Atom<TableState<TFeatures>[K]> };
```

定義元: [core/table/coreTablesFeature.types.ts:44](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L44)

`TableState` のスライスごとに1つある、書き込み可能なアトムのマップです。ライブラリが常に `makeStateUpdater` を通して書き込む、内部の書き込み可能なアトムです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
