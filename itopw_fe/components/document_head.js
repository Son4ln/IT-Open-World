import React from 'react'
import NextHead from 'next/head'

const Head = props => (
  <NextHead>
    <title>{props.title || ''}</title>
  </NextHead>
)

export default Head
