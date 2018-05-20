<template>
  <div id="app">
    <h1 v-text="header"></h1>
    <div class="columns">
      <div class="column col-4">
        <BranchInputs
          :fromBranch.sync="fromBranch"
          :toBranch.sync="toBranch"
          @getDiff="getDiff"
        />
      </div>
      <div class="column col-8">
        <FileInputs
          :filepath.sync="newFilepath"
          :tags.sync="newTags"
          @addFilepath="addNewFilepath"
          :filepaths="filepaths"
        />
      </div>
    </div>
    <FilepathTable
      :filepaths="filepaths"
      :selectedTags="selectedTags"
      :backendUrl="backendUrl"
    />
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

import BranchInputs from "./components/BranchInputs.vue";
import FileInputs from "./components/FileInputs.vue";
import FilepathTable from "./components/FilepathTable.vue";
import DiffDisplayer from "./components/DiffDisplayer";

export default {
  name: "app",
  components: {
    BranchInputs,
    FileInputs,
    FilepathTable,
    DiffDisplayer
  },
  data() {
    return {
      header: "diff generator",
      filepaths: [],
      backendUrl: "Http://localhost:8000/api",
      fromBranch: "",
      toBranch: "release",
      selectedTags: [],
      newSelectedTag: "",
      newFilepath: "",
      newTags: "",
      showDiff: false,
      diff: ""
    };
  },
  methods: {
    addNewTag() {
      this.selectedTags.push(this.newSelectedTag);
      this.newSelectedTag = "";
    },
    removeTag(index) {
      this.selectedTags.splice(index, 1);
    },
    addNewFilepath() {
      const payload = {
        path: this.newFilepath,
        tags: this.commaSeparatedTags(this.newTags),
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
          this.getAllFilepaths();
        })
        .catch(error => {
          console.log(error);
        });
    },
    commaSeparatedTags(tagString) {
      return tagString.split(",");
    },
    getAllFilepaths() {
      axios
        .get(`${this.backendUrl}/filepaths/`)
        .then(response => {
          this.filepaths = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getDiff() {
      axios
        .get(
          `${this.backendUrl}/diff?from-version=${this.fromBranch}&to-version=${
            this.toBranch
          }`
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
    this.getAllFilepaths();
  }
};
</script>

<style lang="scss">
body {
  margin: 3% 10%;
}

.diffify__file-tag {
  border-radius: 5px;
  background-color: #2c66c4;
  color: #fff;
  margin: 0.25em;
  padding: 0.25em;
}

.tag-container {
  direction: rtl;
}
</style>
