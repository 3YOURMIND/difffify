<template>
  <div>
    <div class="form-group">
      <label class="form-label" v-text="'Filepath'" />
      <input
        class="form-input"
        type="text"
        label="Filepath"
        @input="$emit('update:filepath', $event.target.value)"
        placeholder="Enter a filepath"
      />
      <label class="form-label" v-text="'Tags'" />
      <input
        class="form-input"
        type="text"
        @input="$emit('update:tags', $event.target.value)"
        placeholder="Enter some tags, separated by commas"
      />
    </div>
    <button
      @click="addFilepath"
      class="secondary"
    >
      ADD
    </button>
  </div>
</template>

<script>
export default {
  name: "FileInputs",
  props: {
    filepath: String,
    tags: String
  },
  methods: {
    addFilepath() {
      this.$emit("addFilepath");
      this.$emit("update:filepath", "");
      this.$emit("update:tags", "");
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
