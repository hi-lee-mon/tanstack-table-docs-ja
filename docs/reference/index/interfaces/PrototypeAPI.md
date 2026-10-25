---
id: PrototypeAPI
title: PrototypeAPI
---

定義元: [utils.ts:567](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L567)

## 型パラメーター {#type-parameters}

### _TDeps {#_tdeps}

`_TDeps` *extends* `ReadonlyArray`\<`any`\>

### _TDepArgs {#_tdepargs}

`_TDepArgs`

## プロパティ {#properties}

### fn {#fn}

```ts
fn: (self, ...args) => any;
```

定義元: [utils.ts:568](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L568)

#### パラメーター {#parameters}

##### self {#self}

`any`

##### args {#args}

...`any`

#### 戻り値 {#returns}

`any`

***

### memoDeps? {#memodeps}

```ts
optional memoDeps?: (self, depArgs?) => any[] | undefined;
```

定義元: [utils.ts:569](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L569)

#### パラメーター {#parameters-1}

##### self {#self-1}

`any`

##### depArgs? {#depargs}

`any`

#### 戻り値 {#returns-1}

`any`[] \| `undefined`
