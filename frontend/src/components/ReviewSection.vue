<template>
    <div class="review-section">
      <form @submit.prevent="submitReview">
        <textarea v-model="newReview.text" placeholder="Leave a review..."></textarea>
        <select v-model="newReview.rating">
          <option v-for="star in 5" :value="star">{{ star }} Stars</option>
        </select>
        <button type="submit">Submit</button>
      </form>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          <p>{{ review.text }} - {{ review.rating }} Stars</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: ["reviews"],
    data() {
      return {
        newReview: {
          text: "",
          rating: 5,
        },
      };
    },
    methods: {
      submitReview() {
        this.$emit("new-review", { ...this.newReview });
        this.newReview.text = "";
      },
    },
  };
  </script>
  