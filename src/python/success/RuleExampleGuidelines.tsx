RuleExampleGuidelinesSection.css.ts
import { style } from '@vanilla-extract/css'
import { bodySmall, bodyMediumStrong } from 'core/theme/Fonts.css'
import { colors } from 'core/theme/Colors.css'
import { fullContainer, nLineEllipsis, singleLineEllipsis } from 'core/theme/CommonStyles.css'

export const sectionContainer = style({
  ...fullContainer,
  display: 'flex',
  flexDirection: 'column',
  gap: '24px',
  padding: '20px',
})

export const cardTitleStyle = style({
  ...bodyMediumStrong,
  color: colors.textPrimary,
  marginBottom: '4px',
})

export const cardContentStyle = style({
  ...bodySmall,
  color: colors.textSecondary,
})

export const cardContainer = style({
  padding: '16px',
})

export const characterLimitStyle = style({
  ...singleLineEllipsis,
  ...bodySmall,
  color: colors.textSecondary,
  textAlign: 'right',
  marginTop: '8px',
})


RuleExampleGuidelinesSection.tsx
import React from 'react'
import ContentCard from 'web/elements/ContentCard'
import Typography from 'web/elements/Typography'
import * as styles from './RuleExampleGuidelinesSection.css'
import Form from 'web/elements/Form'
import Input from 'web/elements/Input'

const RuleExampleGuidelinesSection: React.FC = () => {
  // Dummy function for updating the character count.
  const handleCharacterChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    // The logic for updating the character limit will go here.
  }
  
  return (
    <div className={styles.sectionContainer}>
      <ContentCard
        title={<div className={styles.cardTitleStyle}>Rule</div>}
        body={
          <>
            <Typography.Paragraph className={styles.cardContentStyle}>
              If a question is unclear, ask for more details to confirm your understanding before answering.
            </Typography.Paragraph>
            <Form.Item>
              <Input.TextArea placeholder="906 characters remaining" onChange={handleCharacterChange} maxLength={1000} />
            </Form.Item>
            <div className={styles.characterLimitStyle}>906 characters remaining</div>
          </>
        }
        className={styles.cardContainer}
      />
      <ContentCard
        title={<div className={styles.cardTitleStyle}>Example</div>}
        body={
          <Typography.Paragraph className={styles.cardContentStyle}>
            If a question is unclear, ask for more details to confirm your understanding before answering.
            <br/>
            If you don't know the answer, recommend contacting admin@acme.com as the next step.
            <br/>
            Generate answers with an emphasis on information from the last month.
          </Typography.Paragraph>
        }
        className={styles.cardContainer}
      />
      <ContentCard
        title={<div className={styles.cardTitleStyle}>Guidelines</div>}
        body={
          <Typography.Paragraph className={styles.cardContentStyle}>
            <ul>
              <li>Use simple, instructive English commands.</li>
              <li>Do not include special characters.</li>
            </ul>
          </Typography.Paragraph>
        }
        className={styles.cardContainer}
      />
    </div>
  )
}

export default RuleExampleGuidelinesSection