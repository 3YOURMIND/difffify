<template>
  <div class="diff-container">
    <pre v-for="line in splitDiff" :class="lineClasses(line)">{{ line }}</pre>
  </div>
</template>

<script>
export default {
  name: "DiffDisplayer",
  props: {
    diff: String
  },
  data() {
    return {};
  },
  computed: {
    splitDiff() {
      return this.diff.split("\n");
    }
  },
  methods: {
    isAddedLine(line) {
      return line[0] === "+";
    },
    isDeletedLine(line) {
      return line[0] === "-";
    },
    lineClasses(line) {
      return {
        "added-line": this.isAddedLine(line),
        "deleted-line": this.isDeletedLine(line)
      };
    }
  }
};
</script>

<style lang="scss">
pre {
  padding: 0;
  margin: 0;
}
.added-line {
  color: green;
}

.deleted-line {
  color: red;
}
</style>
