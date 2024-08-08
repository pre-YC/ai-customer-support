'use client'//use state
import Image from "next/image";

//get state var
import {useState} from 'react'
import {Box, Stack} from '@mui/material'

export default function Home() {
  const [messages, setMessages] = useState({
    role: 'assistant',
    content: `Hi I'm the Headstarter support agent, how can I assist you today?`
  })
  const [message, setMessage] = useState('')

  return (
  <Box>
    width=
  </Box>
  )
}
