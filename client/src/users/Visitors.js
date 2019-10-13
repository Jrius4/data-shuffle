import React from 'react'
import ApolloClient from 'apollo-boost';
import {ApolloProvider} from 'react-apollo'
import {Query} from 'react-apollo'
import gql from 'graphql-tag'


const client = new ApolloClient({
    uri:'http://127.0.0.1:8000/graphql/visitors/'
})

const Visitors = () => {
  return (
    <ApolloProvider client={client}>
      <Query query={gql`
            {
                visitors{
                    id
                    username
                    country
                }
            }
      `}
      >
          {({loading, error, data})=>{
            if(loading) return <p>Loading ...</p>;
            if(error) return <p>Error :( {console.log(error)} ...</p>;
            
                return data.visitors.map(({id,username,country})=>(
                    <div key={id}>
                        <span>{username}</span><br/>
                        <span>{country}</span><br/>
                    </div>
                ))
        }}
      </Query>
    </ApolloProvider>
  )
}

export default Visitors
