/**
 * Created by WillieTran on 3/22/15.
 */

var FeedBox = React.createClass({
	loadPostsFromServer: function() {
		$.ajax({
			url: this.props.url,
			type: 'GET',
			dataType: 'json',
			success: function(data) {
				this.setState({data:data});
				console.log(data);
			}.bind(this),
			error: function(xhr, status, err) {
				console.error(status, err.toString());
				console.log("bad");
			}.bind(this)
		});
	},
	    getInitialState: function() {
    	return {data: []};
    },
    componentDidMount: function() {
    	this.loadPostsFromServer();
    },
  	render: function() {
	    return(
	        <div className="FeedBox">
	          <h1>Testing two</h1>
	        </div>
	    )
    }
});

React.render(
    <FeedBox url="/posts/"/>,
    document.getElementById('feed')
);