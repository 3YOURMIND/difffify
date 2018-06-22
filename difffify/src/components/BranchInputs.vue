<template>
  <div>
    <div class="form-group">
      <label class="form-label" v-text="'From'" />
      <input
        class="form-input"
        type="text"
        :value="fromBranch"
        @input="handleInput('from', $event)"
      />
      <label class="form-label" v-text="'To'" />
      <input
        class="form-input"
        type="text" :value="toBranch"
        @input="handleInput('to', $event)"
      />
    </div>
    <button
      @click="$emit('getDiff')"
      class="primary"
    >
      GET DIFF
    </button>
  </div>
</template>

<script>
export default {
  name: "BranchInputs",
  props: {
    fromBranch: String,
    toBranch: String
  },
  methods: {
    handleInput(branch, event) {
      if (branch === "from") {
        window.localStorage.setItem("fromBranch", event.target.value);
        this.$emit("update:fromBranch", event.target.value);
      } else if (branch === "to") {
        window.localStorage.setItem("toBranch", event.target.value);
        this.$emit("update:toBranch", event.target.value);
      }
    }
  },
  mounted() {
    this.$emit("update:fromBranch", window.localStorage.getItem("fromBranch"));
    this.$emit("update:toBranch", window.localStorage.getItem("toBranch"));
  }
};
</script>

<style lang="scss" scoped>

</style>
