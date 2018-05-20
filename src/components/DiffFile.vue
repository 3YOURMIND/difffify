<template>
  <div class="file-diff-container">
    <h3 v-text="cleanedFileName" class="diffify-diff-filename"/>
    <div v-for="(line, index) in cleanedLines" :key="index">
      <div class="columns">
        <div :class="blockClasses(line)">
          <div
            v-if="isLineNumberLine(line)"
            v-text="isLineNumberLine(line).fromFileStartLineNumber"
          />
        </div>
        <div class="column col-11">
          <pre :class="lineClasses(line)" v-text="line" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DiffFile',
  props: {
    lines: Array,
  },
  computed: {
    cleanedFileName() {
      const splitName = this.lines[0].split(' ');
      return splitName[3].slice(2, splitName[3].length);
    },
    cleanedLines() {
      return this.lines.slice(4, this.lines.length);
    },
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
        "diffify-line-block": true,
        "diffify__added-line-block": this.isAddedLine(line),
        "diffify__deleted-line-block": this.isDeletedLine(line),
        "diffify__filestart-line-block": this.isDeletedLine(line),
      }
    },
    isLineNumberLine(line) {
      const re = new RegExp(/@@\s-(\d+),(\d+)\s+\+(\d+),(\d+)\s@@/);
      const groups = line.match(re);
      if (groups) {
        const lineNumbers = {
          fromFileStartLineNumber: groups[1],
          fromFileNumberOfLines: groups[2],
          toFileStartLineNumber: groups[3],
          toFileNumberOfLines: groups[4]
        };
      return lineNumbers;
      }
      return null;
    }
  }
};
</script>

<style lang="scss" scoped>
pre {
  padding: 0;
  margin: 0;
}

.file-diff-container {
  margin-top: 2em;
  background-color: #FFF;
  border: 1px solid #DBDBDB;
  border-radius: 5px;
  overflow-x: scroll;
}

.columns {
  margin: 0;
}

.column {
  padding:0;
  margin:0;
}

.diffify-diff-filename {
  padding: 0.5em;
}

.diffify__line {
  font-size: 0.875em;
  background-color: inherit;
  overflow-y: hidden;
}

.diffify__added-line {
  background-color: #dfd
}

.diffify__deleted-line {
  background-color: #fee8e9;
}

.diffify-line-block {
  text-align: center;
  font-weight: bold;
}

.diffify__added-line-block {
  background-color: #dfd;
  color: #FFF
}

.diffify__deleted-line-block {
  background-color: #fee8e9;
  color: #FFF
}
</style>
