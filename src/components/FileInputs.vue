<template>
  <div>
    <div class="form-group">
      <label class="form-label" v-text="'Filepath'" />
      <input
        class="form-input"
        type="text"
        label="FilePath"
        @input="$emit('update:filePath', $event.target.value)"
        placeholder="Enter a filepath"
      />
      <label class="form-label" v-text="'Tags'" />
      <input
        class="form-input"
        type="text"
        @input="$emit('update:tags', commaSeparatedTags($event.target.value))"
        placeholder="Enter some tags, separated by commas"
      />
    </div>
    <button
      @click="$emit('addFilePath')"
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
    filePath: String,
    tags: Array
  },
  methods: {
    commaSeparatedTags(tagString) {
      return tagString.split(",");
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
