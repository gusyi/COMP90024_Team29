function loadInfo() {
    var date = "{{ collection.date|escapejs }}";
    var tweet_counts = "{{ collection.tweetcounts|escapejs }}";
    var approval_rate = "{{ collection.approval_rate|escapejs }}";
    var city_name = "{{ collection.cityname|escapejs }}";
    console.log(date);
    console.log(tweet_counts);
    console.log(approval_rate);
    console.log(city_name);
    console.log(city_info["city"]);
}