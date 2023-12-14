import {
  getSelectedNodesOrAllNodes,
} from '@create-figma-plugin/utilities';
import { buildTagTree } from './figmaNode/buildTagTree';

const defaultFileId =  'B5yPvOu7WTkaHQcZn57wIV'
const accessToken = 'enter-figma-access-token-here'

export default async function () {
  const selectedNode = getSelectedNodesOrAllNodes()[0];
  console.log('Current page ID', figma.currentPage)

  async function apiRequest(url: string) {
    console.log('Executing api: ', url)
    const response = await fetch(url, {
      method: 'GET',
      headers: { "x-figma-token": accessToken }
    })

    const json = await response.json();
    return json['images'];
  }
  
  const imagesMap = await apiRequest(`https://api.figma.com/v1/images/${defaultFileId}?ids=${selectedNode.id}`)
  const imageUrl: string = imagesMap[selectedNode.id];
  console.log(imageUrl)

  // TODO: Pass the tag tree of the selected node to the LLM to improve the efficiency of the code generation

  fetch('http://127.0.0.1:8989/generate_code', {
    method: 'POST',
    body: JSON.stringify({ imageUrl }),
    headers: {
      'Content-Type': 'application/json'
    }
  })

  await new Promise(resolve => setTimeout(resolve, 3000));

  figma.closePlugin();
}
