<template>
  <div>
    <div class="form-group">
      <label class="form-label" v-text="'Filepath'" />
      <input
        class="form-input"
        id="form-filepath-input"
        type="text"
        label="Filepath"
        @input="$emit('update:filepath', $event.target.value)"
        placeholder="Enter a filepath"
      />
      <label class="form-label" v-text="'Tags'" />
      <input
        class="form-input"
        id="form-tags-input"
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
    filepaths: Array,
    tags: String
  },
  methods: {
    addFilepath() {
      if (!this.validateFilepath(this.filePath)) {
        return false;
      }
      this.$emit("addFilepath");
      document.querySelector("# form-filepath-input").value = "";
      document.querySelector("# form-tag-input").value = "";
      this.$emit("update:filepath", "");
      this.$emit("update:tags", "");
    },
    validateFilepath() {
      if (!this.filepath) {
        this.$yodify({
          text: 'Enter a filepath',
            type: 'error',
        });
        return false;
      }
      let alreadyAdded = false;
      this.filepaths.forEach((file) => {
        if (file.path === this.filepath)
        this.$yodify({
          text: 'This filepath is already added.',
          type: 'error',
        });
        alreadyAdded = true;
      })
      return !  alreadyAdded;
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
