<template>
  <div class="diff-container">
    <div v-for="(line, index) in splitDiff" :key="index">
      <pre :class="lineClasses(line)">
        {{line}}
      </pre>
    </div>
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
      return this.diff.split("\n")
        .slice(2, this.diff.length)
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
        "diffify__added-line": this.isAddedLine(line),
        "diffify__deleted-line": this.isDeletedLine(line),
        "diffify__line": true
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

.diffify__line {
  font-size: 0.875em;
}
.diffify__added-line {
  color: green;
}

.diffify__deleted-line {
  color: red;
}
</style>
