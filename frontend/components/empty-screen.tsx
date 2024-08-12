import { UseChatHelpers } from 'ai/react'

import { Button } from '@/components/ui/button'
import { ExternalLink } from '@/components/external-link'
import { IconArrowRight } from '@/components/ui/icons'

export function EmptyScreen() {
  return (
    <div className="mx-auto max-w-2xl px-4">
      <div className="flex flex-col gap-2 rounded-lg border bg-background p-8">
        <h1 className="text-lg font-semibold">
          Welcome to the RAG-powered AI Chatbot!
        </h1>
        <p className="leading-normal text-muted-foreground">
          This is an advanced AI chatbot application that utilizes Retrieval
          Augmented Generation (RAG) to provide intelligent responses based on a
          given knowledge base. It's built with{' '}
          <ExternalLink href="https://nextjs.org">Next.js</ExternalLink> and
          deployed on{' '}
          <ExternalLink href="https://aws.amazon.com/ec2/">
            AWS EC2 Servers
          </ExternalLink>
          .
        </p>
        <p className="leading-normal text-muted-foreground">
          Our chatbot leverages{' '}
          <ExternalLink href="https://aws.amazon.com/bedrock/">
            AWS Bedrock API
          </ExternalLink>{' '}
          to access powerful language models. We've implemented an LLM
          orchestration pattern with a router and task-specific models to
          enhance performance and accuracy.
        </p>
        <p className="leading-normal text-muted-foreground">
          Additional features include multi-language support, user
          authentication for personalized experiences, and a feedback mechanism
          for continuous improvement.
        </p>
      </div>
    </div>
  )
}
