import React, {Component} from 'react'
import Head from '../components/document_head'
import '../static/css/styles.scss'

export default class Home extends Component {
  render() {
    return (
      <div>
        <Head title="Home"/>
        <p className="text-blue">HOME PAGEc is here!</p>
      </div>
    )
  }
}
