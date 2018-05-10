<template>
  <div class="filepath-input-container">
    <input
      type="text"
      label="FilePath"
      @input="$emit('update:filePath', $event.target.value)"
      placeholder="Enter a filepath"
    />
    <input
      type="text"
      @input="$emit('update:tags', commaSeparatedTags($event.target.value))"
      placeholder="Enter some tags, separated by commas"
    />
    <button @click="$emit('addFilePath')">
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
.filepath-input-container {
  margin: 1em;
}
</style>
