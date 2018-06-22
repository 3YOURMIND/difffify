<template>
  <div class="diff-container">
    <div v-for="(file, index) in splitFiles" :key="index">
      <DiffFile
        :lines="file"
      />
    </div>
  </div>
</template>

<script>
import DiffFile from './DiffFile.vue';

export default {
  name: "DiffDisplayer",
  components: {
    DiffFile,
  },
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
    },
  },
};
</script>
