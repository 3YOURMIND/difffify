<template>
  <table>
    <tr>
      <th v-text="Filepath"/>
      <th v-text="Tags" />
      <th />
    </tr>
    <tr v-for="(item, index) in filteredFilePaths" :key="item.path">
      <td v-text="item.path" />
      <td>
        <span v-for="tag in item.tags" :key="tag">
          <span class="diffify__file-tag" v-text="tag" />
        </span>
      </td>
      <td class="diffify__table-row--right">
        <button
          @click="removePath(item.id, index)"
          class="danger"
        >
          Remove
        </button>
      </td>
    </tr>
  </table>
</template>

<script>
import axios from "axios";

export default {
  name: "FilepathTable",
  props: {
    filepaths: Array,
    selectedTags: Array,
    backendUrl: String
  },
  computed: {
    filteredFilePaths() {
      return this.filepaths.filter(filepath => {
        return this.containsAllTags(filepath.tags, this.selectedTags);
      });
    }
  },
  methods: {
    containsAllTags(targetTags, selectedTags) {
      if (!this.selectedTags.length) {
        return true;
      }
      let result = true;
      selectedTags.forEach(selectedTag => {
        if (!targetTags.includes(selectedTag)) {
          result = false;
        }
      });
      return result;
    },
    removePath(id, index) {
      axios
        .delete(`${this.backendUrl}/filepaths/${id}/`)
        .then(response => {
          this.filepaths.splice(index, 1);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.diffify__table-row--right {
  text-align: right;
}
</style>
