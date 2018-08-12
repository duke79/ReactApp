import React from 'react';
import IssuesDOM from './IssuesDOM'

/*Redux*/
import { connect } from 'react-redux'
import { loadIssuesList } from '../../redux/actions/actions'
/*Apollo*/
import gql from "graphql-tag";
import { Query } from "react-apollo";



const GET_USERS = gql`
  query GET_USERS($prefix: String!) {
      users (prefix:$prefix) {
        name
      }
    }
  `


class Issues extends React.Component {

  componentWillReceiveProps(nextProps) {
    console.log("props are going to be updated")
    this.setState(() => {
      console.log("Issues being updated...");
    });
  }

  componentDidMount() {
    const { dispatch } = this.props;
    dispatch(loadIssuesList(""));
  }

  render() {
    const { StoreIssues } = this.props;

    return (
      <Query query={GET_USERS} variables={{ prefix: "b" }}>
        {({ loading, error, data }) => {
          if (loading) return "Loading...";
          if (error) return `Error! ${error.message}`;
          console.log(data);
          return <IssuesDOM {...this.props}/>
        }}
      </Query>
    )
  }
}

Issues.defaultProps = {
  "open_issues": "6",
  "close_issues": "3,592",
  "filters": ["Sort", "Asignee", "Milestones", "Projects", "Labels", "Author"]
}

function select(state) {
  return {
    StoreIssues: state.Issues
  }
}

export default connect(select)(Issues);