---
id: SubscribeProps
title: SubscribeProps
---

```ts
type SubscribeProps<TFeatures, TSelected, TSourceValue> =
  | SubscribePropsWithStore<TFeatures, TSelected>
  | SubscribePropsWithSourceIdentity<TSourceValue>
| SubscribePropsWithSourceWithSelector<TSourceValue, TSelected>;
```

Defined in: [src/Subscribe.ts:66](https://github.com/TanStack/table/blob/main/packages/react-table/src/Subscribe.ts#L66)

## Type Parameters {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* `TableFeatures`

### TSelected {#tselected}

`TSelected` = `unknown`

### TSourceValue {#tsourcevalue}

`TSourceValue` = `unknown`
