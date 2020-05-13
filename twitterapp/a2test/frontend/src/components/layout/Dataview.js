import React, {Component} from 'react';

export class Dataview extends Component {
    renderTweets() {
        const tweets = Object.values(this.props.tweets);
        return tweets.map((n) => <div><h2>{n.text}</h2></div>);
    }

    render() {
        return (
            <div>
                { this.renderTweets() }
                {/* <p>
                    {tweets[0].text}
                </p> */}
            </div>
        )
    }

}

export default Dataview