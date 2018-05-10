<template>
  <div id="app">
    <h1>{{ header }}</h1>
    <BranchInputs
      :fromBranch.sync="fromBranch"
      :toBranch.sync="toBranch"
      @getDiff="getDiff"
    />
    <FileInputs
      :filePath.sync="newFilePath"
      :tags.sync="newTags"
      @addFilePath="addNewFilePath"
    />
    <table>
      <tr>
        <th>
          filepath:
        </th>
        <th>
          tags:
        </th>
        <th>
        </th>
      </tr>
      <tr v-for="(item, index) in filteredFilePaths" :key="item.path">
        <td>
          {{ item.path }}
        </td>
        <td>
          <span v-for="tag in item.tags" :key="tag">
            {{ tag }}<br>
          </span>
        </td>
        <td>
          <button @click="removePath(item.id, index)">Remove</button>
        </td>
      </tr>
    </table>
    <div class="tag-container">
      <button @click="addNewTag">ADD TAG</button>
      <input type="text" v-model="newSelectedTag" placeholder="Enter tags to filter by here">
      <ul>
        <li v-for="(tag, index) in selectedTags" :key="tag">
          {{ tag }} <button @click="removeTag(index)">Remove</button>
        </li>
      </ul>
    </div>
    <DiffDisplayer
      v-if="showDiff"
      :diff="diff"
    />
  </div>
</template>

<script>
import axios from "axios";

import BranchInputs from './components/BranchInputs.vue';
import FileInputs from "./components/FileInputs.vue";
import DiffDisplayer from "./components/DiffDisplayer";

export default {
  name: "app",
  components: {
    BranchInputs,
    FileInputs,
    DiffDisplayer
  },
  data() {
    return {
      header: "diffify",
      filePaths: [],
      backendUrl: "Http://localhost:8000/api",
      fromBranch: "",
      toBranch: "release",
      selectedTags: [],
      newSelectedTag: "",
      newFilePath: "",
      newTags: [],
      showDiff: false,
      diff: ""
    };
  },
  computed: {
    filteredFilePaths() {
      return this.filePaths.filter(filePath => {
        return this.containsAllTags(filePath.tags, this.selectedTags);
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
    addNewTag() {
      this.selectedTags.push(this.newSelectedTag);
      this.newSelectedTag = "";
    },
    removeTag(index) {
      this.selectedTags.splice(index, 1);
    },
    addNewFilePath() {
      const payload = {
        path: this.newFilePath,
        tags: this.newTags,
        additionalInfo: {
          additionalProp1: "string",
          additionalProp2: "string",
          additionalProp3: "string"
        }
      };
      axios
        .post(`${this.backendUrl}/filepaths/`, payload)
        .then(response => {
          console.log("hello");
          this.getAllFilePaths();
        })
        .catch(error => {
          console.log(error);
        });
    },
    removePath(id, index) {
      axios
        .delete(`${this.backendUrl}/filepaths/${id}/`)
        .then(response => {
          this.filePaths.splice(index, 1);
        })
        .catch(error => {
          console.log(error);
        });
    },
    getAllFilePaths() {
      axios
        .get(`${this.backendUrl}/filepaths/`)
        .then(response => {
          this.filePaths = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getDiff() {
      axios
        .get(
          `${this.backendUrl}/diff?from-version=${
            this.fromBranch
          }&to-version=${this.toBranch}`
        )
        .then(response => {
          this.diff = response.data.diff;
          this.showDiff = true;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getAllFilePaths();
  }
};
</script>

<style lang="scss">
body {
  margin: 3% 10%;
}

.tag-container {
  direction: rtl;
}
</style>
