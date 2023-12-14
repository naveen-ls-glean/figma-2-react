AppEntityNameSection.css.ts
```typescript
import { style } from '@vanilla-extract/css'
import { bodyMedium, heading5 } from 'core/theme/Fonts.css'
import { fullContainer } from 'core/theme/CommonStyles.css'

export const container = style({
    ...fullContainer,
    flexDirection: 'column',
    display: 'flex',
    gap: '8px',
    padding: '20px',
})

export const inputContainer = style({
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
})

export const headerStyle = style({
    ...heading5,
})

export const descriptionStyle = style({
    ...bodyMedium,
})
```

AppEntityNameSection.tsx
```typescript
import { Rule } from 'antd/es/form'
import TextInput from 'web/elements/TextInput'
import Form from 'web/elements/Form'
import * as styles from './AppEntityNameSection.css'

const AppEntityNameSection = () => {
    const validationRule: Rule[] = [
        {
            message: 'Please input the name of the AI App.',
            required: true,
        },
    ]

    return (
        <div className={styles.container}>
            <div className={styles.headerStyle}>Add a name to help you identify the purpose of the AI App.</div>
            <div className={styles.descriptionStyle}>
                This name will display when the AI App responds in Slack or Teams.
            </div>
            <Form>
                <Form.Item name="aiAppName" rules={validationRule} className={styles.inputContainer}>
                    <TextInput
                        title="Name"
                        placeholder="e.g. General FAQ, Engineering FAQ"
                    />
                </Form.Item>
            </Form>
        </div>
    )
}

export default AppEntityNameSection