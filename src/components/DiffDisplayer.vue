<template>
  <div class="diff-container">
    <div v-for="(line, index) in splitDiff" :key="index">
    <div class="columns">
      <div class="column col-1" :class="blockClasses(line)">

      </div>
      <div class="column col-11">
        <pre :class="lineClasses(line)">
          {{line}}
        </pre>
      </div>
    </div>
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
      const diffLines = this.diff.split("\n");
      return diffLines;
    },
    diffFileStartIndexes() {
      const results = []
      this.splitDiff.forEach((line, index) => {
        if (line.startsWith("diff --git")) {
          results.push(index);
        }
      });
      return results;
    },
    splitFiles() {
      const files = []
      let tempFile = []
      this.splitDiff.forEach((line, index) => {
        if (this.diffFileStartIndexes.includes(index) && index !== 0) {
          files.push(Array.from(tempFile));
          tempFile = []
        }
        tempFile.push(line);
        if (index === this.splitDiff.length - 1) {
          files.push(Array.from(tempFile));
        }
      });
      return files;
    },
    diffLineNumberResolver() {
      return this.diffFileStartIndexes.map((line) => {
        return line + 4;
      });
      // const lineNumberGroups = this.splitDiff.filter((line) => {
      //   const re = new Regex(/@@\s-(\d+),(\d+)\s+\+(\d+),(\d+)\s@@/);

      // });
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
        "diffify__filestart-line": this.isDeletedLine(line),
        "diffify__line": true
      };
    },
    blockClasses(line) {
      return {
        column: true,
        'col-1': true,
        "diffify__added-line-block": this.isAddedLine(line),
        "diffify__deleted-line-block": this.isDeletedLine(line),
        "diffify__filestart-line-block": this.isDeletedLine(line),
      }
    }
  }
};
</script>

<style lang="scss">
pre {
  padding: 0;
  margin: 0;
  line-height: 1em;
  font-size: 0.875em;
}

.column {
  padding:0;
  margin:0;
}

.diffify__line {
  font-size: 0.875em;
  overflow: hidden;
}
.diffify__added-line {
  color: green;
}

.diffify__deleted-line {
  color: red;
}

.diffify__deleted-line {
}

.diffify__added-line-block {
  background-color: green;
}

.diffify__deleted-line-block {
  background-color: red;
}
</style>
