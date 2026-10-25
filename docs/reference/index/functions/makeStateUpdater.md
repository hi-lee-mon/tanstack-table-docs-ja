---
id: makeStateUpdater
title: makeStateUpdater
---

```ts
function makeStateUpdater<TFeatures, K>(key, instance): (updater) => void;
```

定義元: [utils.ts:97](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L97)

1つの状態スライス用に、テーブルの状態のアップデーターを作成します。

このアップデーターはスライスに対応するテーブルの基底アトムに書き込み、値と関数の両方の形のアップデーターに対応します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### K {#k}

`K` *extends* `string` \| `number` \| `symbol` \| `string` & `object`

## パラメーター {#parameters}

### key {#key}

`K`

### instance {#instance}

#### baseAtoms {#baseatoms}

`object`

#### options {#options}

\{
  `atoms?`: `object`;
\}

#### options.atoms? {#optionsatoms}

`object`

## 戻り値 {#returns}

(`updater`) => `void`
