<template>
  <div class="branch-input-container">
    From:
    <input type="text" :value="fromBranch" @input="$emit('update:fromBranch', $event.target.value)"/>
    To:
    <input type="text" :value="toBranch" @input="$emit('update:toBranch', $event.target.value)"/>
    <button @click="$emit('getDiff')">GET DIFF</button>
  </div>
</template>

<script>
export default {
  name: 'BranchInputs',
  props: {
    fromBranch: String,
    toBranch: String
  }
}
</script>

<style lang="scss" scoped>
.branch-input-container {
  margin: 1em;
  display: flex;
  flex-direction: row;
}
</style>
